from tools.Ataque import Talisman

# fairy
# Personagem = {'Classe': 'fairy', 'Ataque': 2, 'Vida': 5000, 'Mana': 4000,
#               'BotaoCura': 6, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': 12000}

# tamer
Personagem = {'Classe': 'tamer', 'Ataque': [1, 2, 'u'], 'Vida': 85, 'Mana': 85,
              'BotaoCura': 8, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': None}

talisman = Talisman(Personagem)
while True:
    # talisman.FairyCurar((6, 7))
    talisman.Curar()
    # talisman.UsarMagia(8, 1)
    talisman.Atacar()
