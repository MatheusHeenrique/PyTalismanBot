from ReadWriteMemory import ReadWriteMemory
from tools.teclado import MeuTeclado
from time import sleep, time
from math import trunc


class ReadTalisman:
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


class Talisman(ReadTalisman):

    def __init__(self, Personagem):
        ReadTalisman.__init__(self)
        self.Classe = Personagem
        self.MagiaInicio = None
        self.Teclado = MeuTeclado()

    def Atacar(self, Numero):
        # selecionando inimigo
        while True:
            self.Teclado.Precionar('tab')
            EnimigoSelect = self.get_info('se')
            if EnimigoSelect >= 1:
                break

        Verif = 0
        TempoInicio = time()
        # atacando
        while True:
            if type(Numero) == type(list()):
                self.ClasseAtaques(Numero[Verif])
            else:
                self.ClasseAtaques(Numero)  # selecione o ataque

            VidaEnimigo = self.get_info('ve')

            # verificando se o bot esta muito tempo parado
            TempoFinal = time()
            Minutos = trunc(TempoFinal - TempoInicio)

            if Minutos > 60:
                break

            if VidaEnimigo == 0:
                break

            if Verif == 0:
                Verif = 1

    def ClasseAtaques(self, NumAtaque):
        # convertendo para string
        #NumAtaque = str(NumAtaque)
        self.Teclado.Precionar(NumAtaque)

        wiz = 'fogo'

        # fay
        if NumAtaque == 1 and self.Classe == 'f':
            sleep(1.5)
        elif NumAtaque == 2 and self.Classe == 'f':
            sleep(2)

        # tamer
        if NumAtaque == 1 and self.Classe == 't':
            sleep(1)
        elif (NumAtaque == 3 or NumAtaque == 4) and self.Classe == 't':
            sleep(1.5)

        # wiz
        if self.Classe == 'w' and wiz == 'fogo':
            if NumAtaque == 1:
                sleep(1.5)
            elif NumAtaque == 2:
                sleep(2.2)
            elif NumAtaque == 4:
                sleep(1)
        elif self.Classe == 'w' and wiz == 'gelo':
            if NumAtaque == 1:
                sleep(1)
            elif NumAtaque == 3:
                sleep(2.5)

    def Cura(self, Vida, Mana=None, BotaoCura=None, BotaoMana=None, FayV=3200):
        # cura
        if self.get_info('v') < Vida:

            if self.Classe == 'f':
                self.Teclado.Precionar('f1')
                while self.get_info('v') < FayV:
                    self.Teclado.Precionar(BotaoCura)
                    sleep(1.6)
            else:
                sleep(4)
                self.Teclado.Precionar(BotaoCura)  # botão em que a vida esta setada
                sleep(15)

        # mana
        if BotaoMana is not None:
            if self.get_info('m') < Mana:
                sleep(4)
                self.Teclado.Precionar(BotaoMana)  # botão em que a mana esta setada
                sleep(15)

    def UsarMagia(self, NumMagia, tempo):
        tempo = tempo * 60
        if self.MagiaInicio is not None:
            Verif = trunc(time() - self.MagiaInicio)
            if Verif >= self.Tempo:
                self.MagiaInicio = None

        if self.MagiaInicio is None:
            if self.Classe == 'f':
                self.Teclado.Precionar('f1')
            self.Teclado.Precionar(NumMagia)
            self.MagiaInicio = time()
            self.Tempo = tempo
