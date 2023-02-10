from os import system


class Menu:
    def __init__(self):
        pass
        self.info = dict()
        classe = self.personagem_classe()
        if type(classe) == type([]):
            self.info['Classe'] = classe[0]
            self.info['Wizard'] = classe[1]
        else:
            self.info['Classe'] = classe
            self.info['Wizard'] = None


        self.info['Ataque'] = self.ataque()

        curaInfo = self.cura('cura')
        if self.info['Classe'] == 'fairy':
            self.info['VidaFairy'] = curaInfo[0]
            self.info['Vida'] = None
        else:
            self.info['Vida'] = curaInfo[0]
            self.info['VidaFairy'] = None
        self.info['BotaoCura'] = curaInfo[1]

        curaInfo = self.cura('mana')
        self.info['Mana'] = curaInfo[0]
        self.info['BotaoMana'] = curaInfo[1]

    @staticmethod
    def logo():
        system('cls')
        print('''
         __ __|      \      |      _ _|    ___|     \  |      \       \  |      __ )     _ \   __ __| 
            |       _ \     |        |   \___ \    |\/ |     _ \       \ |      __ \    |   |     |   
            |      ___ \    |        |         |   |   |    ___ \    |\  |      |   |   |   |     |   
           _|    _/    _\  _____|  ___|  _____/   _|  _|  _/    _\  _| \_|     ____/   \___/     _|   
           
        ''')

    def principal(self):
        while True:
            self.logo()
            print(f'Class: {self.info["Classe"]}')

            if self.info['Classe'] == 'fairy':
                print(f'Cura: {self.info["VidaFairy"]}')
            else:
                print(f'Cura: {self.info["Vida"]}')

            print(f'Mana: {self.info["Mana"]}')

            if type(self.info['Ataque']) == type([]):
                for pos, ataque in enumerate(self.info['Ataque']):
                    print(f'{"Ataque: " if pos == 0 else ", "}{ataque}', end="")
            else:
                print(f'Ataques: {self.info["Ataque"]}')

            print('\n1 -> Editar classe')
            print('2 -> Editar cura')
            print('3 -> Editar mana')
            print('4 -> Editar Ataque')
            print('5 -> Adicionar magia')
            print('6 -> sair\n')

            escolha = ''
            while not escolha.isdigit():
                escolha = input('Comando: ')

            match int(escolha):
                case 1:
                    classe = self.personagem_classe()
                    if type(classe) == type([]):
                        self.info['Classe'] = classe[0]
                        self.info['Wizard'] = classe[1]
                    else:
                        self.info['Classe'] = classe
                        self.info['Wizard'] = None
                case 2:
                    cura = self.cura('cura')
                    if self.info['Classe'] == 'fairy':
                        self.info['VidaFairy'] = cura[0]
                    else:
                        self.info['Vida'] = cura[0]
                    self.info['BotaoCura'] = cura[1]
                case 3:
                    mana = self.cura('mana')
                    self.info['Mana'] = mana[0]
                    self.info['BotaoMana'] = mana[1]
                case 4:
                    self.info['Ataque'] = self.ataque()
                case 5:
                    return self.magia()
                case 6:
                    exit()

            return self.info

    def personagem_classe(self):
        classe = ''
        while not classe.isdigit():
            self.logo()
            print('\nQual a classe do seu personagem?')
            print('\n1 - Fairy \n2 - Tamer')
            print('3 - Assasin  \n4 - Wizard')
            classe = input('Comando: ')

        match int(classe):
            case 1:
                classe = 'fairy'
            case 2:
                classe = 'tamer'
            case 3:
                classe = 'assasin'
            case 4:
                classe = 'wizard'
                arma = ''
                while not arma.isdigit():
                    self.logo()
                    print('Qual arma você usa?')
                    print('\n1 - Fogo \n2 - Gelo')
                    arma = input('Comando: ')

                    if arma > '2' or arma < '1':
                        arma = ''

                if int(arma) == 1:
                    arma = 'fogo'
                else:
                    arma = 'gelo'

                return [classe, arma]

        return classe

    def ataque(self):
        tecla = ''
        lista_ataques = None
        while not tecla.isdigit():
            self.logo()
            tecla = int(input('Tecla do ataque que deseja usar: '))

            pergunta = ' '
            while pergunta not in 'sn':
                self.logo()
                pergunta = str(input('Adicionar outro ataque? [s/N]')).lower()

            if pergunta == 's':
                if lista_ataques is None:
                    lista_ataques = list()
                lista_ataques.append(tecla)
                tecla = ''
            else:
                if lista_ataques is None:
                    lista_ataques = tecla
                else:
                    lista_ataques.append(tecla)

                    pergunta = ' '
                    while pergunta not in 'sn':
                        self.logo()
                        pergunta = str(
                            input('Deseja que o ultimo ataque fique repitindo até o mob morrer? [s/n]')).lower()

                    if pergunta == 's':
                        lista_ataques.append('u')
                    else:
                        lista_ataques.append('l')
                break

        return lista_ataques

    def cura(self, tipo):
        quantidade = ''
        while not quantidade.isdigit():
            self.logo()
            quantidade = input(
                f'Com quantos de {"vida" if tipo == "cura" else tipo} deseja que seu personagem use a {tipo}: ')

        botao = ''
        while not botao.isdigit():
            self.logo()
            botao = input(f'Qual botão da {tipo}: ')

        return [int(quantidade), int(botao)]

    def magia(self):
        botao = ''
        while not botao.isdigit():
            self.logo()
            botao = input('Qual botão da magia: ')

        tempo = ''
        while not tempo.isdigit():
            self.logo()
            tempo = input('Quanto tempo a magia dura: ')

        selecionar = ' '
        while selecionar not in 'sn':
            self.logo()
            selecionar = str(input('Precisa se selecionar para usar? [s/N]'))

        if selecionar == 's':
            selecionar = True
        else:
            selecionar = False

        return [int(botao), int(tempo), selecionar]

    def get_info(self):
        return self.info
