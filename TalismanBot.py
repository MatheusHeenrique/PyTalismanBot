from tools.principal import Talisman


talisman = Talisman('f')
while True:
    # fay config: Vida=3600, Mana=2600, BotaoCura=6, BotaoMana=9, FayV=10000
    talisman.Cura(Vida=4300, Mana=3200, BotaoCura=6, BotaoMana=9, FayV=12000)
    talisman.UsarMagia(8, 1)
    talisman.Atacar(2)
