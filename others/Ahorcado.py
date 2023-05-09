
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabra=0
vocales=  "A" or "E" or "I" or "O" or "U" 

  
def esPalabraValida(palabra):
    contadorVocales=0
    contadorConsonantes=0
    for letra in palabra: 
        if(letra.lower()==vocales):
            contadorVocales+=1
        else:
            contadorConsonantes+=1
    if (len(palabra)-1<7) or contadorVocales>contadorConsonantes or palabra[0]==vocales:
            print("La palabra secreta no es válida ")
            return False
    else:
        return True

        
def imprimirBienvenida(palabra):
    underscore="Palabra: "
    print (" ","\n","\n","\n","\n","\n","\n","\n","\n","\n")
    print("--------------------------------","\nBienvenid@ al Ahorcado 3000Plus","\n--------------------------------")  
    for i in palabra:
        underscore=underscore + "_ "   
    print (underscore)

def revelarPalabra(palabraSecreta): 
    acumulador = ""
    for l in palabraSecreta:
        acumulador = acumulador+ l +" "
    print(f"Palabra Secreta: {acumulador}")

def aplicarReglas(palabra):
    errores= 0
    exitos = 0  
    lenAhorcado = len(AHORCADO)
    letra= ""
    underscore=""

    for i in palabra:
        underscore=underscore + "_"
    
    print(f"Usted tiene {len(AHORCADO)} posibles intentos")  
    while(lenAhorcado>0 and exitos < len(palabra)):
        if exitos != len(palabra):
            letra = input("Ingresa una letra para continuar con el juego: \n")
            if letra in palabra:
                print ("Letra buena, errores: "+str(errores), ", intentos restantes: "+str(lenAhorcado))
                count = 0
                for i in range (0,len(palabra), 1):
                    if letra == palabra[i]:
                        count = i+1
                        exitos +=1
                        underscore = underscore[:i] + letra + underscore[count:]

                revelarPalabra(underscore)
            else: 
                lenAhorcado -=1
                errores+= 1
                print(AHORCADO[errores-1])
                revelarPalabra(underscore)
                print ("Letra mala se le ha disminuido un intento, errores: "+str(errores), ", intentos restantes: "+str(lenAhorcado))
    if exitos == len(palabra):
        return True
    elif lenAhorcado == 0: 
        return False

def inicarJuego():
    palabra= ""
    palabra=input("Ingrese la palabra: \n")
    is_valid= esPalabraValida(palabra)
    imprimir= "Palabra: "
    
    while(is_valid==False):
        palabra=input("Ingrese la palabra: \n")
        is_valid= esPalabraValida(palabra)

    if is_valid:
        imprimirBienvenida(palabra) 
        if aplicarReglas(palabra) == True: 
            print("Felicidades ha ganado el juego")
        else: 
            print("Lo siento ha perdido el juego")
    else: 
        print("Ingrese una palabra que cumpla con los requerimientos\n")
        palabra=input("Ingrese la palabra: \n")
    
inicarJuego()

