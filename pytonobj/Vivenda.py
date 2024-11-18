from estancia import *


class Vivenda:
    def __init__(self, nomVivenda, MaximVivendas):
        self.__Estancies = []
        self.__nomVivenda = ""
        self.__MaximVivendas = 0
        self.set_nomVivienda(nomVivenda)
        self.set_MaximVivendas(MaximVivendas)

    def get_nomVivienda(self):
        return self.__nomVivenda

    def get_MaxViviendas(self):
        return self.__MaximVivendas

    def set_nomVivienda(self, nomVivienda):
        if type(nomVivienda) != str:
            raise Exception("El nombre de la Vivienda debe ser un string")
        if len(nomVivienda) > 20:
            raise Exception("El nombre de la vivienda no debe sobrepasar de 20 caracteres")
        self.__nomVivenda = nomVivienda

    def set_MaximVivendas(self, MaximVivendas):
        if type(MaximVivendas) != int:
            raise Exception("El maximo de viviendas debe ser un integer")
        if 4 > MaximVivendas < 20:
            raise Exception("El maximo de viviendas debe sobrepasar de 4 y no ser mas que 20")
        self.__MaximVivendas = MaximVivendas

    def afegir_Estancia(self, TipoEstancia, M2, Tefinestres):
        if self.__MaximVivendas == len(self.__Estancies):
            raise Exception("No puedes afegir mas estancias")
        self.__Estancies.append(Estancia(TipoEstancia, M2, Tefinestres))
        print("Agregada con exito")

    def Llevar(self, posicion):
        if posicion > len(self.__Estancies):
            raise Exception("Esa posicion no existe en la lista de estancias")
        self.__Estancies.pop(posicion)

    def Resum(self):
        num_habitacio = 0
        num_menjador = 0
        num_cuina = 0
        num_bany = 0
        m2_total = 0
        te_finestres_exterior = False

        for estancia in self.__Estancies:
            if estancia.get_TipoEstancia() == "Habitacio":
                num_habitacio += 1
            elif estancia.get_TipoEstancia() == "Menjador":
                num_menjador += 1
            elif estancia.get_TipoEstancia() == "Cuina":
                num_cuina += 1
            elif estancia.get_TipoEstancia() == "Bany":
                num_bany += 1
            if estancia.get_Tefinistres() == "amb finestres":
                te_finestres_exterior = True

            m2_total += estancia.get_M2()

        print("Resum Vivienda:")
        print("Habitacio: " + str(num_habitacio))
        print("Menjador: " + str(num_menjador))
        print("Cuina: " + str(num_cuina))
        print("Bany: " + str(num_bany))
        print("Metres Cuadrados: " + str(m2_total))
        print("Finistres al Exterior: " + str(te_finestres_exterior))

        if num_habitacio == 0 or num_menjador == 0 or num_cuina == 0 or num_bany == 0 or m2_total < 50 or not te_finestres_exterior:
            print("La vivienda no es legal per:")
            if num_habitacio == 0:
                print("- No té cap habitació.")
            if num_menjador == 0:
                print("- No té cap menjador.")
            if num_cuina == 0:
                print("- No té cap cuina.")
            if num_bany == 0:
                print("- No té cap bany.")
            if m2_total < 50:
                print("- Té menys de 50 metres quadrats.")
            if te_finestres_exterior == False:
                print("- No té cap finestra a l’exterior.")

    def Mostrar(self):
        for estancia in self.__Estancies:
            estancia.Mostrar()


if __name__ == "__main__":
    prueba = Vivenda("Alex",15)
    prueba.afegir_Estancia("H",11,True)
    prueba.Mostrar()
    prueba.Resum()
