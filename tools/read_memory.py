from ReadWriteMemory import ReadWriteMemory


class ReadMemory:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.program = rwm.get_process_by_name('client.exe')
        self.program.open()

        # ponteiros
        self.pointer_life = self.program.get_pointer(0x00400000 + 0x00D359E0, offsets=[0x30, 0x10, 0x44, 0x30, 0x50, 0x3B8]) # check
        self.mana_pointer = self.program.get_pointer(0x00400000 + 0x00C5C754, offsets=[0x64, 0x20, 0x48, 0x44, 0x64, 0x30, 0x368]) # check
        self.stamina_pointer = self.program.get_pointer(0x00400000 + 0x00C0E980, offsets=[0x8, 0x40, 0x4, 0x4, 0x4, 0xC, 0x3DC])  # check
        self.pointer_select_enemy = self.program.get_pointer(0x00400000 + 0x00EB0DE0, offsets=[0xD0, 0x2DC, 0x24, 0x14, 0x2C, 0x9C, 0x30, 0x50, 0x18, 0x744]) # check
        self.enemy_life_pointer = self.program.get_pointer(0x00400000 + 0x00D6BA94, offsets=[0x70, 0x19C, 0xC, 0x28, 0x18, 0x4, 0x448, 0x8, 0xC, 0xC00]) # check

    def get_information(self, field):
        information = False
        
        match field:
            case 'v':  # verifica a vida
                information = self.program.read(self.pointer_life)
            case 'm':  # verifica a mana
                information = self.program.read(self.mana_pointer)
            case's':  # verifica a estamina
                information = self.program.read(self.stamina_pointer)
            case 'se':  # verifica se tem alguem selecionado
                information = self.program.read(self.pointer_select_enemy)
            case 've':  # verifica se o inimigo esta morto
                information = self.program.read(self.enemy_life_pointer)

        return information
