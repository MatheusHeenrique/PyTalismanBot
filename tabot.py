from tools import Talisman, Ataque
from pyautogui import press, moveTo, click
from time import sleep, time
from math import trunc


def autopick(Pos=[515, 418], Pulo=55):
    for x in range(417, 623, Pulo):
        for y in range(311, 485, Pulo):
            click(x=x, y=y, button='right')
    moveTo(x=Pos[0], y=Pos[1])
    click()


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
    config('f', Vida=1300, Mana=1300, BotaoMana=9, BotaoCura=6, FayV=4000)

    # selecionando inimigo
    while True:
        press('tab')
        EnimigoSelect = talisman.get_info('se')
        if EnimigoSelect >= 1:
            break

    TempoInicio = time()
    # atacando
    while True:
        ataque.Atacar(2)  # selecione o ataque
        VidaEnimigo = talisman.get_info('ve')

        # verificando se o bot esta muito tempo parado
        TempoFinal = time()
        Minutos = trunc(TempoFinal - TempoInicio)

        if Minutos > 60:
            break

        if VidaEnimigo == 0:
            break

    autopick()
