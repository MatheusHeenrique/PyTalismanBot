from tools.Ataque import Ataque
from tools.Menu import Menu
from threading import Thread


menu = Menu()
menu_information = menu.get_info()
spell_list = list()
while True:
    if 'spell' in menu_information:
        spell_list.append(menu_information['spell'])
        menu.remove_from_dictionary('spell')
        menu_information.pop('spell')

    # configurando
    talisman = Ataque(menu_information)

    #menu
    exec_menu = Thread(target=menu.principal)
    exec_menu.start()

    # attack
    while True:
        if menu.get_info() != menu_information:
            menu_information = menu.get_info()
            break

        # Cura
        talisman.curar()

        # Magia
        if spell_list:
            for spell in spell_list:
                talisman.usar_magia(spell[0], spell[1], spell[2])

        # Ataque
        talisman.atacar()
