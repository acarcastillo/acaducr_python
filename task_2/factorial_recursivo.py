from termcolor import colored

def factorial(n):
    # Validar si el número es un entero positivo
    if not isinstance(n, int) or n < 0:
        raise ValueError('El número debe ser un entero positivo')
    # Caso base: si n es 0 o 1, retornar 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: multiplicar n por el factorial de n-1
    return n * factorial(n-1)

def call_function(): 
    numero = input("Digite un numero para calcular el factorial: \n")
    print(colored(f"El resultado del facorial es: {factorial(int(numero))}",'green'))

call_function()