from ReadWriteMemory import ReadWriteMemory



class Talisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.process = rwm.get_process_by_name('client.exe')
        self.process.open()

        # ponteiros
        self.health_pointer = self.process.get_pointer(0x00400000 + 0x00D1DB7C, offsets=[0x30, 0x0, 0x44, 0x10, 0x7EC, 0x150, 0x3B8])
        self.mana_pointer = self.process.get_pointer(0x00400000 + 0x00D1DB7C, offsets=[0x30, 0x30, 0x84, 0x3BC])
        self.stamina_pointer = self.process.get_pointer(0x00400000 + 0x00EA6CF4, offsets=[0xB0, 0xC0, 0x24, 0x4, 0x10C, 0x3DC])
        self.selected_enemy_pointer = self.process.get_pointer(0x00400000 + 0x00E98E60, offsets=[0xD0, 0x794, 0x0, 0x24, 0x6C, 0x38, 0x2A4])
        self.health_eni_pointer = self.process.get_pointer(0x00400000 + 0x00EA6B78, offsets=[0x18, 0x59C, 0x0, 0xC, 0x1F4, 0x54, 0x224, 0x50, 0x28, 0x480])

    def get_info(self, valor):
        if valor == 'v': # verifica a vida
            self.health = self.process.read(self.health_pointer)
            return self.health
        elif valor == 'm':  # verifica a mana
            self.mana = self.process.read(self.mana_pointer)
            return self.mana
        elif valor == 's':  # verifica a estamina
            self.stamina = self.process.read(self.stamina_pointer)
            return self.stamina
        elif valor == 'se':  # verifica se tem alguem selecionado
            self.selected_enemy = self.process.read(self.selected_enemy_pointer)
            return self.selected_enemy
        elif valor == 've': # verifica se o inimigo esta morto
            self.health_eni = self.process.read(self.health_eni_pointer)
            return self.health_eni
