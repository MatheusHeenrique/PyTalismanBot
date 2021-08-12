from tools.ataque import Talisman

# fairy
personagem = {'Classe': 'fairy', 'Ataque': 2, 'Vida': 5000, 'Mana': 4000,
              'BotaoCura': 6, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': 12000}

talisman = Talisman(personagem)
while True:
    # talisman.fairy_curar((6, 7))
    talisman.curar()
    talisman.usar_magia(8, 1)
    talisman.atacar()
