# La clase "Mazo" crea un mazo de cartas y permite sacar una carta del mazo.
import random
from card import Card
class Deck:

# `__init__(self)` es un método especial en las clases de Python que se llama cuando un objeto del
# se crea la clase. En este código específico, `__init__(self)` inicializa la baraja de cartas por
# crear una lista de cartas con todas las combinaciones posibles de palos y valores, y luego
# baraja la baraja.
        
    def __init__(self):
        palos = ['♠', '♥', '♦', '♣']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cartas = [Card(valor, palo) for palo in palos for valor in valores]
        random.shuffle(self.cartas)

# `sacar_carta` es un método que quita y devuelve la carta superior de la baraja.
    def sacar_carta(self):
        return self.cartas.pop()