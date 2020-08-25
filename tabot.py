from tools import Talisman
from pyautogui import press
from time import sleep


def curar(classe=None, bCura=None):
    if classe == 'f':
        press('f1')
        while talisman.get_info('v') < 3200:
            press(str(bCura))
            sleep(1.6)
    else:
        sleep(4)
        press(str(bCura))  # botão em que a vida esta setada
        sleep(15)


def mana(bMana=None):
    sleep(4)
    press(str(bMana))  # botão em que a mana esta setada
    sleep(15)


def per(clase_personagem, Vida, Mana=None, BotaoCura=None, BotaoMana=None):

    # fairy
    if clase_personagem == 'f':
        if talisman.get_info('v') < Vida:
            curar('f', BotaoCura)
        if talisman.get_info('m') < Mana:  # vai usar a mana
            mana(BotaoMana)

    # assasin e monk
    elif clase_personagem == 's':
        if talisman.get_info('v') < Vida:  # vai curar quando estiver com 150 de vida
            curar(bCura=BotaoCura)

    # tamer e wiz
    elif clase_personagem == 't' or clase_personagem == 'w':
        if talisman.get_info('v') < Vida:
            curar(bCura=BotaoCura)
        if talisman.get_info('m') < Mana:
            mana(BotaoMana)


def atacar(num_ataque, tempo=None):
    # selecionando inimigo
    while True:
        press('tab')
        enimigo_sel = talisman.get_info('se')
        if enimigo_sel >= 1:
            break

    # atacando
    i = 0
    while True:
        if i == len(num_ataque):
            i = 0

        press(str(num_ataque[i]))

        if i < len(num_ataque):
            i += 1

        vida_eni = talisman.get_info('ve')
        if vida_eni == 0:
            break
        else:
            if tempo is not None:
                if i == 0:
                    sleep(tempo[0])
                else:
                    sleep(tempo[1])
            else:
                sleep(1.6)


talisman = Talisman()
sleep(3)

while True:
    # selecionando a classe
    per('w', Vida=200, Mana=250, BotaoCura=9, BotaoMana=8)

    # atacando
    atacar([2, 1], tempo=[2.6, 1.6])
