from SumaDeCuadrados import SumaDeCuadrados
from SumaDeCubos import SumaDeCubos

print("Bienvenidos a Reto Python")
cantidad=input("Ingresa la cantidad a calcular  ")
cuadrados=SumaDeCuadrados(cantidad)
cuadrados.RecorrerCadena()
cubos=SumaDeCubos(cantidad)
cubos.RecorrerCadena()
resultadoFinal=cuadrados.CalcularCuadrados()+cubos.CalcularCubos()
print("El resultado es= "+str(resultadoFinal))
