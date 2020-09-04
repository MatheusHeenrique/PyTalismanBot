from tools import Talisman, Ataque
from pyautogui import press
from time import sleep


def config(clase_personagem, Vida, Mana=None, BotaoCura=None, BotaoMana=None, FayV=3200):
    # cura
    if talisman.get_info('v') < Vida:

        if clase_personagem == 'f':
            press('f1')
            while talisman.get_info('v') < FayV:
                press(str(BotaoCura))
                sleep(1.6)
        else:
            sleep(4)
            press(str(BotaoCura))  # botão em que a vida esta setada
            sleep(15)

    # mana
    if BotaoMana is not None:
        if talisman.get_info('m') < Mana:
            sleep(4)
            press(str(BotaoMana))  # botão em que a mana esta setada
            sleep(15)


talisman = Talisman()
ataque = Ataque('s')

sleep(3)

while True:
    # selecionando a classe
    config('s', Vida=100, BotaoCura=0)


    # selecionando inimigo
    while True:
        press('tab')
        EnimigoSelect = talisman.get_info('se')
        if EnimigoSelect >= 1:
            break

    # atacando
    while True:
        ataque.Atacar(3)  # selecione o ataque
        VidaEnimigo = talisman.get_info('ve')

        if VidaEnimigo == 0:
            break
