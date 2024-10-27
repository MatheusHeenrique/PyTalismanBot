import win32gui
import win32ui
import win32con
import win32api
from time import sleep
from pywinauto import Desktop


class MyKeyboard:
    def __init__(self):
        self.process_name = None
        self.get_name()

        self.hwnd = win32gui.FindWindow(None, self.process_name)
        win = win32ui.CreateWindowFromHandle(self.hwnd)

        # dicionario teclado
        self.key_dictionary = {
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

    def press(self, key):
        key = str(key).lower()

        win32api.SendMessage(
            self.hwnd,
            win32con.WM_KEYDOWN,
            self.key_dictionary[key],
            0
        )
        sleep(0.5)
        win32api.SendMessage(
            self.hwnd,
            win32con.WM_KEYUP,
            self.key_dictionary[key],
            0
        )

    def get_name(self):
        windows = Desktop(backend="uia").windows()
        windows = [w.window_text() for w in windows]

        for name in windows:
            if name.find('Talisman Online | ') != -1:
                self.process_name = name
                break
