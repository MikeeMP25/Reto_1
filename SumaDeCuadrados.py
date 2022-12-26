from Potencia import Potencia

class SumaDeCuadrados(Potencia):

    def __init__(self, valor):
        super().__init__(valor)

    def CalcularCuadrados(self):
        a=0
        resultado=0
        for valor in recorrido():
            a=valor
            a=a*a
            resultado+=a
        #resultado=(self.a*self.a)+(self.b*self.b)+(self.c*self.c)
        return resultado      
