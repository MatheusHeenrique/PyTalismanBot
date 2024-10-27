import ctypes
from ctypes import wintypes

# Constants
PROCESS_ALL_ACCESS = 0x1F0FFF

TH32CS_SNAPHEAPLIST = 0x00000001
TH32CS_SNAPPROCESS  = 0x00000002
TH32CS_SNAPTHREAD   = 0x00000004
TH32CS_SNAPMODULE   = 0x00000008
TH32CS_SNAPMODULE32 = 0x00000010
TH32CS_SNAPALL      = 0x0000001F
TH32CS_INHERIT      = 0x80000000

INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value

# Define ULONG_PTR based on pointer size
if ctypes.sizeof(ctypes.c_void_p) == 8:
    ULONG_PTR = ctypes.c_uint64
else:
    ULONG_PTR = ctypes.c_uint32

# Structures
class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize',          wintypes.DWORD),
        ('cntUsage',        wintypes.DWORD),
        ('th32ProcessID',   wintypes.DWORD),
        ('th32DefaultHeapID', ULONG_PTR),
        ('th32ModuleID',    wintypes.DWORD),
        ('cntThreads',      wintypes.DWORD),
        ('th32ParentProcessID', wintypes.DWORD),
        ('pcPriClassBase',  wintypes.LONG),
        ('dwFlags',         wintypes.DWORD),
        ('szExeFile',       wintypes.CHAR * 260),
    ]

class MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize',          wintypes.DWORD),
        ('th32ModuleID',    wintypes.DWORD),
        ('th32ProcessID',   wintypes.DWORD),
        ('GlblcntUsage',    wintypes.DWORD),
        ('ProccntUsage',    wintypes.DWORD),
        ('modBaseAddr',     wintypes.LPVOID),
        ('modBaseSize',     wintypes.DWORD),
        ('hModule',         wintypes.HMODULE),
        ('szModule',        wintypes.CHAR * 256),
        ('szExePath',       wintypes.CHAR * 260),
    ]

# Functions
CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
Process32First = ctypes.windll.kernel32.Process32First
Process32Next = ctypes.windll.kernel32.Process32Next
Module32First = ctypes.windll.kernel32.Module32First
Module32Next = ctypes.windll.kernel32.Module32Next
OpenProcess = ctypes.windll.kernel32.OpenProcess
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
CloseHandle = ctypes.windll.kernel32.CloseHandle

class MemoryReader:
    def get_final_address(self, processName, baseOffset, offsets):
        
        pid = self.get_pid_by_name(processName)
        if not pid:
            print("Processo não encontrado.")
            return 0

        # Open the process with full access
        hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not hProcess:
            print("Falha ao abrir o processo com acesso total.")
            return 0

        snapFlags = TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32
        hSnapshot = CreateToolhelp32Snapshot(snapFlags, pid)
        if hSnapshot == INVALID_HANDLE_VALUE:
            print("Falha ao criar snapshot.")
            CloseHandle(hProcess)
            return 0

        me32 = MODULEENTRY32()
        me32.dwSize = ctypes.sizeof(MODULEENTRY32)

        found = False
        if Module32First(hSnapshot, ctypes.byref(me32)):
            while True:
                szModule = me32.szModule.decode('utf-8')
                if szModule.lower() == processName.lower():
                    found = True
                    modBaseAddr = me32.modBaseAddr
                    break
                if not Module32Next(hSnapshot, ctypes.byref(me32)):
                    break

        CloseHandle(hSnapshot)

        if not found:
            print("Módulo não encontrado.")
            CloseHandle(hProcess)
            return 0

        modBaseAddr_value = modBaseAddr  # Use the integer address directly
        initialAddress = modBaseAddr_value + baseOffset
        currentAddress = initialAddress

        for offset in offsets:
            value = self.read_pointer(hProcess, currentAddress)
            if value == 0 or value > 0x7FFFFFFF:
                print(f"Falha ao ler memória no endereço {currentAddress:#x}")
                CloseHandle(hProcess)
                return 0
            currentAddress = value + offset

        CloseHandle(hProcess)
        return currentAddress

    def read_pointer(self, hProcess, address):
        buffer = ctypes.c_uint32()
        bytesRead = ctypes.c_size_t()
        result = ReadProcessMemory(
            hProcess, 
            ctypes.c_void_p(address), 
            ctypes.byref(buffer), 
            ctypes.sizeof(buffer), 
            ctypes.byref(bytesRead)
        )
        if not result:
            return 0
        return buffer.value

    def read_memory(self, processName, address, tamanho=4):
        pid = self.get_pid_by_name(processName)
        if not pid:
            print("Processo não encontrado.")
            return None

        hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not hProcess:
            print("Falha ao abrir o processo com acesso total.")
            return None

        buffer = (ctypes.c_char * tamanho)()
        bytesRead = ctypes.c_size_t()
        result = ReadProcessMemory(
            hProcess, 
            ctypes.c_void_p(address), 
            buffer, 
            tamanho, 
            ctypes.byref(bytesRead)
        )
        if not result:
            print(f"Falha ao ler a memória no endereço {address:#x}")
            CloseHandle(hProcess)
            return None

        CloseHandle(hProcess)

        if tamanho == 8:
            valor = ctypes.c_int64.from_buffer(buffer).value
        else:
            valor = ctypes.c_int.from_buffer(buffer).value

        return valor

    def get_pid_by_name(self, process_name):
        snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        pe32 = PROCESSENTRY32()
        pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)
        pid = None

        if Process32First(snapshot, ctypes.byref(pe32)):
            while True:
                exe_file = pe32.szExeFile.decode('utf-8')
                if exe_file.lower() == process_name.lower():
                    pid = pe32.th32ProcessID
                    break
                if not Process32Next(snapshot, ctypes.byref(pe32)):
                    break

        CloseHandle(snapshot)
        return pid