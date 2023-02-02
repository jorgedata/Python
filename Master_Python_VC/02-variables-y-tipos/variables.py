"""
Una variable es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato
distinto
"""

# crear variables y asignarles un valor

texto = "Master en python"
numero = 45
decimal = 6.7

# Mostrar varibles
print(texto)
print(numero)
print(decimal)
print("----------------------------")

# Sustituir el valor de algunas varibles / reasignando valores
numero = 77
decimal = 5.5

print(texto)
print(numero)
print(decimal)
print("----------------------------")

# Concatencion

nombre = "jorge"
apellidos = "Flores"
web = "jorgeflores.com.ar"

print(nombre + " "+ apellidos +" "+ web )
print(f"{nombre} - {apellidos} - {web}")
print("hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))














