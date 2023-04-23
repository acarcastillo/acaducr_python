import random

# Solicitar al usuario que ingrese la longitud de la lista
longitud = int(input("Ingrese la longitud de la lista de números aleatorios: "))

# Crear una lista de números aleatorios
numeros = []
for i in range(longitud):
    numero = random.randint(1, 20)
    numeros.append(numero)

# Imprimir la lista original
print("La lista de números aleatorios es: ", numeros)

# Crear una nueva lista con los cubos de los números de la lista original
cubos = []
for numero in numeros:
    cubo = numero ** 3
    cubos.append(cubo)

# Imprimir la lista de cubos
print("La lista de cubos es: ", cubos)
