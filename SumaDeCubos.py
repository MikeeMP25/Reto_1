from Potencia import Potencia


class SumaDeCubos(Potencia):

    def __init__(self, valor):
        super().__init__(valor)
    
    def CalcularCubos(self):
      respuesta=(self.a*self.a*self.a)+(self.b*self.b*self.b)+(self.c*self.c*self.c)
      return respuesta