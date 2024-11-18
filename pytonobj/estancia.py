class Estancia:

    def __init__(self, TipoEstancia, M2, Tefinistres):
        self.__TipoEstancia = ""
        self.__M2 = 0
        self.__Tefinistres = False
        self.set_TipoEstancia(TipoEstancia)
        self.set_M2(M2)
        self.set_Tefinistres(Tefinistres)

    def get_TipoEstancia(self):
        Transformador = ""
        if self.__TipoEstancia == "M":
            Transformador = "Menjador"
        elif self.__TipoEstancia == "H":
            Transformador = "Habitacio"
        elif self.__TipoEstancia == "C":
            Transformador = "Cuina"
        elif self.__TipoEstancia == "B":
            Transformador = "Bany"

        return Transformador

    def get_M2(self):
        return self.__M2

    def get_Tefinistres(self):
        finistres = ""
        if self.__Tefinistres == True:
            finistres = "amb finestres"
        else:
            finistres = "sense finestres"
        return finistres

    def set_TipoEstancia(self, TipoEstancia):
        if type(TipoEstancia) != str:
            raise Exception("El tipo de estancia debe ser una cadena")
        if TipoEstancia not in "MHCB":
            raise Exception("No se permite ese tipo de estancia")
        self.__TipoEstancia = TipoEstancia

    def set_M2(self, M2):
        if type(M2) != int:
            raise Exception("Los m2 deben ser un integer")
        elif 5 > M2 > 50:
            raise Exception("Los metros cuadrados no deben ser menores de 5 ni sobrepasar los 50")
        elif self.__TipoEstancia == "M" and M2 < 15:
            raise Exception("No puedes elegir un menjador de menos de 15 metros cuadrados")
        elif self.__TipoEstancia == "B" and M2 < 5:
            raise Exception("No puedes elegir un baño de menos de 5 metros cuadrados")
        elif self.__TipoEstancia == "H" and M2 < 10:
            raise Exception("No puedes elegir una habitacion de menos de 10 metros cuadrados")
        self.__M2 = M2

    def set_Tefinistres(self, Tefinistres):
        if type(Tefinistres) != bool:
            raise Exception("El valor de las finistres debe ser un boolean")
        self.__Tefinistres = Tefinistres

    def Mostrar(self):
        print("TIpo de Estancia: " + self.get_TipoEstancia() + "\nM2: " + str(self.get_M2()) + "\nTe Finestres: " + str(
            self.get_Tefinistres()))

if __name__ == "__main__":
    prueba = Estancia("H",11,False)
    prueba.Mostrar()

