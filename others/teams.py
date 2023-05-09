# Solicitar el número de equipos en el torneo
num_equipos = int(input("¿Cuántos equipos participaron en el torneo? "))

# Crear una lista vacía para almacenar los nombres de los equipos
equipos = []

# Solicitar los nombres de los equipos y agregarlos a la lista
for i in range(num_equipos):
    nombre_equipo = input(f"Ingrese el nombre del equipo {i+1}: ")
    equipos.append(nombre_equipo)

# Solicitar el número de contrincantes que tuvo cada equipo
num_contrincantes = int(input("¿Cuántos contrincantes tuvo cada equipo? "))

# Crear un diccionario vacío para almacenar los resultados de los marcadores
marcadores = {}

# Solicitar los resultados de los marcadores y agregarlos al diccionario
for equipo in equipos:
    marcadores[equipo] = []
    for i in range(num_contrincantes):
        contrincante = input(f"Ingrese el nombre del contrincante {i+1} de {equipo}: ")
        marcador_equipo = int(input(f"Ingrese el marcador de {equipo}: "))
        marcador_contrincante = int(input(f"Ingrese el marcador de {contrincante}: "))
        puntos_ganados = 0
        if marcador_equipo > marcador_contrincante:
            puntos_ganados = marcador_equipo - marcador_contrincante
        elif marcador_equipo == marcador_contrincante:
            puntos_ganados = 1
        marcadores[equipo].append((contrincante, puntos_ganados))

# Calcular los puntos acumulados por equipo
puntos = {}
for equipo in equipos:
    puntos[equipo] = 0
    for contrincante, puntos_ganados in marcadores[equipo]:
        puntos[equipo] += puntos_ganados

# Imprimir los puntos acumulados por equipo
for equipo, puntuacion in puntos.items():
    print(f"{equipo}: {puntuacion} puntos")
