from funciones import sumar, restar, multiplicar, dividir, factorial, potencia
from utils import log_binacle
import datetime

def iniciar():
    opciones_aritmeticas= ["sumar", "restar","multiplicar", "dividir", "factorial","potencia"]
    operaciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir,
        "factorial": factorial,
        "potencia": potencia
    }

    opciones_validas = ["y", "n"]
    opcion_elegida =""
    while opcion_elegida not in opciones_validas:
        opcion_elegida = input("¿Quieres iniciar la rutina de la calculadora? (y/n):")
        if opcion_elegida not in opciones_validas:
            print("Opción no válida, por favor intenta de nuevo.")
        else:
            elegir_operacion(opciones_aritmeticas, operaciones)


def elegir_operacion(opciones_aritmeticas, operaciones):
    continuar = True
    opciones_validas = ["y", "n"]
    # Obtener la hora actual
    hora_actual = datetime.datetime.now()
    while continuar: 
        opcion_elegida = ""
        while opcion_elegida not in opciones_aritmeticas:
            print("Elige una de las siguientes opciones: ")
            for opcion in opciones_aritmeticas:
                print("-", opcion)
            opcion_elegida = input("Opción elegida: ")
            if opcion_elegida not in opciones_aritmeticas:
                print("Opción no válida, por favor intenta de nuevo.")

        resultado = operaciones[opcion_elegida]()
        print_result= f"El resultado de la función {opcion_elegida} es: {resultado}"
        print(print_result)
        log_binacle(print_result)

        respuesta = input("¿Deseas continuar realizando calculos? (y/n): ")

        while respuesta.lower() not in opciones_validas:
            respuesta = input("Respuesta no válida. ¿Deseas continuar realizando calculos? (y/n): ")
        if respuesta.lower()== "n": 
            continuar = False
            print("Gracias por usar nuestro sistema de operaciones aritmeticas")

iniciar()