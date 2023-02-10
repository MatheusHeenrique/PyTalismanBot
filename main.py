from tools.Ataque import Ataque

# fairy
personagem = {'Classe': 'fairy', 'Ataque': [2, 1, 'l'], 'Vida': None, 'Mana': None,
              'BotaoCura': 6, 'BotaoMana': 9, 'Wizard': None, 'VidaFairy': None}

talisman = Ataque(personagem)


while True:
    talisman.curar()
    talisman.usar_magia(8, 1, True)
    talisman.usar_magia(7, 5, True)
    talisman.atacar()
