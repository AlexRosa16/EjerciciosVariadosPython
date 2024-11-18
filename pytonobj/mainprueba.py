from garageprueba import Garatxe
import time

creando_garage = False
texto = "(1) Crear garatxe (6) Eixir del programa"
garage = None
while True:
    print(texto)
    opcion = int(input())
    if creando_garage and opcion == 1:
        print("Garage previamente creado")
    elif not creando_garage and opcion == 1:
        garage = Garatxe(input("Descripcio: "), int(input("Capacitat: ")), int(input("Carregadors electrics")))
        creando_garage = True
        texto = "(1) Crear garatge\n(2) Afegir cotxe al garatge\n(3) Traure cotxe del garatge\n(4) Mostrar un " \
                "llistat de tots els cotxes que están al garatge\n(5) Mostrar l'estadística de tots els cotxes que " \
                "tenim al garatge\n(6) Exir del programa"
        print("Garatge creat")
    if creando_garage and opcion == 2:
        garage.afegir_cotxe(input("Matricula: "), input("Marca: "), input("Model"), int(input("Any")),
                            input("Combustible [D|G|E]"))
    if creando_garage and opcion == 3:
        if len(garage.cotxes) == 0:
            raise Exception("No puedes sacar cotxes si no hay")
        tiposalida = int(input("Como quieres sacar coches? (1) Index, (2)Matricula"))
        if tiposalida == 1:
            posicion = int(input("Dime la posicion del coche que quieres sacar"))
            if len(garage.cotxes) - 1 < posicion:
                garage.traure_cotxe_num(posicion)
        elif tiposalida == 2:
            matricula = input("Dime la matricula del coche que quieres sacar")
            garage.traure_cotxe_matricula(matricula)
    if creando_garage and opcion == 4:
        garage.resum()
    if creando_garage and opcion == 5:
        garage.estadistica()
    if creando_garage and opcion == 6:
        break
    time.sleep(1.5)

print("Fin del programa")
