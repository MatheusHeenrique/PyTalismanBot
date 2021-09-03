from ReadWriteMemory import ReadWriteMemory


class LerTalisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.programa = rwm.get_process_by_name('client.exe')
        self.programa.open()

        # ponteiros
        self.ponteiro_vida = self.programa.get_pointer(0x00400000 + 0x00C0E980, offsets=[0x7A0, 0x64, 0x0, 0xE4, 0x10, 0x218, 0x758]) # check
        self.ponteiro_mana = self.programa.get_pointer(0x00400000 + 0x00D325F0, offsets=[0x64, 0x0, 0x4C, 0x4, 0x7A4, 0x1D8, 0x75C]) # check
        self.ponteiro_estamina = self.programa.get_pointer(0x00400000 + 0x00C0E980, offsets=[0x8, 0x40, 0x4, 0x4, 0x4, 0xC, 0x3DC])  # check
        self.ponteiro_selecionar_inimigo = self.programa.get_pointer(0x00400000 + 0x00EAD9A8, offsets=[0xD0, 0x2DC, 0x24, 0x10, 0x28, 0x2C, 0xA48]) # check
        self.ponteiro_vida_inimigo = self.programa.get_pointer(0x00400000 + 0x00C0E97C, offsets=[0x4, 0xB0, 0x0, 0x8, 0x430, 0x18, 0x0, 0x48, 0x28, 0x80, 0x8F8]) # check

    def catar_info(self, valor):
        if valor == 'v':  # verifica a vida
            self.vida = self.programa.read(self.ponteiro_vida)
            return self.vida
        elif valor == 'm':  # verifica a mana
            self.mana = self.programa.read(self.ponteiro_mana)
            return self.mana
        elif valor == 's':  # verifica a estamina
            self.estamina = self.programa.read(self.ponteiro_estamina)
            return self.estamina
        elif valor == 'se':  # verifica se tem alguem selecionado
            self.selecionar_inimigo = self.programa.read(self.ponteiro_selecionar_inimigo)
            return self.selecionar_inimigo
        elif valor == 've':  # verifica se o inimigo esta morto
            self.vida_inimigo = self.programa.read(self.ponteiro_vida_inimigo)
            return self.vida_inimigo
