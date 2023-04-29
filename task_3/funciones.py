from utils import validar_numero

"""
Solicita al usuario ingresar una serie de números y devuelve la suma total.
Returns:
float: La suma de los números ingresados por el usuario.
"""

def sumar():
    print("\nInicializando la funcion: sumar \n")
    numeros = []
    continuar = True
    opciones_validas = ["y", "n"]
    while continuar:
        numero = validar_numero("Ingresa un número: ")
        numeros.append(numero)
        respuesta = input("¿Deseas ingresar otro número? (y/n): ")
        
        while respuesta.lower() not in opciones_validas:
            respuesta = input("Respuesta no válida. ¿Deseas ingresar otro número? (y/n): ")
        if respuesta.lower()== "n": 
            continuar = False

        suma = 0
        for numero in numeros:
            suma += numero
    return suma

"""
Solicita al usuario ingresar dos números y devuelve la resta de ellos.

Returns:
float: La resta del primer número menos el segundo número.
"""
def restar():
    print("\nInicializando la funcion: restar \n")
    num1 = validar_numero("Ingresa el primer número: ")
    num2 = validar_numero("Ingresa el segundo número: ")
    resta = num1 - num2
    return resta

"""
Solicita al usuario ingresar una serie de números y devuelve el producto de ellos.

Returns:
float: El producto de los números ingresados por el usuario.
"""
def multiplicar():
    print("\nInicializando la funcion: multiplicar \n")
    numeros = []
    continuar = True
    opciones_validas = ["y", "n"]
    while continuar:
        numero = validar_numero("Ingresa un número: ")
        numeros.append(numero)
        respuesta = input("¿Deseas ingresar otro número? (y/n): ")
        
        while respuesta.lower() not in opciones_validas:
            respuesta = input("Respuesta no válida. ¿Deseas ingresar otro número? (y/n): ")
        if respuesta.lower()== "n": 
            continuar = False

    producto = 1
    for numero in numeros:
        producto *= numero
    return producto

"""
Solicita al usuario ingresar dos números y devuelve el resultado de dividir el primer número por el segundo.

Returns:
float: El resultado de la división del primer número entre el segundo número.

Raises:
TypeError: Si alguno de los argumentos no es numérico.
ValueError: Si el segundo argumento es cero.
"""
def dividir():
    print("\nInicializando la funcion: dividir \n")
    num1 = validar_numero("Ingresa el primer número: ")
    num2 = validar_numero("Ingresa el segundo número: ")

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Ambos argumentos deben ser numéricos")
    if num2 == 0:
        print("El segundo argumento no puede ser cero")
        return dividir()
    resultado = num1 / num2
    return resultado

"""
Solicita al usuario ingresar un número entero positivo y devuelve su factorial.

Returns:
int: El factorial del número ingresado por el usuario.
"""
def factorial():
    print("\nInicializando la funcion: factorial \n")
    resultado = 1
    num = int(validar_numero("Ingresa el número: "))

    if not isinstance(num, int) or num < 0:
        print('El número debe ser un entero positivo')    
        factorial()

    for i in range(1, num + 1):
        resultado *= i
    return resultado


"""
Solicita al usuario ingresar una base y un exponente, y devuelve la 
potencia de la base elevada al exponente.
"""
def potencia():
    print("\nInicializando la funcion: potencia \n")
    base = validar_numero("Ingresa el número base: ")
    exponente = validar_numero("Ingresa el número exponente: ")  
    resultado = base ** exponente
    return resultado


   


