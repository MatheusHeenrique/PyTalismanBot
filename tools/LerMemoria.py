from ReadWriteMemory import ReadWriteMemory


class LerTalisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.Process = rwm.get_process_by_name('client.exe')
        self.Process.open()

        # ponteiros
        self.HealthPointer = self.Process.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x320]) # check
        self.ManaPointer = self.Process.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x324]) # check
        self.StaminaPointer = self.Process.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x344])  # check
        self.SelectedEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00EA7CF4, offsets=[0xB4, 0x174, 0x48, 0x28, 0x9C, 0x18, 0x784]) # check
        self.HealthEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00EA7B78,
                                                           offsets=[0x18, 0x59C, 0x0, 0xC, 0x1F4, 0x50, 0x28, 0x224,
                                                                    0x50, 0x28, 0xDB0]) # check

    def CatarInfo(self, valor):
        if valor == 'v':  # verifica a vida
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
        elif valor == 've':  # verifica se o inimigo esta morto
            self.HealthEnemy = self.Process.read(self.HealthEnemyPointer)
            return self.HealthEnemy
