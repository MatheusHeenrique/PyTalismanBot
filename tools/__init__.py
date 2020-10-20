from ReadWriteMemory import ReadWriteMemory
from pyautogui import press, moveTo, click
from time import sleep, time
from math import trunc


class ReadTalisman:
    def __init__(self):
        rwm = ReadWriteMemory()
        self.Process = rwm.get_process_by_name('client.exe')
        self.Process.open()

        # ponteiros
        self.HealthPointer = self.Process.get_pointer(0x00400000 + 0x00D1CB7C, offsets=[0x30, 0x30, 0x84, 0x3B8])
        self.ManaPointer = self.Process.get_pointer(0x00400000 + 0x00D1CB7C, offsets=[0x64, 0x30, 0x7E8, 0x1D4, 0x3BC])
        self.StaminaPointer = self.Process.get_pointer(0x00400000 + 0x00EA6CF4,
                                                       offsets=[0xB0, 0xC0, 0x24, 0x4, 0x10C, 0x3DC])  # atualizar
        self.SelectedEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00E97E60,
                                                             offsets=[0xD0, 0x794, 0x0, 0x24, 0x300])
        self.HealthEnemyPointer = self.Process.get_pointer(0x00400000 + 0x00EA5B78,
                                                           offsets=[0x18, 0x59C, 0x0, 0xC, 0x1F4, 0x50, 0x28, 0x224,
                                                                    0x50, 0x460, 0x918])

    def get_info(self, valor):
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


class ActionTalisman(ReadTalisman):

    def __init__(self, Personagem):
        ReadTalisman.__init__(self)
        self.Classe = Personagem
        self.MagiaInicio = None

    def Atacar(self, Numero):
        # selecionando inimigo
        while True:
            press('tab')
            EnimigoSelect = self.get_info('se')
            if EnimigoSelect >= 1:
                break

        TempoInicio = time()
        # atacando
        while True:
            self.ClasseAtaques(Numero)  # selecione o ataque
            VidaEnimigo = self.get_info('ve')

            # verificando se o bot esta muito tempo parado
            TempoFinal = time()
            Minutos = trunc(TempoFinal - TempoInicio)

            if Minutos > 60:
                break

            if VidaEnimigo == 0:
                break

    def ClasseAtaques(self, NumAtaque):
        # convertendo para string
        #NumAtaque = str(NumAtaque)
        press(str(NumAtaque))

        # fay
        if NumAtaque == 1 and self.Classe == 'f':
            sleep(1.5)
        elif NumAtaque == 2 and self.Classe == 'f':
            sleep(2)

        # sin
        if self.Classe == 's':  # sin
            sleep(1)

    def Autopick(self, Pos=[515, 418], Pulo=55):
        for x in range(417, 623, Pulo):
            for y in range(311, 485, Pulo):
                click(x=x, y=y, button='right')
        moveTo(x=Pos[0], y=Pos[1])
        click()

    def Cura(self, Vida, Mana=None, BotaoCura=None, BotaoMana=None, FayV=3200):
        # cura
        if self.get_info('v') < Vida:

            if self.Classe == 'f':
                press('f1')
                while self.get_info('v') < FayV:
                    press(str(BotaoCura))
                    sleep(1.6)
            else:
                sleep(4)
                press(str(BotaoCura))  # botão em que a vida esta setada
                sleep(15)

        # mana
        if BotaoMana is not None:
            if self.get_info('m') < Mana:
                sleep(4)
                press(str(BotaoMana))  # botão em que a mana esta setada
                sleep(15)

    def UsarMagia(self, NumMagia, tempo):
        tempo = tempo * 60
        if self.MagiaInicio is not None:
            Verif = trunc(time() - self.MagiaInicio)
            if Verif >= self.Tempo:
                self.MagiaInicio = None

        if self.MagiaInicio is None:
            if self.Classe == 'f':
                press('f1')
            press(str(NumMagia))
            self.MagiaInicio = time()
            self.Tempo = tempo
