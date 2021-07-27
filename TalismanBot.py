from tools.Ataque import Talisman

Personagem = {'Classe': 'fairy', 'Ataque': 2, 'Vida': 4300, 'Mana': 3200,
              'BotaoCura': 6, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': 12000}

talisman = Talisman(Personagem)
while True:
    talisman.Curar()
    talisman.UsarMagia(8, 1)
    talisman.Atacar()

