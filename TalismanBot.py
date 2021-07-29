from tools.Ataque import Talisman

Personagem = {'Classe': 'fairy', 'Ataque': 2, 'Vida': 5000, 'Mana': 4000,
              'BotaoCura': 6, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': 12000}

talisman = Talisman(Personagem, 'Giant Sky Medal')
while True:
    # talisman.FairyCurar((6, 7))
    talisman.Curar()
    talisman.UsarMagia(8, 1)
    talisman.Atacar()
