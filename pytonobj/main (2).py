from garatge import *
import time

creado_garage = False
texto = "(1) Crear garatge (6) Exir del programa"
garage = None
while True:
    print(texto)
    opcion = int(input())
    if creado_garage and opcion == 1:
        print("Garatget ja creat previament\n")
    elif not creado_garage and opcion == 1:
        garage = Garatge(input("Descripció: "), int(input("Capacitat: ")), int(input("Carregadors elèctrics: ")))
        creado_garage = True
        texto = "(1) Crear garatge\n(2) Afegir cotxe al garatge\n(3) Traure cotxe del garatge\n(4) Mostrar un " \
                "llistat de tots els cotxes que están al garatge\n(5) Mostrar l'estadística de tots els cotxes que " \
                "tenim al garatge\n(6) Exir del programa"
        print("Garatge creat")
    if creado_garage and opcion == 2:
        garage.afegir_cotxe(input("Matricula:"), input("Marca: "), input("Model: "), int(input("Any: ")),
                            input("Combustible [D|G|E]: "))
    if creado_garage and opcion == 3:
        if len(garage.cotxes) == 0:
            raise Exception("No hi ha ningun cotxe al garatge")
        opcion = int(input("Traure per (1) Index o per (2) matrícula"))
        if opcion == 1:
            garage.traure_cotxe_num(int(input(f"Index 0-{len(garage.cotxes)-1}: ")))
        elif opcion == 2:
            garage.traure_cotxe_matricula(input("Matricula: "))
    if creado_garage and opcion == 4:
        garage.resum()
    if creado_garage and opcion == 5:
        garage.estadistica()
    if opcion == 6:
        break
    time.sleep(1.5)


print("Fin del programa.")
