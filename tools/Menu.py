from os import system
class Menu:
    def __init__(self):
        self.info = dict()
        self.info['Classe'] = self.personagem_classe()
        self.info['Ataque'] = self.ataque()

        curaInfo = self.cura('cura')
        if self.info['Classe'] == 'fairy':
            self.info['VidaFairy'] = curaInfo[0]
        else:
            self.info['Vida'] = curaInfo[0]
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
        pass

    def personagem_classe(self):
        classe = ''
        while not(classe.isdigit()):
            self.logo()
            print('\nQual a classe do seu personagem?')
            print('\n1 - Fairy \n2 - Tamer')
            print('3 - Assasin  \n4 - Wizard')
            classe = input('Comando: ')

        match classe:
            case 1:
                classe = 'fairy'
            case 2:
                classe = 'tamer'
            case 3:
                classe = 'assasin'
            case 4:
                classe = 'wizard'

        return classe

    def ataque(self):
        tecla = ''
        lista_ataques = None
        while not(tecla.isdigit()):
            self.logo()
            tecla = int(input('Tecla do ataque que deseja usar: '))

            pergunta = ' '
            while pergunta not in 'sn':
                self.logo()
                pergunta = str(input('Adicionar outro ataque? [s/N]')).lower()

            if pergunta == 's':
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
                        pergunta = str(input('Deseja que o ultimo ataque fique repitindo até o mob morrer? [s/n]')).lower()

                    if pergunta == 's':
                        lista_ataques.append('u')
                    else:
                        lista_ataques.append('l')
                break

        return lista_ataques

    def cura(self, tipo):
        quantidade = ''
        while type(quantidade) == str:
            self.logo()
            quantidade = int(input(f'Com quantos de {"vida" if tipo == "cura" else tipo} deseja que seu personagem use a {tipo}: '))

        botao = ''
        while type(botao) == str:
            self.logo()
            botao = int(input(f'Qual botão da {tipo}: '))

        return [quantidade, botao]

    def getInfo(self):
        return self.info
