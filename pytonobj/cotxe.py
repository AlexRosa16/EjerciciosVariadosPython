class Cotxe:
    def __init__(self, num_matricula, marca, model, anyo, combustible):
        self.__matricula = ""
        self.__marca = ""
        self.__model = ""
        self.__any = 0
        self.__combustible = ''
        self.set_matricula(num_matricula)
        self.set_marca(marca)
        self.set_model(model)
        self.set_any(anyo)
        self.set_combustible(combustible)

    def get_matricula(self):
        return self.__matricula

    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_any(self):
        return self.__any

    def get_combustible(self):
        if self.__combustible == 'D':
            return "Diesel"
        elif self.__combustible == 'G':
            return "Gasolina"
        elif self.__combustible == 'E':
            return "Electric"

    def set_matricula(self, nueva):
        validas = "BCDFGHJKLMNÑPQRSTVWXYZ"
        decimales = "1234567890"
        if type(nueva) != str:
            raise Exception("El valor debe de ser una cadena")
        if nueva[0] not in validas or nueva[1] not in validas or nueva[2] not in validas:
            raise Exception("Las letras no són válidas")
        if len(nueva) != 7:
            raise Exception("La longitud de la matrícula introducida no es correcta")
        for x in range(3, 7):  # Podría haber buscado como empezar un for each desde un index especifico
            if not nueva[x] in decimales:
                raise Exception("Valores no decimales")
        self.__matricula = nueva

    def set_marca(self, nueva):
        if type(nueva) != str:
            raise Exception("El valor debe de ser una cadena")
        self.__marca = nueva

    def set_model(self, nueva):
        if type(nueva) != str:
            raise Exception("El valor debe de ser una cadena")
        self.__model = nueva

    def set_any(self, nueva):
        if type(nueva) != int:
            raise Exception("El valor debe de ser un entero")
        if 1900 <= nueva <= 2100:
            self.__any = nueva
        else:
            raise Exception("Año no válido")

    def set_combustible(self, nueva):
        if type(nueva) != str:
            raise Exception("El valor debe de ser una cadena")
        if len(nueva) != 1:
            raise Exception("La cadena sólo puede tener un caracter")
        if nueva not in ['D', 'G', 'E']:
            raise Exception("El caracter no és válido")
        self.__combustible = nueva

    def classificacio_ecologica(self):
        if self.__combustible == 'D':
            if self.__any >= 2017:
                return "B"
            else:
                return "C"
        elif self.__combustible == 'G':
            if self.__any >= 2015:
                return "B"
            else:
                return "C"
        elif self.__combustible == 'E':
            return "A"

    def __str__(self):
        return self.__matricula + "`" + self.__marca + "`" + self.__model + "`" + str(
            self.__any) + "`" + self.get_combustible() + "-" + self.classificacio_ecologica()


if __name__ == "__main__":
    prueba = Cotxe("BGF1234", "Ford", "Focus", 2000, "D")
    print(prueba)
