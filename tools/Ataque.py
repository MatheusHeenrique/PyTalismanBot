# from ReadWriteMemory import ReadWriteMemory
# from tools.Teclado import MeuTeclado
# from time import sleep, time
# from math import trunc
#
# class Talisman(ReadTalisman):
#
#     def __init__(self, Personagem):
#         ReadTalisman.__init__(self)
#         self.Classe = Personagem
#         self.MagiaInicio = None
#         self.Teclado = MeuTeclado()
#
#     def Atacar(self, Numero):
#         # selecionando inimigo
#         while True:
#             self.Teclado.Precionar('tab')
#             EnimigoSelect = self.get_info('se')
#             if EnimigoSelect >= 1:
#                 break
#
#         Verif = 0
#         TempoInicio = time()
#         # atacando
#         while True:
#             if type(Numero) == type(list()):
#                 self.ClasseAtaques(Numero[Verif])
#             else:
#                 self.ClasseAtaques(Numero)  # selecione o ataque
#
#             VidaEnimigo = self.get_info('ve')
#
#             # verificando se o bot esta muito tempo parado
#             TempoFinal = time()
#             Minutos = trunc(TempoFinal - TempoInicio)
#
#             if Minutos > 60:
#                 break
#
#             if VidaEnimigo == 0:
#                 break
#
#             if Verif == 0:
#                 Verif = 1
#
#     def ClasseAtaques(self, NumAtaque):
#         # convertendo para string
#         #NumAtaque = str(NumAtaque)
#         self.Teclado.Precionar(NumAtaque)
#
#         wiz = 'fogo'
#
#         # fay
#         if NumAtaque == 1 and self.Classe == 'f':
#             sleep(1.5)
#         elif NumAtaque == 2 and self.Classe == 'f':
#             sleep(2)
#
#         # tamer
#         if NumAtaque == 1 and self.Classe == 't':
#             sleep(1)
#         elif (NumAtaque == 3 or NumAtaque == 4) and self.Classe == 't':
#             sleep(1.5)
#
#         # wiz
#         if self.Classe == 'w' and wiz == 'fogo':
#             if NumAtaque == 1:
#                 sleep(1.5)
#             elif NumAtaque == 2:
#                 sleep(2.2)
#             elif NumAtaque == 4:
#                 sleep(1)
#         elif self.Classe == 'w' and wiz == 'gelo':
#             if NumAtaque == 1:
#                 sleep(1)
#             elif NumAtaque == 3:
#                 sleep(2.5)
#
#     def Cura(self, Vida, Mana=None, BotaoCura=None, BotaoMana=None, FayV=3200):
#         # cura
#         if self.get_info('v') < Vida:
#
#             if self.Classe == 'f':
#                 self.Teclado.Precionar('f1')
#                 while self.get_info('v') < FayV:
#                     self.Teclado.Precionar(BotaoCura)
#                     sleep(1.6)
#             else:
#                 sleep(4)
#                 self.Teclado.Precionar(BotaoCura)  # botão em que a vida esta setada
#                 sleep(15)
#
#         # mana
#         if BotaoMana is not None:
#             if self.get_info('m') < Mana:
#                 sleep(4)
#                 self.Teclado.Precionar(BotaoMana)  # botão em que a mana esta setada
#                 sleep(15)
#
#     def UsarMagia(self, NumMagia, tempo):
#         tempo = tempo * 60
#         if self.MagiaInicio is not None:
#             Verif = trunc(time() - self.MagiaInicio)
#             if Verif >= self.Tempo:
#                 self.MagiaInicio = None
#
#         if self.MagiaInicio is None:
#             if self.Classe == 'f':
#                 self.Teclado.Precionar('f1')
#             self.Teclado.Precionar(NumMagia)
#             self.MagiaInicio = time()
#             self.Tempo = tempo
from tools.LerMemoria import LerTalisman
from tools.Teclado import MeuTeclado
from time import sleep, time
from math import trunc


class Talisman(LerTalisman):
    def __init__(self, config):
        LerTalisman.__init__(self)
        self.MagiaInicio = None
        self.ClasseInfo = config
        self.Teclado = MeuTeclado()

    def Atacar(self):
        # selecionando inimigo
        while True:
            self.Teclado.Precionar('tab')
            EnimigoSelecionado = self.CatarInfo('se')
            if EnimigoSelecionado >= 1:
                break

        TempoInicio = time()
        while True:
            self.Ataque()

            VidaEnimigo = self.CatarInfo('ve')

            # verificando se o bot esta muito tempo parado
            TempoFinal = time()
            Minutos = trunc(TempoFinal - TempoInicio)

            if Minutos > 60:
                break

            if VidaEnimigo == 0:
                break

    def Ataque(self):
        # ataque
        self.Teclado.Precionar(self.ClasseInfo['Ataque'])


        # fay
        if self.ClasseInfo['Ataque'] == 1 and self.ClasseInfo['Classe'][0] == 'f':
            sleep(1.5)
        elif self.ClasseInfo['Ataque'] == 2 and self.ClasseInfo['Classe'][0] == 'f':
            sleep(2)

        # tamer
        if self.ClasseInfo['Ataque'] == 1 and self.ClasseInfo['Classe'][0] == 't':
            sleep(1)
        elif (self.ClasseInfo['Ataque'] == 3 or self.ClasseInfo['Ataque'] == 4) and self.ClasseInfo['Classe'][0] == 't':
            sleep(1.5)

        # wiz
        if self.ClasseInfo['Classe'][0] == 'w' and self.ClasseInfo['Wizard'] == 'fogo':
            if self.ClasseInfo['Ataque'] == 1:
                sleep(1.5)
            elif self.ClasseInfo['Ataque'] == 2:
                sleep(2.2)
            elif self.ClasseInfo['Ataque'] == 4:
                sleep(1)
        elif self.ClasseInfo['Classe'][0] == 'w' and self.ClasseInfo['Wizard'] == 'gelo':
            if self.ClasseInfo['Ataque'] == 1:
                sleep(1)
            elif self.ClasseInfo['Ataque'] == 3:
                sleep(2.5)

    def UsarMagia(self, NumeroMagia, Tempo):

        if self.MagiaInicio is not None:
            Verif = trunc(time() - self.MagiaInicio)
            if Verif >= self.TempoMagia:
                self.MagiaInicio = None

        if self.MagiaInicio is None:
            if self.ClasseInfo['Classe'][0] == 'f':
                self.Teclado.Precionar('f1')
            self.Teclado.Precionar(NumeroMagia)
            self.MagiaInicio = time()
            self.TempoMagia = Tempo * 60

    def Curar(self):
        # cura
        if self.CatarInfo('v') < self.ClasseInfo['Vida']:

            if self.ClasseInfo['Classe'][0] == 'f':
                self.Teclado.Precionar('f1')
                while self.CatarInfo('v') < self.ClasseInfo['VidaFairy']:
                    self.Teclado.Precionar(self.ClasseInfo['BotaoCura'])
                    sleep(1.6)
            else:
                sleep(4)
                self.Teclado.Precionar(self.ClasseInfo['BotaoCura'])  # botão em que a vida esta setada
                sleep(15)

        # mana
        if self.ClasseInfo['Mana'] is not None:
            if self.CatarInfo('m') < self.ClasseInfo['Mana']:
                sleep(4)
                self.Teclado.Precionar(self.ClasseInfo['BotaoMana'])  # botão em que a mana esta setada
                sleep(15)




