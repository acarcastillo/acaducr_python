import re 

def count_special_characters(string_input):
    pattern_special_characters = r'[!@#$%^&*()_+\-=[\]{}|;":<>,./?\\]'
    count_special_characters = len(re.findall(pattern_special_characters, string_input))
    print(f"La cantidad de caracteres especiales en la cadena es: {count_special_characters}")

    pattern_numbers = r'\d'
    count_numbers = len(re.findall(pattern_numbers, string_input))
    print(f"La cantidad de números en la cadena es: {count_numbers}")

    pattern_strings = r'[a-zA-Z]'
    count_strings = len(re.findall(pattern_strings, cadena))
    print(f"La cantidad de letras en la cadena es: {count_strings}")
    print("\n__________________________________________________________________________")


def count_characters(string_input):
    characters = {}
    for character in string_input:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    print(characters)  
    print("\n__________________________________________________________________________")

def delete_element(list, element):
    print("Lista original: ",list )
    while element in list:
        list.remove(element)
    print(list)
    print("\n__________________________________________________________________________")

def print_list_and_tuple():
    secuencia = input("Ingrese una secuencia de números separados por coma: ")
    lista = []
    tupla = ()
    if secuencia: 
        elementos = secuencia.split(",") 
        for elemento in elementos:
            elemento = elemento.strip() 
            if elemento:
                try:
                    numero = elemento
                    lista.append(numero)
                    tupla += (numero,)
                except ValueError:
                    print(f"El elemento '{elemento}' no es un número válido y será ignorado.")
            else:
                print("Se ha ingresado un elemento vacío y será ignorado.")
    else:
        print("No se ingresó ninguna secuencia.")
    if lista:
        print("Lista resultante:", lista)
    else:
        print("La lista resultante está vacía.")
    if tupla:
        print("Tupla resultante:", tupla)
    else:
        print("La tupla resultante está vacía.")
    print("\n__________________________________________________________________________")
    

cadena = "P@#yn26at^&i5ve"
count_special_characters(cadena)    

cadena= "papaya"
count_characters(cadena)

list = [20, 30, 40, 20, 5, 100, 5, 20]
element = 20
delete_element(list, element)

list= ["perro", "gato", "sombrero", "gato", "zanahoria"]
element= "gato"
delete_element(list, element)

print_list_and_tuple()

