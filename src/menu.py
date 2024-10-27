import copy
from os import system


class Menu:
    def __init__(self):
        self.information = dict()

        character_class = self.getting_character_class()
        if type(character_class) == type([]):
            self.information['Classe'] = character_class[0]
            self.information['Wizard'] = character_class[1]
        else:
            self.information['Classe'] = character_class
            self.information['Wizard'] = None

        self.information['Ataque'] = self.attack()

        healing_information = self.healing('cura')
        self.information['Vida'] = healing_information[0]
        self.information['BotaoCura'] = healing_information[1]
        if len(healing_information) >= 3:
            self.information['VidaFairy'] = healing_information[2]
        else:
            self.information['VidaFairy'] = None

        if self.information['Classe'] in ['assasin', 'monk']:
            self.information['Mana'] = None
            self.information['BotaoMana'] = None
        else:
            healing_information = self.healing('mana')
            self.information['Mana'] = healing_information[0]
            self.information['BotaoMana'] = healing_information[1]

    @staticmethod
    def logo():
        system('cls')
        print('''
         __ __|      \      |      _ _|    ___|     \  |      \       \  |      __ )     _ \   __ __| 
            |       _ \     |        |   \___ \    |\/ |     _ \       \ |      __ \    |   |     |   
            |      ___ \    |        |         |   |   |    ___ \    |\  |      |   |   |   |     |   
           _|    _/    _\  _____|  ___|  _____/   _|  _|  _/    _\  _| \_|     ____/   \___/     _|   
           
        ''')

    def main_menu(self):
        while True:
            self.logo()
            wizzard = self.information["Wizard"]
            print(f'Class: {self.information["Classe"]}{f", {wizzard}" if self.information["Classe"] == "wizard" else ""}')

            stop_healing = self.information["VidaFairy"]
            print(f'Cura: {self.information["Vida"]}{f", {stop_healing}" if stop_healing is not None else ""}')

            print(f'Mana: {self.information["Mana"]}')

            if type(self.information['Ataque']) == type([]):
                for position, attack in enumerate(self.information['Ataque']):
                    print(f'{"Ataque: " if position == 0 else ", "}{attack}', end="")
            else:
                print(f'Ataques: {self.information["Ataque"]}')

            print('\n1 -> Editar classe')
            print('2 -> Editar cura')
            print('3 -> Editar mana')
            print('4 -> Editar Ataque')
            print('5 -> Adicionar magia')
            print('6 -> Pausar\n')

            choice = ''
            while not choice.isdigit():
                choice = input('Comando: ')

            match int(choice):
                case 1:
                    character_class = self.getting_character_class()
                    if type(character_class) == type([]):
                        self.information['Classe'] = character_class[0]
                        self.information['Wizard'] = character_class[1]
                    else:
                        self.information['Classe'] = character_class
                        self.information['Wizard'] = None
                case 2:
                    healing_information = self.healing('cura')
                    self.information['Vida'] = healing_information[0]
                    self.information['BotaoCura'] = healing_information[1]
                    if len(healing_information) >= 3:
                        self.information['VidaFairy'] = healing_information[2]
                    else:
                        self.information['VidaFairy'] = None

                case 3:
                    if self.information['Classe'] in ['assasin', 'monk']:
                        continue
                    mana = self.healing('mana')
                    self.information['Mana'] = mana[0]
                    self.information['BotaoMana'] = mana[1]
                case 4:
                    self.information['Ataque'] = self.attack()
                case 5:
                    self.information['spell'] = self.magic()
                case 6:
                    self.information['pause'] = True

            return self.information

    def getting_character_class(self):
        character_class = ''
        while not character_class.isdigit():
            self.logo()
            print('\nQual a classe do seu personagem?')
            print('\n1 - Fairy \n2 - Tamer')
            print('3 - Assasin  \n4 - Monk')
            print('5 - Wizard')
            character_class = input('Comando: ')

        match int(character_class):
            case 1:
                character_class = 'fairy'
            case 2:
                character_class = 'tamer'
            case 3:
                character_class = 'assasin'
            case 4:
                character_class = 'monk'
            case 5:
                character_class = 'wizard'
                weapon = ''
                while not weapon.isdigit():
                    self.logo()
                    print('Qual arma você usa?')
                    print('\n1 - Fogo \n2 - Gelo')
                    weapon = input('Comando: ')

                    if weapon > '2' or weapon < '1':
                        weapon = ''

                if int(weapon) == 1:
                    weapon = 'fogo'
                else:
                    weapon = 'gelo'

                return [character_class, weapon]

        return character_class

    def attack(self):
        key = ''
        attack_list = None
        while not key.isdigit():
            self.logo()
            key = int(input('Tecla do ataque que deseja usar: '))

            question = ' '
            while question not in 'sn':
                self.logo()
                question = str(input('Adicionar outro ataque? [s/N]')).lower()

            if question == 's':
                if attack_list is None:
                    attack_list = list()
                attack_list.append(key)
                key = ''
            else:
                if attack_list is None:
                    attack_list = key
                else:
                    attack_list.append(key)

                    question = ' '
                    while question not in 'sn':
                        self.logo()
                        question = str(
                            input('Deseja que o ultimo ataque fique repitindo até o mob morrer? [s/n]')).lower()

                    if question == 's':
                        attack_list.append('u')
                    else:
                        attack_list.append('l')
                break

        return attack_list

    def healing(self, tipo):
        amount = ''
        while not amount.isdigit():
            self.logo()
            amount = input(
                f'Com quantos de {"vida" if tipo == "cura" else tipo} deseja que seu personagem use a {tipo}: ')

        button = ''
        while not button.isdigit():
            self.logo()
            button = input(f'Qual botão da {tipo}: ')

        healing = None
        if self.information['Classe'] == 'fairy' and tipo == 'cura':
            stop_healing = ' '
            while stop_healing not in 'sn':
                self.logo()
                stop_healing = input('Você quer que a fairy pare de curar quando chegar a uma quantidade de hp? [s/N]')

            if stop_healing == 's':
                fairy = ''
                while not fairy.isdigit():
                    self.logo()
                    fairy = input('Você quer que a fairy pare de se cura com quantos de hp: ')
                healing = [int(amount), int(button), int(fairy)]
                return healing

        healing = [int(amount), int(button)]
        return healing

    def magic(self):
        button = ''
        while not button.isdigit():
            self.logo()
            button = input('Qual botão da magia: ')

        time = ''
        while not time.isdigit():
            self.logo()
            time = input('Quanto tempo a magia dura: ')

        select = ' '
        while select not in 'sn':
            self.logo()
            select = str(input('Precisa se selecionar para usar? [s/N]'))

        if select == 's':
            select = True
        else:
            select = False

        return [int(button), int(time), select]

    def get_info(self):
        return copy.deepcopy(self.information)

    def remove_from_dictionary(self, string):
        self.information.pop(string)
