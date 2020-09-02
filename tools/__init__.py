from ReadWriteMemory import ReadWriteMemory
from pyautogui import press


class Talisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.Process = rwm.get_process_by_name('client.exe')
        self.Process.open()

        # ponteiros
        self.HealthPointer = self.Process.get_pointer(0x00400000 + 0x00D1DB7C, offsets=[0x30, 0x0, 0x44, 0x10, 0x7EC, 0x150, 0x3B8])
        self.ManaPointer = self.Process.get_pointer(0x00400000 + 0x00D1DB7C, offsets=[0x30, 0x30, 0x84, 0x3BC])
        self.StaminaPointer = self.Process.get_pointer(0x00400000 + 0x00EA6CF4, offsets=[0xB0, 0xC0, 0x24, 0x4, 0x10C, 0x3DC])
        self.SelectedEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00E98E60, offsets=[0xD0, 0x794, 0x0, 0x24, 0x6C, 0x38, 0x2A4])
        self.HealthEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00EA6B78, offsets=[0x18, 0x59C, 0x0, 0xC, 0x1F4, 0x54, 0x224, 0x50, 0x28, 0x480])

    def get_info(self, valor):
        if valor == 'v': # verifica a vida
            self.Health = self.Process.read(self.HealthPointer)
            return self.Health
        elif valor == 'm':  # verifica a mana
            self.Mana = self.Process.read(self.ManaPointer)
            return self.Mana
        elif valor == 's':  # verifica a estamina
            self.Stamina = self.Process.read(self.StaminaPointer)
            return self.Stamina
        elif valor == 'se':  # verifica se tem alguem selecionado
            self.SelectedEnemy = self.Process.read(self.SelectedEnemyPointer)
            return self.SelectedEnemy
        elif valor == 've': # verifica se o inimigo esta morto
            self.HealthEnemy = self.Process.read(self.HealthEnemyPointer)
            return self.HealthEnemy


class Ataque:

    def __init__(self, Personagem):
        self.Classe = Personagem

    def atacar(self, NumAtaque):
        pass

