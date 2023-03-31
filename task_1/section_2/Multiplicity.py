
num = input("Introduzca un número: ")
digitos = list(num)
digitos.sort(reverse=True)
num_ordenado = "".join(digitos)
num_ordenado = int(num_ordenado)
if num_ordenado % 5 == 0:
    print(f"El número {num} ordenado es {num_ordenado} y es un múltiplo de 5")
else:
    print(f"No se pudo ordenar el número {num} de forma tal que sea un múltiplo de 5")
