from deck import Deck
from player import Player
import json
from datetime import datetime

# `Juego` es una clase que representa un juego de Blackjack. Tiene métodos para repartir cartas,
# mostrar el estado del juego, permitiendo que el jugador tome turnos, determinando el ganador,
# y escribir datos del juego en un archivo con fines estadísticos. También tiene un método para iniciar
# el juego y permitir que el jugador elija si jugar con un apodo nuevo o existente,
# ver estadísticas recientes del juego o salir del juego.

class Juego:
    temp_carta_jugador = None
    user_id_value= None
    user_nickname= None

    
#Esta función inicia un juego de Blackjack imprimiendo un mensaje de bienvenida, creando una baraja de
#cards, y creando un jugador para el usuario y la casa.
        
    def __init__(self):
        print("\n¡Bienvenido al Blackjack!")
        print()
        print("┌───────────────────────────┐")
        print("│                           │")
        print("│♠ ♥ ♦ ♣ BlackJack ♠ ♥ ♦ ♣  │")
        print("│                           │")
        print("└───────────────────────────┘")   
        self.iniciar()
        print("\nINICIANDO JUEGO DE BLACK JACK!\n")
        self.mazo = Deck()
        self.jugador = Player("Jugador")
        self.casa = Player("Casa")
        
# `repartir_cartas_iniciales` es un método que reparte dos cartas tanto al jugador como al
# casa al comienzo del juego.
    def repartir_cartas_iniciales(self):
        for _ in range(2):
            self.jugador.recibir_carta(self.mazo.sacar_carta())
            self.casa.recibir_carta(self.mazo.sacar_carta())

    def mostrar_mano_casa(self, ocultar_primera_carta):
        print("Mano de la casa:")
        if ocultar_primera_carta:
            print("<Carta oculta>")
            for carta in self.casa.mano[1:]:
                print(carta)
        else:
            for carta in self.casa.mano:
                print(carta)
        print()

# `mostrar_mano_jugador` es un método que imprime la mano actual del jugador. Se repite
# a través de las cartas en la mano del jugador e imprime cada carta.
    def mostrar_mano_jugador(self):
        print("Tu mano:")
        for carta in self.jugador.mano:
            print(carta)     
        print()

# `mostrar_estado_juego` es un método que imprime el estado actual del juego, incluyendo el
# estado del jugador y la casa. Llama al método `obtener_estado_jugador` para determinar
# el estado de cada jugador basado en su mano actual, y luego imprime el estado de cada
# jugador.
    def mostrar_estado_juego(self):
        estado_casa = self.obtener_estado_jugador(self.casa)
        estado_jugador = self.obtener_estado_jugador(self.jugador)
        print(f"Estado de la Casa: {estado_casa}")
        print(f"Estado del Jugador: {estado_jugador}")
        print()

#Esta función devuelve el estado actual de un jugador en un juego, ya sea "Perdió", "Blackjack" o "En
#juego", basado en su puntaje y mano.
    def obtener_estado_jugador(self, jugador):
        puntaje = jugador.calcular_puntaje()
        if puntaje > 21:
            return "Perdió"
        elif puntaje == 21 and len(jugador.mano) == 2:
            return "Blackjack"
        else:
            return "En juego"


#Esta función permite al jugador elegir si pedir otra carta o dejar de jugar en una carta.
#:return: ya sea cuando el jugador decide detenerse (opción "S") o cuando la mano del jugador llega a un
#otro estado que no sea "En juego".
    def turno_jugador(self):
        while True:
            opcion = input("¿Deseas pedir una carta (P) o parar (S)? ").upper()
            if opcion == "P":
                carta = self.mazo.sacar_carta()
                self.jugador.recibir_carta(carta)
                print(f"Has recibido la carta: {carta}")
                self.mostrar_mano_casa(ocultar_primera_carta=True)
                self.mostrar_mano_jugador()
                estado_jugador = self.obtener_estado_jugador(self.jugador)
                if estado_jugador != "En juego":
                    return
            elif opcion == "S":
                print("Has decidido parar.")
                return
            else:
                print("Opción inválida. Por favor, elige 'P' para pedir una carta o 'S' para parar.")

#Esta función hace que la casa robe cartas hasta que su puntuación sea de al menos 19.
    def turno_casa(self):
        while self.casa.calcular_puntaje() < 19:
            carta = self.mazo.sacar_carta()
            self.casa.recibir_carta(carta)
            print("La casa ha recibido una carta.")                

#Esta función determina el ganador de un juego de blackjack en función de las puntuaciones del jugador y casa.
#:return: La función `determinar_ganador` devuelve una cadena indicando el ganador del juego
    def determinar_ganador(self):
        puntaje_jugador = self.jugador.calcular_puntaje()
        puntaje_casa = self.casa.calcular_puntaje()

        if puntaje_jugador > 21 or (puntaje_casa <= 21 and puntaje_jugador < puntaje_casa):
            return "Casa"
        elif puntaje_casa > 21 or puntaje_jugador > puntaje_casa:
            if puntaje_jugador == 21 and len(self.jugador.mano) == 2:
                return "Jugador con Blackjack"
            return "Jugador"
        elif puntaje_jugador == puntaje_casa:
            return "Empate"
        else:
            return "Casa"        

#Esta función juega un juego de blackjack y determina el ganador.
    def jugar_partida(self):
        self.repartir_cartas_iniciales()
        self.mostrar_mano_casa(ocultar_primera_carta=True)
        self.mostrar_mano_jugador()

        while True:
            self.mostrar_estado_juego()
            self.turno_jugador()

            if self.jugador.calcular_puntaje() > 21:
                break

        self.mostrar_mano_casa(ocultar_primera_carta=False)
        self.turno_casa()

        ganador = self.determinar_ganador() 
        
        print("¡El juego ha terminado!")
        ganador_final = f"Resultado: {ganador} gana."
        print(ganador_final)
        self.write_nickname_choice_to_file(self.user_nickname, self.user_id_value, self.jugador.mano, ganador_final)

#Esta función lee un archivo JSON de una ruta específica y devuelve su contenido como un diccionario, o
#un diccionario vacío si el archivo no se encuentra o no se puede decodificar.      
    def read_file(self):
        file_path = "task_5/logs.json"
        try:
            with open(file_path, "r") as f:
                data_dict = json.load(f)
        except FileNotFoundError:
            data_dict = {}
        except json.JSONDecodeError:
            data_dict = {}
        return data_dict

#Esta función muestra las estadísticas de los 5 registros más recientes de un usuario determinado.
#:param data: un diccionario que contiene los datos del juego, donde las claves son cadenas que representan la fecha
#y la hora del juego en el formato "ddmmyyyy_hhmm", y los valores son diccionarios que contienen el
#puntajes de cada jugador en ese juego
#:param usuario: El parámetro "usuario" es una variable de cadena que representa el nombre de usuario del
#usuario cuyas estadísticas recientes se muestran
    def mostrar_estadisticas_recientes(self, data, usuario):
        print(f"\nEstadísticas de los 5 registros más recientes para el usuario {usuario}:\n")
        fechas = [datetime.strptime(fecha_hora, "%d%m%Y_%H%M") for fecha_hora in data.keys()]
        fechas_ordenadas = sorted(fechas, reverse=True)

        contador = 0
        for fecha in fechas_ordenadas:
            if contador >= 5:
                break

            fecha_hora = fecha.strftime("%d%m%Y_%H%M")
            if fecha_hora in data:
                usuarios = data[fecha_hora]
                if usuario in usuarios:
                    puntajes = usuarios[usuario]
                    if any("Resultado" in puntaje for puntaje in puntajes):
                        fecha_str = fecha.strftime("%d/%m/%Y")
                        hora_str = fecha.strftime("%H:%M")
                        print(f"Fecha: {fecha_str} - Hora: {hora_str}")
                        print(f"Usuario: {usuario} - Partida: {' '.join(map(str, puntajes))}\n")
                        contador += 1
        self.write_nickname_choice_to_file(usuario, user_id_param=None, point_param= None, ganador= None)  


#La función "mostrar_usuarios" lee un archivo que contiene datos del usuario y devuelve un diccionario con
#nombres de usuario enumerados.
#:return: un diccionario llamado `enum_usuarios` que contiene una enumeración de los nombres de usuario de todos
#los usuarios que han jugado el juego antes. Las claves del diccionario son números enteros a partir del 1
#y los valores son los nombres de usuario. Si no hay usuarios existentes, la función imprime un mensaje y
#devuelve un diccionario vacío.
    def mostrar_usuarios(self):
        enum_usuarios={}
        if existing_users := self.read_file():
            i = 0
            for fecha_hora, usuarios in existing_users.items():
                for user, puntajes in usuarios.items():
                    for puntaje in puntajes:
                        enum_usuarios[i+1]= (f"{user}")
                        i += 1
            print()
        else: 
            print("Al parecer no hay usuarios previamente registrados que hayan jugado")
        return enum_usuarios


#Esta función elimina los valores duplicados de un diccionario y devuelve un nuevo diccionario con valores únicos.
#valores.
#:param input_dict: un diccionario que contiene pares clave-valor donde los valores pueden tener duplicados
#:return: un diccionario con los mismos pares clave-valor que el diccionario de entrada, pero con cualquier duplicado
#valores eliminados. El diccionario también se imprime en la consola.

    def eliminar_repetidos(self, input_dict):
        unique_dict = {}
        for key, value in input_dict.items():
            if value not in unique_dict.values():
                unique_dict[key] = value
        print(unique_dict)
        return unique_dict


#Esta función permite al usuario elegir un usuario de una lista de opciones y muestra su reciente
#Estadísticas.
#:return: un valor booleano. Si la función muestra con éxito las estadísticas de un usuario elegido,
#devuelve Falso. De lo contrario, devuelve True.
    
    def choose_user(self):
        return_value = True
        usuarios = self.eliminar_repetidos(self.mostrar_usuarios())
        if usuarios:
            opciones_validas = dict(usuarios.items())
            while True:
                opcion = input("Elija un usuario por su número correspondiente: ")
                if opcion.isdigit() and int(opcion) in opciones_validas:
                    break
                print("Opción inválida. Por favor, ingrese un número válido de usuario.")
            self.mostrar_estadisticas_recientes(self.read_file(), usuarios[int(opcion)])
            return_value = False
        return return_value
    

#La función "salir" imprime un mensaje y devuelve False para salir de un juego.
#:return: un valor booleano de False.   
    def salir(self):
        print("Gracias por jugar, lo esperamos pronto")
        return False

    def opcion_por_defecto():
        print("Opción inválida")


#Esta función escribe el apodo elegido por el usuario, los puntos del juego y el ganador en un archivo JSON para
#fines estadísticos.
    def write_nickname_choice_to_file(self, nick_name, user_id_param, point_param, ganador):
        now = datetime.now()
        if user_id_param == None:
            user_id = now.strftime("%d%m%Y_%H%M")
        else: 
            user_id = user_id_param
        
        if point_param == None:
             points = " "
        else: 
            card_strings = [str(card) for card in point_param]
            points =  ' '.join(card_strings) + f' - Fin --> {ganador}'
        file_name = "task_5/logs.json"
        data = self.read_file()
        
        if user_id in data:
            if nick_name in data[user_id]:
                data[user_id][nick_name].append(points)
            else:
                data[user_id][nick_name] = [points]
        else:
            data[user_id] = {nick_name: [points]}
            
        with open(file_name, "w") as f:
            json.dump(data, f)
            f.write('\n')
        self.user_id_value= None
        self.user_id_value= user_id
        self.user_nickname= None
        self.user_nickname= nick_name
        print(f"¡Tu nickname {nick_name} y partida han sido guardados en nuestras bitacoras con fines estadisticos!")
        return False
            

#Esta función solicita al usuario que ingrese un apodo, genera una ID de usuario única basada en el
#fecha y hora actuales, y escribe el apodo del usuario y los resultados del juego en un archivo JSON.
#:return: un valor booleano de False.            
    def write_nickname_to_file(self):
        now = datetime.now()
        user_id = now.strftime("%d%m%Y_%H%M")
        nick_name = input("Por favor, ingresa el nickname con el que iniciaras el juego: \n")
        #points = int(input("Ingresa la cantidad de puntos: "))
        points = " "
        file_name = "task_5/logs.json"
        data = self.read_file()
        
        if user_id in data:
            if nick_name in data[user_id]:
                print(f"usuario ya existe, el resultado de tu partida se guardara bajo el nickname {nick_name}")
                data[user_id][nick_name].append(points)
            else:
                data[user_id][nick_name] = [points]
        else:
            data[user_id] = {nick_name: [points]}
            
        with open(file_name, "w") as f:
            json.dump(data, f)
            f.write('\n')
        self.user_id_value= user_id
        self.user_nickname= nick_name
        print(f"¡Tu nickname {nick_name} y partida seran guardados en nuestras bitacoras con fines estadisticos!")
        return False        
            
#Esta funcion de swift en Python que asigna diferentes opciones a las funciones correspondientes.
#:param opcion: El parámetro "opcion" es una cadena que representa la elección de acción del usuario en un
#menú. Se usa como una clave en un diccionario para determinar qué función llamar en función de la eleccion del usuario     
    def switch(self, opcion):
        switcher = { "N": self.write_nickname_to_file, "E": self.choose_user, "S": self.salir }
        funcion = switcher.get(opcion, self.opcion_por_defecto)
        funcion()

#Esta función presenta al usuario opciones para iniciar un juego con un apodo nuevo o existente y
#valida su entrada.     
    def iniciar(self):
        ask = True
        opciones_validas = {"N":"Jugar con nickname nuevo", "S": "Salir"}
        if list(self.read_file().keys()):
            opciones_validas["E"]= "Jugar con nickname existente"
        opcion = (input(f"¿Deseas {opciones_validas} \n(Elige un numero de las opciones desplegadas): \n"))
        while ask:  
            if opcion.upper() in opciones_validas:
                ask = self.switch(opcion.upper())
            else: 
                opcion = input(f"Opción no valida: ¿Deseas {opciones_validas} \n(Elige un numero de las opciones desplegadas): \n")
        
        
if __name__ == "__main__":
    juego = Juego()
    juego.jugar_partida()