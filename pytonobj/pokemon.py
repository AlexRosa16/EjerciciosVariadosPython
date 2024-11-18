class Pokemon:
    def __init__(self,tipo,nombre):
        self.__tipo = ''
        self.__nombre = ""
        self.__nivell = 0
        self.__atacs = []
        self.set_tipo(tipo)
        self.set_nombre(nombre)
        self.set_nivell(1)
        self.set_atacs()


    def get_tipo(self):
        TipoString = ""
        if self.__tipo == "N":
            TipoString = "Normal"
        elif self.__tipo == "V":
            TipoString = "Volador"
        elif self.__tipo == "F":
            TipoString = "Foc"
        elif self.__tipo == "A":
            TipoString = "Aigua"
        elif self.__tipo == "P":
            TipoString = "Planta"

        return TipoString

    def get_nombre(self):
        return self.__nombre

    def get_nivell(self):
        return self.__nivell

    def get_atacs(self):
        return self.__atacs

    def set_tipo(self,tipo):
        if tipo not in "N" or "V" or "F" or "A" or "P":
            raise Exception("Ese tipo no esta permitido")
        self.__tipo = tipo

    def set_nombre(self,nombre):
        if type(nombre) != str:
            raise Exception("Nombre debe ser una cadena")
        self.__nombre = nombre

    def set_nivell(self,nivell):
        if 0 >= self.__nivell < 10:
            raise Exception("Ese no esta permitido")
        self.__nivell = nivell

    def set_atacs(self):
        Atacs = self.__nivell
        if Atacs == 1:
            self.__atacs.append("Placaje")
        elif Atacs == 2:
            self.__atacs.append("Placaje,Gruñido")
        elif Atacs == 3:
            if self.__tipo == "N":
                self.__atacs.append("Placaje,Gruñido,Persecucion,")
            elif self.__tipo == "V":
                self.__atacs.append("Placaje,Gruñido, Ataque Volador")
            elif self.__tipo == "F":
                self.__atacs.append("Placaje,Gruñido,Ascuas")
            elif self.__tipo == "A":
                self.__atacs.append("Placaje,Gruñido,Burbuja")
            elif self.__tipo == "P":
                self.__atacs.append("Placaje,Gruñido,Latigo Cepa")
        elif Atacs == 4:
            if self.__tipo == "N":
                self.__atacs.append("Placaje,Gruñido,Persecucion,Derribo")
            elif self.__tipo == "V":
                self.__atacs.append("Placaje,Gruñido, Ataque Volador,Ataque Rapido")
            elif self.__tipo == "F":
                self.__atacs.append("Placaje,Gruñido,Ascuas,Nitrocarga")
            elif self.__tipo == "A":
                self.__atacs.append("Placaje,Gruñido,Burbuja,Hidropulso")
            elif self.__tipo == "P":
                self.__atacs.append("Placaje,Gruñido,Latigo Cepa,Absorber")

    def Mostrar_Datos(self):
        print("****************************************************************************")
        print("\nPokemon: " + self.__nombre + "\nTIPUS: " + self.__tipo + "\nNIVELL: " + str(self.__nivell) + "\nATACS: " + str(self.__atacs))
        print("****************************************************************************")

    def ModificarNivel(self):
        opcion = int(input("Elige una opcion: (1)Subir un nivell , (2) Bajar un nivell"))
        if opcion == 1:
            self.__nivell = self.__nivell + 1
            if self.__nivell > 10:
                raise Exception("Has superado el limite de nivel")
        elif opcion == 2:
            self.__nivell = self.__nivell - 1
            if self.__nivell < 1 :
                raise Exception("No puedes bajar a 0 el nivel del pokemon")


