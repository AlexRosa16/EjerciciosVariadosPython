from cocheprueba import *


class Garatxe:
    def __init__(self, descripcio, capacitat, electrics):
        self.__descripcio = ""
        self.__capacitat = 0
        self.__electrics = 0
        self.cotxes = []
        self.set_descripcio(descripcio)
        self.set_capacitat(capacitat)
        self.set_electrics(electrics)

    def get_descripcion(self):
        return self.__descripcio

    def get_capacitat(self):
        return self.__capacitat

    def get_electrics(self):
        return self.__electrics

    def set_descripcio(self, descripcio):
        if type(descripcio) != str:
            raise Exception("La descripcion debe ser string")
        if len(descripcio) > 40:
            raise Exception("La descripcion no debe superar los 40 caracteres")
        self.__descripcio = descripcio

    def set_capacitat(self, capacitat):
        if type(capacitat) != int:
            raise Exception("La capacitat debe ser entero")
        if capacitat < 5:
            raise Exception("La capacidad debe ser positiva y mayor de 5")
        self.__capacitat = capacitat

    def set_electrics(self, electrics):
        if electrics < len(self.cotxes):
            raise Exception("Los cotxes electricos no deberian mas que la capacidad que el garatxe")
        if type(electrics) != int:
            raise Exception("Electrics debe ser un entero")
        self.__electrics = electrics

    def afegir_cotxe(self, matricula, model, marca, anyo, combustible):
        if len(self.cotxes) > self.__capacitat:
            raise Exception("No se pueden meter mas coches")
        self.cotxes.append(Cotxe2(matricula, model, marca, anyo, combustible))

    def traure_cotxe_num(self, posicion):
        self.cotxes.pop(posicion)

    def traure_cotxe_matricula(self, matricula):
        for coche in self.cotxes:
            if coche.get_matricula() == matricula:
                self.cotxes.remove(coche)
                break

    def resum(self):
        print("Descripcion: " + self.__descripcio + "Capacitat: " + str(self.__capacitat) + "Electrics: " + str(self.__electrics))
        for x in self.cotxes:
            print(x)

    def estadistica(self):
        print("Garatge: " + self.__descripcio + "\nCapacitat: " + str(
            self.__capacitat) + "\nElectrics: " +str(self.__electrics) + "\nCotxes al garatge: ")
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        for x in self.cotxes:
            if x.get_combustible() == "Diesel":
                a += 1
            elif x.get_combustible() == "Gasolina":
                b += 1
            elif x.get_combustible() == "Electric":
                c += 1
            if x.classificacioEcologica() == "A":
                d += 1
            elif x.classificacioEcologica() == "B":
                e += 1
            elif x.classificacioEcologica() == "C":
                f += 1

        print("Per combustible: " + "\nDiesel: " + str(a) + "\nGasolina: " + str(b) + "\nElectrics: " + str(
            c) + "\nPer classificació ecològica: " + "\nA: " + str(d) + "\nB: " + str(e) + "\nC: " + str(f))


if __name__ == "__main__":
    prueba = Garatxe("Calle Colón, 19 València", 120, 5)
    prueba.afegir_cotxe("BGF1234", "Ford", "Focus", 2000, "D")
    prueba.afegir_cotxe("PYR2345", "Pegaso", "Valiente", 2099, "E")
    prueba.afegir_cotxe("BFG9000", "Rayo Veloz", "Olvidona", 1984, "G")
    prueba.resum()
    print()
    prueba.estadistica()


