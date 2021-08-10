from time import sleep
import win32gui, win32ui, win32con, win32api
from pywinauto import Desktop


class MeuTeclado:

    def __init__(self):
        # self.NomeProcesso = f"Talisman Online | {NomeServer} | ver.5540\n"
        self.PegarNome()
        self.hwnd = win32gui.FindWindow(None, self.NomeProcesso)
        # hwnd = get_inner_windows(hwnd)['Edit']
        win = win32ui.CreateWindowFromHandle(self.hwnd)

        # dicionario teclado
        self.DicionarioTeclado = {'tab': 0x09, 'f1': 0x70, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33,
                                  '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39}

    def Precionar(self, tecla):
        tecla = str(tecla).lower()

        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, self.DicionarioTeclado[tecla], 0)
        sleep(0.5)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, self.DicionarioTeclado[tecla], 0)

    def PegarNome(self):
        Janelas = Desktop(backend="uia").windows()
        Janelas = [w.window_text() for w in Janelas]

        for nome in Janelas:
            if nome.find('Talisman Online | ') != -1:
                self.NomeProcesso = nome
                break




