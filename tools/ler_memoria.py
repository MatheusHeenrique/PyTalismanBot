from ReadWriteMemory import ReadWriteMemory


class LerTalisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.programa = rwm.get_process_by_name('client.exe')
        self.programa.open()

        # ponteiros
        self.ponteiro_vida = self.programa.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x320]) # check
        self.ponteiro_mana = self.programa.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x324]) # check
        self.ponteiro_estamina = self.programa.get_pointer(0x00400000 + 0x00BFB980, offsets=[0x344])  # check
        self.ponteiro_selecionar_inimigo = self.programa.get_pointer(0x00400000 + 0x00EA7CF4, offsets=[0xB4, 0x174, 0x48, 0x28, 0x9C, 0x18, 0x784]) # check
        self.ponteiro_vida_inimigo = self.programa.get_pointer(0x00400000 + 0x00EA7B78,
                                                               offsets=[0x18, 0x59C, 0x0, 0xC, 0x1F4, 0x50, 0x28, 0x224,
                                                                    0x50, 0x28, 0xDB0]) # check

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
