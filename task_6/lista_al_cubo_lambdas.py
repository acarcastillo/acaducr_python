import random

# Solicitar al usuario que ingrese la longitud de la lista
longitud = int(input("Ingrese la longitud de la lista de números aleatorios: "))

# Crear una lista de números aleatorios
numeros = []
for _ in range(longitud):
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

###########################################################
#MISMO EJEMPLO ANTERIOR PERO USANDO LAMBDAS:
# Solicitar al usuario que ingrese la longitud de la lista
# Crear una lista de números aleatorios utilizando comprensión de listas
numeros = [random.randint(1, 20) for _ in range(int(input("Ingrese la longitud de la lista de números aleatorios: ")))]
# Imprimir la lista original
print("La lista de números aleatorios es:", numeros)
# Crear una nueva lista con los cubos de los números de la lista original utilizando lambdas y comprensión de listas
cubos = [(lambda x: x ** 3)(numero) for numero in numeros]
# Imprimir la lista de cubos
print("La lista de cubos es:", cubos)
