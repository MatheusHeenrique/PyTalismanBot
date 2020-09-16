from tools import ActionTalisman
from time import sleep

sleep(3)
talisman = ActionTalisman('s')

while True:
    # fay config: Vida=1600, Mana=1550, BotaoCura=6, BotaoMana=9, FayV=4000
    talisman.Cura(Vida=170, BotaoCura=9)
    talisman.UsarMagia(8, 30)
    talisman.Atacar(3)
