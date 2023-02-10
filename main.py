from tools.Ataque import Ataque
from tools.Menu import Menu

menu = Menu()


while True:
    personagem = menu.get_info()
    talisman = Ataque(personagem)
    # talisman.curar()
    # talisman.usar_magia(8, 1, True)
    # talisman.usar_magia(7, 5, True)
    # talisman.atacar()
