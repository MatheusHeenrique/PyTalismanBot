from tools.Ataque import Ataque
from tools.Menu import Menu
from threading import Thread
from time import sleep


def ataque(info=dict(), magias=[]):
    personagem = info
    talisman = Ataque(personagem)

    while True:
        # Cura
        talisman.curar()

        # Magia
        if magias:
            for magia in magias:
                talisman.usar_magia(magia[0], magia[1], magia[2])

        #Ataque
        talisman.atacar()
        if para_ataque:
            break


menu = Menu()
contador = 0
lista_magias = []
while True:
    if contador == 0:
        para_ataque = False
        argumento = menu.get_info()
        Thread(target=ataque, args=(argumento, lista_magias)).start()

    resposta_menu = menu.principal()
    para_ataque = True
    sleep(3)

    para_ataque = False
    if type(resposta_menu) == type(list()):
        lista_magias.append(resposta_menu)
        Thread(target=ataque, args=(argumento, lista_magias)).start()
    else:
        Thread(target=ataque, args=(argumento, lista_magias)).start()

    contador += 1


    # talisman.curar()
    # talisman.usar_magia(8, 1, True)
    # talisman.usar_magia(7, 5, True)
    # talisman.atacar()
