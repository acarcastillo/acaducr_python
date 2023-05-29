cadena1 = input("Ingrese la primera cadena de texto: ")
cadena2 = input("Ingrese la segunda cadena de texto: ")

while len(cadena1) != len(cadena2):
    print("Error: Las cadenas de texto deben tener la misma longitud.")
    cadena1 = input("Ingrese la primera cadena de texto: ")
    cadena2 = input("Ingrese la segunda cadena de texto: ")

nueva_cadena = ""
for i in range(len(cadena1)):
    nueva_cadena += cadena1[i] + cadena2[i]

print("La nueva cadena intercalada es:", nueva_cadena)

###########################################################
#MISMO EJEMPLO ANTERIOR PERO USANDO LAMBDAS:
cadena1 = input("Ingrese la primera cadena de texto: ")
cadena2 = input("Ingrese la segunda cadena de texto: ")

while len(cadena1) != len(cadena2):
    print("Error: Las cadenas de texto deben tener la misma longitud.")
    cadena1 = input("Ingrese la primera cadena de texto: ")
    cadena2 = input("Ingrese la segunda cadena de texto: ")

nueva_cadena_lambda = lambda cadena1, cadena2: ''.join([cadena1[i] + cadena2[i] for i in range(len(cadena1))])


print("La nueva cadena intercalada es:", nueva_cadena_lambda)