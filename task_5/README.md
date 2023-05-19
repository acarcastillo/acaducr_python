# Blackjack Game

This is a simple implementation of the Blackjack game in Python.

## Description

The code consists of the following classes:

- `Card`: Represents a playing card with attributes `value` and `suit`.
- `Deck`: Represents a deck of cards. It can shuffle the cards and deal a card.
- `Player`: Represents a player in the game. It has a name and a hand of cards.
- `Game`: Represents a game of Blackjack. It handles the logic of the game, including dealing cards, player turns, determining the winner, and writing game data to a file.

## How to Run

To play the game, run the `main.py` script. The game will prompt you to enter your name and choose an option to start a new game, view recent game statistics, or quit the game.

## Example Usage

Here is an example of how to play the game:

```python
from game import Game

# Create a new game
game = Game()

# Start the game
game.start()

# Play the game
game.play()

# End the game
game.end()

┌───────────────────┐            ┌───────────────────┐            ┌───────────────────┐
│       Card        │            │        Deck       │            │       Player      │
├───────────────────┤            ├───────────────────┤            ├───────────────────┤
│ - valor: String   │            │ - cartas: List    │            │ - nombre: String  │
│ - palo: String    │            │                   │            │ - mano: List      │
├───────────────────┤            ├───────────────────┤            ├───────────────────┤
│ + __init__()      │            │ + __init__()      │            │ + __init__()      │
│ + __str__(): str  │            │ + sacar_carta():  │            │ + recibir_carta() │
└───────────────────┘            │     Card          │            │ + calcular_puntaje│
                                 │                   │            └───────────────────┘
                                 │                   │
                                 └───────────────────┘
                                           △
                                           │
                                           │
                                           │
                                 ┌───────────────────┐
                                 │       Game        │
                                 ├───────────────────┤
                                 │ - mazo: Deck      │
                                 │ - jugador: Player │
                                 │ - casa: Player    │
                                 ├───────────────────┤
                                 │ + iniciar()       │
                                 │ + repartir_cartas │
                                 │ + mostrar_mano    │
                                 │ + turno_jugador() │
                                 │ + turno_casa()    │
                                 │ + determinar_gan. │
                                 │ + jugar_partida() │
                                 └───────────────────┘

En este diagrama, las clases se representan en rectángulos, y los atributos y métodos se enumeran debajo de ellas. Los atributos privados se indican con un guion bajo antes del nombre, mientras que los métodos públicos se indican con un signo más antes del nombre.

La clase Card representa una carta con sus atributos valor y palo, y tiene un constructor __init__ y un método __str__ para obtener una representación en cadena de la carta.

La clase Deck representa una baraja de cartas y tiene un atributo cartas que es una lista de objetos Card. Tiene un constructor __init__ que crea una baraja de cartas y las baraja, y un método sacar_carta para quitar y devolver la carta superior del mazo.

La clase Player representa un jugador en un juego de cartas y tiene atributos nombre y mano, que es una lista de objetos Card. Tiene un constructor __init__ para inicializar el nombre del jugador y la mano, y un método recibir_carta para agregar una carta a la mano del jugador. También tiene un método calcular_puntaje para calcular la puntuación total de la mano del jugador.

La clase Game representa un juego de cartas, específicamente el juego de Blackjack. Tiene atributos mazo de tipo Deck, jugador y casa de tipo Player. Tiene métodos para iniciar el juego, repartir cartas

Requirements
Python 3.x


## Autor

Este programa fue desarrollado por:
## Autors ✒️


* **Carlos Castillo Aleman** - *Initial work* - [acarcastillo](https://github.com/acarcastillo)
