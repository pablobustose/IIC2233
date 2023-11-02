from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTO_DEFENSA, GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, \
    GASTO_ENERGIA_POCION, PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION

class Objetos(ABC):
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo
    
    @abstractmethod
    def aplicar_objeto(self, programon):
        print(f"Programón beneficiado: {programon.nombre}")
        print(f"Objeto utilizado: {self.nombre} (Tipo {self.tipo})")

class Baya(Objetos):
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_BAYA
        self.exito = PROB_EXITO_BAYA
    
    def aplicar_objeto(self, programon):
        aumento_vida = randint(1, 10)
        vida_antigua = programon.vida
        programon.vida += aumento_vida
        super().aplicar_objeto(programon)
        print(f"Aumento vida: {aumento_vida}")
        print(f"La vida subió de {vida_antigua} a {programon.vida}")

class Pocion(Objetos):
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_POCION
        self.exito = PROB_EXITO_POCION

    def aplicar_objeto(self, programon):
        aumento_ataque = randint(1, 7)
        ataque_antiguo = programon.ataque
        programon.ataque += aumento_ataque
        super().aplicar_objeto(programon)
        print(f"Aumento ataque: {aumento_ataque}")
        print(f"El ataque subió de {ataque_antiguo} a {programon.ataque}")

class Caramelo(Pocion, Baya):
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre, tipo)
        self.costo = GASTO_ENERGIA_CARAMELO
        self.exito = PROB_EXITO_CARAMELO

    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        defensa_antigua = programon.defensa
        programon.defensa += AUMENTO_DEFENSA
        print(f"Aumento defensa: {AUMENTO_DEFENSA}")
        print(f"La defensa subió de {defensa_antigua} a {programon.defensa}")
