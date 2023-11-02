from abc import ABC, abstractmethod
from random import randint
from parametros import MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA, \
    MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO

class Programon(ABC):
    def __init__(self, nombre: str, tipo: str, nivel: int, vida: int, ataque: int, defensa: int, 
    velocidad: int): 
        self.nombre = nombre
        self._tipo = tipo
        self.nivel = nivel
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa
        self._velocidad = velocidad
        self._experiencia = 0
    
    @property
    def tipo(self):
        return self._tipo

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, nueva_experiencia):
        self._experiencia = nueva_experiencia
        menor_a_100 = False
        while menor_a_100 == False:
            if self.nivel == 100:
                print(f"{self.nombre} ha llegado al nivel 100 (máximo). Ya no podrás seguir " + \
                "entrenando a este programón")
                self._experiencia = 0
                menor_a_100 = True
            elif self._experiencia >= 100 and self.nivel < 100:
                self.nivel += 1
                print(f"{self.nombre} ha aumentado su nivel a {self.nivel}")
                self._experiencia -= 100
                valor_vida = randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                valor_ataque = randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                valor_defensa = randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                valor_velocidad = randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                self.vida += valor_vida
                self.ataque += valor_ataque
                self.defensa += valor_defensa
                self.velocidad += valor_velocidad
                print(f"{self.nombre} ha aumentado {valor_vida} de vida. Ahora tiene {self.vida}")
                print(f"{self.nombre} ha aumentado {valor_ataque} de vida. Ahora tiene" + \
                f" {self.ataque}")
                print(f"{self.nombre} ha aumentado {valor_defensa} de vida. Ahora tiene " + \
                f"{self.defensa}")
                print(f"{self.nombre} ha aumentado {valor_velocidad} de vida. Ahora tiene " + \
                f"{self.velocidad}")
            elif self._experiencia < 100:
                menor_a_100 = True

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor >= 255:
            self._vida = 255
            print(f"{self.nombre} ha llegado al máximo de vida posible")
        else:
            self._vida = nuevo_valor
    
    @property
    def ataque(self):
        return self._ataque
    
    @ataque.setter
    def ataque(self, nuevo_valor):
        if nuevo_valor >= 190:
            self._ataque = 190
            print(f"{self.nombre} ha llegado al máximo de ataque posible")
        else:
            self._ataque = nuevo_valor
    
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, nuevo_valor):
        if nuevo_valor >= 250:
            self._defensa = 250
            print(f"{self.nombre} ha llegado al máximo de defensa posible")
        else:
            self._defensa = nuevo_valor
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, nuevo_valor):
        if nuevo_valor >= 200:
            self._velocidad = 200
            print(f"{self.nombre} ha llegado al máximo de velocidad posible")
        else:
            self._velocidad = nuevo_valor

    def entrenamiento(self):
        self.experiencia += randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)

    @abstractmethod
    def luchar(self, rival) -> bool: #True si gana y False si pierde
        pass

class Planta(Programon):
    def __init__(self, nombre: str, tipo: str, nivel: int, vida: int, ataque: int, defensa: int, 
    velocidad: int): 
         super().__init__(nombre, tipo, nivel, vida, ataque, defensa, velocidad)
        
    def luchar(self, rival: Programon):
        if rival.tipo == "agua":
            ventaja_usuario = 1
            ventaja_rival = -1
        elif rival.tipo == "fuego":
            ventaja_usuario = -1
            ventaja_rival = 1
        elif rival.tipo == "planta":
            ventaja_usuario = 0
            ventaja_rival = 0
        puntaje_usuario = max(0,(self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 + 
        self.defensa * 0.15 + self.velocidad * 0.2 + ventaja_usuario * 40))
        puntaje_rival = max(0,(rival.vida * 0.2 + rival.nivel * 0.3 + rival.ataque * 0.15 + 
        rival.defensa * 0.15 + rival.velocidad * 0.2 + ventaja_rival * 40))
        if puntaje_usuario > puntaje_rival:
            return True
        elif puntaje_usuario < puntaje_rival:
            return False
        elif puntaje_usuario == puntaje_rival:
            azar = randint(0,1)
            if azar == 0:
                return True
            elif azar == 1:
                return False

class Fuego(Programon):
    def __init__(self, nombre: str, tipo: str, nivel: int, vida: int, ataque: int, defensa: int, 
    velocidad: int):
         super().__init__(nombre, tipo, nivel, vida, ataque, defensa, velocidad)

    def luchar(self, rival: Programon):
        if rival.tipo == "agua":
            ventaja_usuario = -1
            ventaja_rival = 1
        elif rival.tipo == "fuego":
            ventaja_usuario = 0
            ventaja_rival = 0
        elif rival.tipo == "planta":
            ventaja_usuario = 1
            ventaja_rival = -1
        puntaje_usuario = max(0,(self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 + 
        self.defensa * 0.15 + self.velocidad * 0.2 + ventaja_usuario * 40))
        puntaje_rival = max(0,(rival.vida * 0.2 + rival.nivel * 0.3 + rival.ataque * 0.15 + 
        rival.defensa * 0.15 + rival.velocidad * 0.2 + ventaja_rival * 40))
        if puntaje_usuario > puntaje_rival:
            return True
        elif puntaje_usuario < puntaje_rival:
            return False
        elif puntaje_usuario == puntaje_rival:
            azar = randint(0,1)
            if azar == 0:
                return True
            elif azar == 1:
                return False

class Agua(Programon):
    def __init__(self, nombre: str, tipo: str, nivel: int, vida: int, ataque: int, defensa: int, 
    velocidad: int):
         super().__init__(nombre, tipo, nivel, vida, ataque, defensa, velocidad)

    def luchar(self, rival: Programon):
        if rival.tipo == "agua":
            ventaja_usuario = 0
            ventaja_rival = 0
        elif rival.tipo == "fuego":
            ventaja_usuario = 1
            ventaja_rival = -1
        elif rival.tipo == "planta":
            ventaja_usuario = -1
            ventaja_rival = 1
        puntaje_usuario = max(0,(self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 + 
        self.defensa * 0.15 + self.velocidad * 0.2 + ventaja_usuario * 40))
        puntaje_rival = max(0,(rival.vida * 0.2 + rival.nivel * 0.3 + rival.ataque * 0.15 + 
        rival.defensa * 0.15 + rival.velocidad * 0.2 + ventaja_rival * 40))
        if puntaje_usuario > puntaje_rival:
            return True
        elif puntaje_usuario < puntaje_rival:
            return False
        elif puntaje_usuario == puntaje_rival:
            azar = randint(0,1)
            if azar == 0:
                return True
            elif azar == 1:
                return False