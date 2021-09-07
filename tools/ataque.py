from tools.ler_memoria import LerTalisman
from tools.teclado import MeuTeclado
from time import sleep, time
from math import trunc


class Talisman(LerTalisman):
    def __init__(self, personagem):
        LerTalisman.__init__(self)
        self.magia = []
        self.classe_info = personagem
        self.teclado = MeuTeclado()

        if type(self.classe_info['Ataque']) == type(list()):
            self.tipo_ataque = self.classe_info['Ataque'][-1]
            self.lista_ataque = None

    def atacar(self):
        # selecionando inimigo
        while True:
            self.teclado.precionar('tab')
            enimigo_selecionado = self.catar_info('se')
            if enimigo_selecionado >= 1:
                break

        tempo_inicio = time()
        while True:
            self.ataque()

            vida_enimigo = self.catar_info('ve')

            # verificando se o bot esta muito tempo parado
            tempo_final = time()
            minutos = trunc(tempo_final - tempo_inicio)

            if minutos > 60:
                self.lista_ataque = None  # resetar lista de ataques
                break

            if vida_enimigo == 0:
                self.lista_ataque = None  # resetar lista de ataques
                break

    def ataque(self):
        # ataque
        if type(self.classe_info['Ataque']) == type(list()):

            # passando a lista de ataques do dicionario para a variavel lista ataque
            if self.lista_ataque is None:
                self.lista_ataque = self.classe_info['Ataque'][:-1]

            if self.tipo_ataque == 'l':  # vai ficar repetindo
                self.teclado.precionar(self.lista_ataque[0])

                # loop aqui
                self.lista_ataque.append(self.lista_ataque[0])
                self.lista_ataque.pop(0)

            elif self.tipo_ataque == 'u':  # vai usar todos ataques e ficar repetindo o ultimo
                self.teclado.precionar(self.lista_ataque[0])

                # repetindo ultimo ataqui
                if len(self.lista_ataque) > 1:
                    self.lista_ataque.pop(0)

        else:
            self.teclado.precionar(self.classe_info['Ataque'])

        # fay
        if self.classe_info['Ataque'] == 1 and self.classe_info['Classe'][0] == 'f':
            sleep(1.5)
        elif self.classe_info['Ataque'] == 2 and self.classe_info['Classe'][0] == 'f':
            sleep(2)

        # tamer
        if self.classe_info['Ataque'] == 1 and self.classe_info['Classe'][0] == 't':
            sleep(1)
        elif (self.classe_info['Ataque'] == 3 or self.classe_info['Ataque'] == 4) and self.classe_info['Classe'][
            0] == 't':
            sleep(1.5)

        # wiz
        if self.classe_info['Classe'][0] == 'w' and self.classe_info['Wizard'] == 'fogo':
            if self.classe_info['Ataque'] == 1:
                sleep(1.5)
            elif self.classe_info['Ataque'] == 2:
                sleep(2.2)
            elif self.classe_info['Ataque'] == 4:
                sleep(1)
        elif self.classe_info['Classe'][0] == 'w' and self.classe_info['Wizard'] == 'gelo':
            if self.classe_info['Ataque'] == 1:
                sleep(1)
            elif self.classe_info['Ataque'] == 3:
                sleep(2.5)

    def usar_magia(self, numero_magia, tempo, se_selecionar=False):
        # fazendo uma lista com todas as magia existentes
        if self.magia != []:
            # verificando se ja foi addicionado essa magia a lista
            for lista_magia in self.magia:
                if lista_magia[0] == numero_magia:
                    verificar_lista = True
                    break
                else:
                    verificar_lista = False

            # se não foi adicionado vai adicionar aqui
            if verificar_lista is False:
                self.magia.append([numero_magia, tempo * 60, se_selecionar, None])
        else:
            self.magia.append([numero_magia, tempo * 60, se_selecionar, None])

        # usand magia
        for pos_lista, lista_magia in enumerate(self.magia):
            if lista_magia[3] is not None:
                verificar_tempo = trunc(time() - lista_magia[3])
                if verificar_tempo >= lista_magia[1]:
                    lista_magia.pop(3)
                    lista_magia.append(None)

                    # atualizando a variavel self.magia
                    # self.magia.pop(pos_lista)
                    # self.magia.insert(pos_lista, lista_magia)

            if lista_magia[3] is None:

                # verificando se é para se selecionar
                if lista_magia[2] is True:
                    self.teclado.precionar('f1')

                # precionando tecla e ativando time
                for i in range(2):
                    self.teclado.precionar(lista_magia[0])
                lista_magia.pop(3)
                lista_magia.append(time())

                # atualizando a variavel self.magia
                # self.magia.pop(pos_lista)
                # self.magia.insert(pos_lista, lista_magia)


        # if self.magia_inicio != []:
        #     for i in len(self.magia_inicio):
        #         inicio = self.magia_inicio[i-1]
        #         verificar = trunc(time() - inicio[1])
        #         if verificar >= inicio[2]:
        #             self.magia_inicio.pop(i)
        #
        # if self.magia_inicio == [] or :
        #     if self.classe_info['Classe'][0] == 'f':
        #         self.teclado.precionar('f1')
        #     self.teclado.precionar(numero_magia)
        #     self.magia_inicio.append([numero_magia, time(), tempo * 60])
        #     # self.tempo_magia = tempo * 60

    def curar(self):
        # se o usuario não tiver colocado com quanto ele quer que se cure
        # o programa vai se curar quando tiver com 40 da mana ou da vida
        if self.classe_info['Vida'] is None:
            vida_total = self.catar_info('v') * 40
            self.classe_info['Vida'] = trunc(vida_total / 100)

        if self.classe_info['Mana'] is None:
            mana_total = self.catar_info('m') * 40
            self.classe_info['Mana'] = trunc(mana_total / 100)

        # cura
        if self.catar_info('v') < self.classe_info['Vida']:

            if self.classe_info['Classe'][0] == 'f':
                self.teclado.precionar('f1')
                while self.catar_info('v') < self.classe_info['VidaFairy']:
                    self.teclado.precionar(self.classe_info['BotaoCura'])
                    sleep(1.6)
            else:
                sleep(4)
                self.teclado.precionar(self.classe_info['BotaoCura'])  # botão em que a vida esta setada
                sleep(15)

        # mana
        if self.classe_info['Mana'] is not None:
            if self.catar_info('m') < self.classe_info['Mana']:
                sleep(4)
                self.teclado.precionar(self.classe_info['BotaoMana'])  # botão em que a mana esta setada
                sleep(15)

    def fairy_curar(self, valor):
        while True:
            for i in range(0, 8):
                self.teclado.precionar(valor[0])
                sleep(0.5)
            self.teclado.precionar(valor[1])
            sleep(0.5)
