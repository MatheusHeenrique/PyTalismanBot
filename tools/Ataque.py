from tools.LerMemoria import LerTalisman
from tools.Teclado import MeuTeclado
from time import sleep, time
from math import trunc


class Talisman(LerTalisman):
    def __init__(self, Personagem, Server):
        LerTalisman.__init__(self)
        self.MagiaInicio = None
        self.ClasseInfo = Personagem
        self.Teclado = MeuTeclado(Server)

        if type(self.ClasseInfo['Ataque']) == type(list()):
            self.TipoAtaque = self.ClasseInfo['Ataque'][-1]
            self.ListaAtaque = None

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
                self.ListaAtaque = None # resetar lista de ataques
                break

            if VidaEnimigo == 0:
                self.ListaAtaque = None # resetar lista de ataques
                break

    def Ataque(self):
        # ataque
        if type(self.ClasseInfo['Ataque']) == type(list()):

            # passando a lista de ataques do dicionario para a variavel lista ataque
            if self.ListaAtaque is None:
                self.ListaAtaque = self.ClasseInfo['Ataque'][:-1]

            if self.TipoAtaque == 'l': # vai ficar repetindo
                self.Teclado.Precionar(self.ListaAtaque[0])

                # loop aqui
                self.ListaAtaque.append(self.ListaAtaque[0])
                self.ListaAtaque.pop(0)

            elif self.TipoAtaque == 'u': # vai usar todos ataques e ficar repetindo o ultimo
                self.Teclado.Precionar(self.ListaAtaque[0])

                # repetindo ultimo ataqui
                if len(self.ListaAtaque) > 1:
                    self.ListaAtaque.pop(0)

        else:
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

    def FairyCurar(self, valor):

        while True:
            for i in range(0, 8):
                self.Teclado.Precionar(valor[0])
                sleep(0.5)
            self.Teclado.Precionar(valor[1])
            sleep(0.5)
