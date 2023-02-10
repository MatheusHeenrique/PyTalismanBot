from ReadWriteMemory import ReadWriteMemory


class LerMemoria:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.programa = rwm.get_process_by_name('client.exe')
        self.programa.open()

        # ponteiros
        self.ponteiro_vida = self.programa.get_pointer(0x00400000 + 0x00D359E0, offsets=[0x30, 0x10, 0x44, 0x30, 0x50, 0x3B8]) # check
        self.ponteiro_mana = self.programa.get_pointer(0x00400000 + 0x00C5C754, offsets=[0x64, 0x20, 0x48, 0x44, 0x64, 0x30, 0x368]) # check
        self.ponteiro_estamina = self.programa.get_pointer(0x00400000 + 0x00C0E980, offsets=[0x8, 0x40, 0x4, 0x4, 0x4, 0xC, 0x3DC])  # check
        self.ponteiro_selecionar_inimigo = self.programa.get_pointer(0x00400000 + 0x00EB0DE0, offsets=[0xD0, 0x2DC, 0x24, 0x14, 0x2C, 0x9C, 0x30, 0x50, 0x18, 0x744]) # check
        self.ponteiro_vida_inimigo = self.programa.get_pointer(0x00400000 + 0x00D6BA94, offsets=[0x70, 0x19C, 0xC, 0x28, 0x18, 0x4, 0x448, 0x8, 0xC, 0xC00]) # check

    def catar_info(self, campo):
        info = False
        
        match campo:
            case 'v':  # verifica a vida
                info = self.programa.read(self.ponteiro_vida)
            case 'm':  # verifica a mana
                info = self.programa.read(self.ponteiro_mana)
            case's':  # verifica a estamina
                info = self.programa.read(self.ponteiro_estamina)
            case 'se':  # verifica se tem alguem selecionado
                info = self.programa.read(self.ponteiro_selecionar_inimigo)
            case 've':  # verifica se o inimigo esta morto
                info = self.programa.read(self.ponteiro_vida_inimigo)

        return info
