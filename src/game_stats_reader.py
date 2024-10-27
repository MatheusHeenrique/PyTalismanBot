from src.memory_reader import MemoryReader

class GameStatsReader:
    def __init__(self):
        self.reader = MemoryReader()
        self.processName = "client.exe"

    def get_information(self, field):
        information = False
        
        match field:
            case 'v':  # verifica a vida
                base_address = 0x00D39C0C
                offsets = [0x30, 0x18, 0x44, 0x38, 0x364]
                finalAddress = self.reader.get_final_address(self.processName, base_address, offsets)
                information = self.reader.read_memory(self.processName, finalAddress)

            case 'm':  # verifica a mana
                base_address = 0x00D39C0C
                offsets = [0x30, 0x38, 0x44, 0x40, 0x368]
                finalAddress = self.reader.get_final_address(self.processName, base_address, offsets)
                information = self.reader.read_memory(self.processName, finalAddress)

            case's':  # verifica a estamina
                base_address = 0x00C15980
                offsets = [0x8, 0x68, 0x40, 0x38, 0x4, 0x24, 0x3DC]
                finalAddress = self.reader.get_final_address(self.processName, base_address, offsets)
                information = self.reader.read_memory(self.processName, finalAddress)
                
            case 'se':  # verifica se tem alguem selecionado
                base_address = 0x00EC2EA4
                offsets = [0xB4, 0x1B0, 0x44, 0x2C, 0x9C, 0x28, 0x784]
                finalAddress = self.reader.get_final_address(self.processName, base_address, offsets)
                information = self.reader.read_memory(self.processName, finalAddress)

            case 've':  # verifica se o inimigo esta morto
                base_address = 0x00D6FCC8
                offsets = [0x70, 0x464, 0xC, 0x18, 0x4, 0x448, 0xC00]
                finalAddress = self.reader.get_final_address(self.processName, base_address, offsets)
                information = self.reader.read_memory(self.processName, finalAddress)

        return information
