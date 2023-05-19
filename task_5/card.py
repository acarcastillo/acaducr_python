# `Card` es una clase que representa un naipe. Tiene dos atributos, `valor` (valor) y
# `palo` (traje), que se inicializan en el constructor (`__init__`). El método `__str__` es
# definido para devolver una representación de cadena de la carta, que incluye su valor y palo.
class Card:
    
# `__init__` es un método constructor en Python que inicializa los atributos de un objeto
# cuando se crea. En este caso concreto, inicializa los atributos `valor` y `palo`
# de un objeto `Tarjeta` con los valores pasados como argumentos al constructor.    
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

#La función anterior es un método especial en Python que devuelve una representación de cadena de un objeto.
    def __str__(self):
        return f"{self.valor} {self.palo}"