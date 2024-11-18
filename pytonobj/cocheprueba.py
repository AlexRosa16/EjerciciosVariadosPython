class Cotxe2:
    def __init__(self, matricula, marca, model, anyo, combustible):
        self.__matricula = ""
        self.__marca = ""
        self.__model = ""
        self.__anyo = 0
        self.__combustible = ''
        self.set_matricula(matricula)
        self.set_marca(marca)
        self.set_model(model)
        self.set_anyo(anyo)
        self.set_combustible(combustible)
        self.classificacioEcologica()

    def get_matricula(self):
        return self.__matricula

    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_any(self):
        return self.__anyo

    def get_combustible(self):
        if self.__combustible == "D":
            return "Diesel"
        elif self.__combustible == "G":
            return "Gasolina"
        elif self.__combustible == "E":
            return "Electric"
        else:
            return ""

    def set_matricula(self, nueva):
        validas = "BCDFGHJKLMNÑPQRSTVWXYZ"
        decimales = "1234567890"
        if type(nueva) != str:
            raise Exception("La matricula debe ser una cadena")
        if nueva[0] not in validas or nueva[1] not in validas or nueva[2] not in validas:
            raise Exception("Los tres primeros caracteres deben ser consonantes mayusculas")
        if nueva[3] not in decimales or nueva[4] not in decimales or nueva[5] not in decimales or nueva[
            6] not in decimales:
            raise Exception("Los ultimos 4 caracteres deben ser numeros")
        if len(nueva) != 7:
            raise Exception("La matricula debe tener una longitud de 7 caracteres")
        self.__matricula = nueva

    def set_marca(self, marca):
        if type(marca) != str:
            raise Exception("La marca debe ser una cadena")
        self.__marca = marca

    def set_model(self, model):
        if type(model) != str:
            raise Exception("El model debe ser una cadena")
        self.__model = model

    def set_anyo(self, anyo):
        if type(anyo) != int:
            raise Exception("El anyo debe ser un número")
        if not (1900 <= anyo <= 2100):
            raise Exception("El año debe estar entre 1900 y 2100")
        self.__anyo = anyo

    def set_combustible(self, combustible):
        if type(combustible) != str:
            raise Exception("El combustible debe ser una cadena")
        if combustible not in ["D", "G", "E"]:
            raise Exception("Ese tipo de combustible no se permite")
        self.__combustible = combustible

    def classificacioEcologica(self):
        TipoCombustible = ""
        if self.__combustible == "E":
            TipoCombustible = "A"
        elif self.__combustible == "G" and self.__anyo > 2015:
            TipoCombustible = "B"
        elif self.__combustible == "D" and self.__anyo > 2017:
            TipoCombustible = "B"
        elif self.__combustible == "D":
            TipoCombustible = "C"
        return TipoCombustible

    def __str__(self):
        return self.__matricula + "`" + self.__marca + "`" + self.__model + "`" + str(
            self.__anyo) + "`" + self.get_combustible() + "-" + self.classificacioEcologica()


if __name__ == "__main__":
    prueba = Cotxe2("BGF1234", "Ford", "Focus", 2000, "D")
    print(prueba)
