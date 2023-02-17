from tools.attack_manager import AttackManager
from tools.menu import Menu
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
    talisman = AttackManager(menu_information)

    #menu
    exec_menu = Thread(target=menu.main_menu)
    exec_menu.start()

    # attack
    while True:
        if menu.get_info() != menu_information:
            menu_information = menu.get_info()
            break

        # Cura
        talisman.heal()

        # Magia
        if spell_list:
            for spell in spell_list:
                talisman.use_magic(spell[0], spell[1], spell[2])

        # Ataque
        talisman.to_attack()
