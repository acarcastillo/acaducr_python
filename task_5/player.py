# La clase Player representa a un jugador en un juego de cartas e incluye métodos para recibir cartas,
# calcular su puntaje y almacenar su mano.
class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

# `recibir_carta` es un método de la clase `Player` que añade una carta a la mano del jugador
# (`mano`). Toma un parámetro `carta` que representa la carta que se agregará a la mano y
# lo agrega a la lista `mano`.
    def recibir_carta(self, carta):
        self.mano.append(carta)

#Esta función calcula la puntuación de una mano en un juego de cartas, teniendo en cuenta el valor de cada
#carta y la posibilidad de tener un As.
#:return: La función `calcular_puntaje` devuelve la puntuación total de la mano de un jugador en un juego de cartas,
#teniendo en cuenta el valor de cada carta y el caso especial de tener una carta As.
    def calcular_puntaje(self):
        puntaje = 0
        tiene_as = False

        for carta in self.mano:
            if carta.valor in ['J', 'Q', 'K']:
                puntaje += 10
            elif carta.valor == 'A':
                puntaje += 11
                tiene_as = True
            else:
                puntaje += int(carta.valor)

        if puntaje > 21 and tiene_as:
            puntaje -= 10

        return puntaje