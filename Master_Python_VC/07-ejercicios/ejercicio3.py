"""
Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales.
resolverlo con fo y con while
"""

contador = 0
while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador +=1