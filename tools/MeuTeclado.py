import win32gui
import win32ui
import win32con
import win32api
from time import sleep
from pywinauto import Desktop


class MeuTeclado:
    def __init__(self):
        self.nome_processo = None
        self.pegar_nome()

        self.hwnd = win32gui.FindWindow(None, self.nome_processo)
        win = win32ui.CreateWindowFromHandle(self.hwnd)

        # dicionario teclado
        self.dicionario_teclado = {
            'tab': 0x09,
            'f1': 0x70,
            '0': 0x30,
            '1': 0x31,
            '2': 0x32,
            '3': 0x33,
            '4': 0x34,
            '5': 0x35,
            '6': 0x36,
            '7': 0x37,
            '8': 0x38,
            '9': 0x39
        }

    def precionar(self, tecla):
        tecla = str(tecla).lower()

        win32api.SendMessage(
            self.hwnd,
            win32con.WM_KEYDOWN,
            self.dicionario_teclado[tecla],
            0
        )
        sleep(0.5)
        win32api.SendMessage(
            self.hwnd,
            win32con.WM_KEYUP,
            self.dicionario_teclado[tecla],
            0
        )

    def pegar_nome(self):
        janelas = Desktop(backend="uia").windows()
        janelas = [w.window_text() for w in janelas]

        for nome in janelas:
            if nome.find('Talisman Online | ') != -1:
                self.nome_processo = nome
                break