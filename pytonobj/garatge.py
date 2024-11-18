from cotxe import *


class Garatge:
    def __init__(self, descripcion, capacidad, electricos):
        self.__descripcio = ""
        self.__capacitat = 0
        self.__electrics = 0
        self.cotxes = []
        self.set_descripcio(descripcion)
        self.set_capacitat(capacidad)
        self.set_electrics(electricos)

    def get_descripcio(self):
        return self.__descripcio

    def get_capacitat(self):
        return self.__capacitat

    def get_electrics(self):
        return self.__electrics

    def set_descripcio(self, nueva):
        if type(nueva) != str:
            raise Exception("El valor debe de ser una cadena")
        if len(nueva) > 40:
            raise Exception("La descripción no debe de superar 40 caracteres")
        self.__descripcio = nueva

    def set_capacitat(self, nueva):
        if type(nueva) != int:
            raise Exception("El valor debe de ser un entero")
        if nueva < 6:
            raise Exception("El valor debe de ser mayor de 5")
        self.__capacitat = nueva

    def set_electrics(self, nueva):
        if type(nueva) != int:
            raise Exception("El valor debe de ser un entero")
        if nueva > self.__capacitat:
            raise Exception("El valor no puede ser mayor que la capacidad del garaje")
        self.__electrics = nueva

    def afegir_cotxe(self, matricula, marca, modelo, anyo, combustible):
        if len(self.cotxes) < self.__capacitat:
            self.cotxes.append(Cotxe(matricula, marca, modelo, anyo, combustible))
        else:
            raise ValueError("El garaje está lleno")

    def traure_cotxe_num(self, posicion):
        self.cotxes.pop(posicion)

    def traure_cotxe_matricula(self, num):
        self.cotxes.remove(num)

    def resum(self):
        print("Garatge: " + self.__descripcio + "\nCapacitat: " + str(
            self.__capacitat) + " espacios\nElèctrics: " + str(self.__electrics) + " espacios\nCotxes al garatge:")
        for x in self.cotxes:
            print(f"\t {x}")

    def estadistica(self):
        print("Garatge: " + self.__descripcio + "\nCapacitat: " + str(
            self.__capacitat) + " espacios\nElèctrics: " + str(self.__electrics) + " espacios\nCotxes al garatge:")
        d = 0
        g = 0
        e = 0

        a = 0
        b = 0
        c = 0
        for x in self.cotxes:
            if x.get_combustible() == "Dièsel":
                d += 1
            elif x.get_combustible() == "Gasolina":
                g += 1
            elif x.get_combustible() == "Elèctric":
                e += 1
            if x.classificacio_ecologica() == 'A':
                a += 1
            elif x.classificacio_ecologica() == 'B':
                b += 1
            elif x.classificacio_ecologica() == 'C':
                c += 1

        print(f"Per combustible:\n\tDièsel: {d}\n\tGasolina: {g}\n\t"
              f"Elèctric: {e}\nPer classificació ecològica:\n\tA: {a}\n\tB: {b}\n\tC: {c}")


if __name__ == "__main__":
    prueba = Garatge("Calle Colón, 19 València", 120, 5)
    prueba.afegir_cotxe("BGF1234", "Ford", "Focus", 2000, "D")
    prueba.afegir_cotxe("PYR2345", "Pegaso", "Valiente", 2099, "E")
    prueba.afegir_cotxe("BFG9000", "Rayo Veloz", "Olvidona", 1984, "G")
    prueba.resum()
    print()
    prueba.estadistica()
