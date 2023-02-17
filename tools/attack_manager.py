from tools.read_memory import ReadMemory
from tools.my_keyboard import MyKeyboard
from time import sleep, time
from math import trunc


class AttackManager(ReadMemory):
    def __init__(self, character):
        ReadMemory.__init__(self)
        self.magic = []
        self.information_character = character
        self.keyboard = MyKeyboard()

        if isinstance(self.information_character['Ataque'], list):
            self.attack_type = self.information_character['Ataque'][-1]
            self.attack_list = None

    def to_attack(self):
        # selecionando inimigo
        while True:
            self.keyboard.press('tab')
            selected_enemy = self.get_information('se')
            if selected_enemy >= 1:
                break

        time_it_started = time()
        while True:
            self.attack()

            enemy_life = self.get_information('ve')

            # verificando se o bot esta muito tempo parado
            time_its_over = time()
            minutes = trunc(time_its_over - time_it_started)

            if minutes > 60:
                self.attack_list = None  # resetar lista de ataques
                break

            if enemy_life == 0:
                self.attack_list = None  # resetar lista de ataques
                break

    def attack(self):
        # ataque
        if isinstance(self.information_character['Ataque'], list):

            # passando a lista de ataques do dicionario para a variavel lista ataque
            if self.attack_list is None:
                self.attack_list = self.information_character['Ataque'][:-1]

            if self.attack_type == 'l':  # vai ficar repetindo
                self.keyboard.press(self.attack_list[0])

                # loop aqui
                self.attack_list.append(self.attack_list[0])
                self.attack_list.pop(0)

            elif self.attack_type == 'u':  # vai usar todos ataques e ficar repetindo o ultimo
                self.keyboard.press(self.attack_list[0])

                # repetindo ultimo ataqui
                if len(self.attack_list) > 1:
                    self.attack_list.pop(0)

        else:
            self.keyboard.press(self.information_character['Ataque'])

        # fay
        if self.information_character['Ataque'] == 1 and self.information_character['Classe'][0] == 'f':
            sleep(1.5)
        elif self.information_character['Ataque'] == 2 and self.information_character['Classe'][0] == 'f':
            sleep(2)

        # tamer
        if self.information_character['Ataque'] == 1 and self.information_character['Classe'][0] == 't':
            sleep(1)
        elif (self.information_character['Ataque'] == 3 or self.information_character['Ataque'] == 4) and self.information_character['Classe'][
            0] == 't':
            sleep(1.5)

        # wiz
        if self.information_character['Classe'][0] == 'w' and self.information_character['Wizard'] == 'fogo':
            if self.information_character['Ataque'] == 1:
                sleep(1.5)
            elif self.information_character['Ataque'] == 2:
                sleep(2.2)
            elif self.information_character['Ataque'] == 4:
                sleep(1)
        elif self.information_character['Classe'][0] == 'w' and self.information_character['Wizard'] == 'gelo':
            if self.information_character['Ataque'] == 1:
                sleep(1)
            elif self.information_character['Ataque'] == 3:
                sleep(2.5)

    def use_magic(self, magic_number, tempo, self_select=False):
        # fazendo uma lista com todas as magia existentes
        if self.magic != []:
            # verificando se ja foi addicionado essa magia a lista
            for spell_list in self.magic:
                if spell_list[0] == magic_number:
                    check_list = True
                    break
                else:
                    check_list = False

            # se não foi adicionado vai adicionar aqui
            if not check_list:
                self.magic.append([magic_number, tempo * 60, self_select, None])
        else:
            self.magic.append([magic_number, tempo * 60, self_select, None])

        # usand magia
        for position, spell_list in enumerate(self.magic):
            if spell_list[3] is not None:
                check_time = trunc(time() - spell_list[3])
                if check_time >= spell_list[1]:
                    spell_list.pop(3)
                    spell_list.append(None)

            if spell_list[3] is None:

                # verificando se é para se selecionar
                if spell_list[2] is True:
                    self.keyboard.press('f1')

                # precionando tecla e ativando time
                for i in range(2):
                    self.keyboard.press(spell_list[0])
                spell_list.pop(3)
                spell_list.append(time())

    def heal(self):
        # se o usuario não tiver colocado com quanto ele quer que se cure
        # o programa vai se curar quando tiver com 40 da mana ou da vida

        if self.information_character['Classe'][0] == 'f' and self.information_character['VidaFairy'] is None:
            total_life = self.get_information('v') * 82
            self.information_character['VidaFairy'] = trunc(total_life / 100)

        if self.information_character['Vida'] is None:
            total_life = self.get_information('v') * 40
            self.information_character['Vida'] = trunc(total_life / 100)

        if self.information_character['Mana'] is None:
            total_mana = self.get_information('m') * 40
            self.information_character['Mana'] = trunc(total_mana / 100)

        # cura
        if self.get_information('v') < self.information_character['Vida']:

            if self.information_character['Classe'][0] == 'f':
                self.keyboard.press('f1')
                while self.get_information('v') < self.information_character['VidaFairy']:
                    self.keyboard.press(self.information_character['BotaoCura'])
                    sleep(1.6)
            else:
                sleep(4)
                self.keyboard.press(self.information_character['BotaoCura'])  # botão em que a vida esta setada
                sleep(15)

        # mana
        if self.information_character['Mana'] is not None:
            if self.get_information('m') < self.information_character['Mana']:
                sleep(4)
                self.keyboard.press(self.information_character['BotaoMana'])  # botão em que a mana esta setada
                sleep(15)
