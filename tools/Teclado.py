from time import sleep
import win32gui, win32ui, win32con, win32api


class MeuTeclado:

    def __init__(self, NomeServer):
        self.NomeProcesso = f"Talisman Online | {NomeServer} | ver.5540\n"
        self.hwnd = win32gui.FindWindow(None, self.NomeProcesso)
        # hwnd = get_inner_windows(hwnd)['Edit']
        win = win32ui.CreateWindowFromHandle(self.hwnd)

    def Precionar(self, tecla):

        if tecla == 'tab':
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x09, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x09, 0)
        elif tecla == 'f1':
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x70, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x70, 0)
        elif tecla == 0:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x30, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x30, 0)
        elif tecla == 1:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x31, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x31, 0)
        elif tecla == 2:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x32, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x32, 0)
        elif tecla == 3:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x33, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x33, 0)
        elif tecla == 4:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x34, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x34, 0)
        elif tecla == 5:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x35, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x35, 0)
        elif tecla == 6:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x36, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x36, 0)
        elif tecla == 7:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x37, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x37, 0)
        elif tecla == 8:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x38, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x38, 0)
        elif tecla == 9:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, 0x39, 0)
            sleep(0.5)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, 0x39, 0)
