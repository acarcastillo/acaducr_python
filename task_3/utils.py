import datetime
"""
Este método recibe un mensaje como entrada para solicitar al usuario que ingrese 
un número. Luego, intenta convertir la entrada del usuario en un número de punto 
flotante (float). Si la conversión es exitosa, devuelve el número ingresado. Si 
hay una excepción de valor (ValueError), se muestra un mensaje de error al usuario 
y se llama al método validar_numero() recursivamente para que el usuario ingrese un 
número válido
"""
def validar_numero(mensaje):
    numero_str = input(mensaje)
    try:
        numero = float(numero_str)
        return numero
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return validar_numero(mensaje)

"""
Este método recibe una cadena de texto como entrada (log), que se escribirá en un
archivo de registro llamado "log.txt". Primero, obtiene la hora actual usando la 
biblioteca datetime. Luego, abre el archivo en modo "append" y escribe la hora actual
seguida del texto de registro proporcionado por el usuario. El método se encarga 
de agregar una nueva línea al final del registro.
"""
def log_binacle(log): 
    # Obtener la hora actual
    hora_actual = datetime.datetime.now()

    # Abrir el archivo en modo "append"
    with open("log.txt", "a") as archivo:
        # Escribir la hora actual en el archivo
        archivo.write(str(hora_actual) +" "+log+ "\n")