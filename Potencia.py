from typing import List


class Potencia:

    def __init__(self,valor):
        self.cadena=valor
        self.a=0
        self.b=0
        self.c=0
        
    def RecorrerCadena(self):
            self.a=int(self.cadena[0])
            self.b=int(self.cadena[1])
            self.c=int(str(self.cadena)[-1])

