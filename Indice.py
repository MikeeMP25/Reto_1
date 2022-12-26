from SumaDeCuadrados import SumaDeCuadrados
from SumaDeCubos import SumaDeCubos


print("Bienvenidos a Reto Python")
when true:
  try{
  cantidad=int(input("Ingresa un numero entero:  "))
  exception e{
    print("No es un nuemero vuelve a intentarlo")
  }
  }
cuadrados=SumaDeCuadrados(cantidad)
cuadrados.RecorrerCadena()
cubos=SumaDeCubos(cantidad)
cubos.RecorrerCadena()
resultadoFinal=cuadrados.CalcularCuadrados()+cubos.CalcularCubos()
print("El resultado es= "+str(resultadoFinal))
