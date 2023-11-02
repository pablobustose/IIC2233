from random import random, randint
from objetos import Baya, Caramelo, Pocion
from parametros import GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, GASTO_ENERGIA_POCION, \
    PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION

class Entrenador:
    def __init__(self, nombre: str, energia: int, programones: list, objetos: list):
        self.nombre = nombre
        self._energia = energia
        self.programones = programones
        self.objetos = objetos
    
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, nuevo_valor):
        if nuevo_valor <= 0:
            self._energia = 0
        else:
            self._energia = nuevo_valor
    
    def estado(self):
        objetos = ""
        for objeto in self.objetos:
            objetos += f"{objeto.nombre}, "
        print("        *** Estado entrenador ***       ")
        print("-----------------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Energía: {self.energia}")
        print(f"Objetos: {objetos}")
        print("-----------------------------------------")
        print("               Programones              ")
        print("-----------------------------------------")
        print("     NOMBRE    |  TIPO  | NIVEL |  VIDA  ")
        print("-----------------------------------------")
        for programon in self.programones:
            print(f"{programon.nombre:14.14s} | {programon.tipo:<7s}|  {programon.nivel:<3d} " + \
                f" |  {programon.vida: <3d}") 
        print("-----------------------------------------")
        print("[1] Volver")
        print("[2] Salir\n")
        
    def crear_objeto(self, tipo: str):
        from funciones import crear_lista_objetos 
        lista_objetos = crear_lista_objetos()
        if tipo == "baya":
            probabilidad = random()
            if self.energia < GASTO_ENERGIA_BAYA:
                print("No tienes energía suficiente\n")
            elif probabilidad <= PROB_EXITO_BAYA:
                self.energia -= GASTO_ENERGIA_BAYA
                mismo_tipo = False
                while mismo_tipo == False:
                    posicion_objeto = randint(0, len(lista_objetos) - 1)
                    if lista_objetos[posicion_objeto][1] == "baya":
                        crear_objeto = Baya(lista_objetos[posicion_objeto][0], "baya")
                        self.objetos.append(crear_objeto)
                        print(f"Se ha creado el objeto {crear_objeto.nombre}\n")
                        mismo_tipo = True
            else:
                self.energia -= GASTO_ENERGIA_BAYA
                print(f"No se ha podido crear el objeto de tipo Baya. Haz perdido " + \
                f"{GASTO_ENERGIA_BAYA} de energía")
        elif tipo == "pocion":
            probabilidad = random()
            if self.energia < GASTO_ENERGIA_POCION:
                print("No tienes energía suficiente\n")
            elif probabilidad <= PROB_EXITO_POCION:
                self.energia -= GASTO_ENERGIA_POCION
                mismo_tipo = False
                while mismo_tipo == False:
                    posicion_objeto = randint(0, len(lista_objetos) - 1)
                    if lista_objetos[posicion_objeto][1] == "pocion":
                        crear_objeto = Pocion(lista_objetos[posicion_objeto][0], "pocion")
                        self.objetos.append(crear_objeto)
                        print(f"Se ha creado el objeto {crear_objeto.nombre}\n")
                        mismo_tipo = True
            else:
                self.energia -= GASTO_ENERGIA_POCION
                print(f"No se ha podido crear el objeto de tipo Poción. Haz perdido" + \
                f" {GASTO_ENERGIA_POCION} de energía")
        elif tipo == "caramelo":
            probabilidad = random()
            if self.energia < GASTO_ENERGIA_CARAMELO:
                print("No tienes energía suficiente\n")
            elif probabilidad <= PROB_EXITO_CARAMELO:
                self.energia -= GASTO_ENERGIA_CARAMELO
                mismo_tipo = False
                while mismo_tipo == False:
                    posicion_objeto = randint(0, len(lista_objetos) - 1)
                    if lista_objetos[posicion_objeto][1] == "caramelo":
                        crear_objeto = Caramelo(lista_objetos[posicion_objeto][0], "caramelo")
                        self.objetos.append(crear_objeto)
                        print(f"Se ha creado el objeto {crear_objeto.nombre}\n")
                        mismo_tipo = True
            else:
                self.energia -= GASTO_ENERGIA_CARAMELO
                print(f"No se ha podido crear el objeto de tipo Caramelo. Haz perdido " + \
                f"{GASTO_ENERGIA_CARAMELO} de energía")

    