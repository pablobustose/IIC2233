from random import randint
from entrenador import Entrenador
from objetos import Baya, Caramelo, Pocion
from parametros import ENERGIA_ENTRENAMIENTO, MAX_AUMENTO_EXPERIENCIA, MIN_AUMENTO_EXPERIENCIA
from programon import Agua, Fuego, Planta, Programon

def validar_respuesta(menor: int, mayor: int, eleccion: str) -> bool: 
    if eleccion.isnumeric() == False:
        print("La respuesta debe ser un número. Inténtelo nuevamente\n")
        return False
    else:
        if menor <= int(eleccion) <= mayor:
            return True
        else:
            print("Valor fuera de rango. Inténtelo Nuevamente")
            return False
        
def crear_lista_entrenadores() -> list:
    archivo = open("entrenadores.csv")
    lista_readlines = archivo.readlines()
    lista_entrenadores = []
    for linea in lista_readlines:
        entrenador = linea.strip("\n").split(",")
        lista_entrenadores.append(entrenador)
    lista_entrenadores.pop(0)
    for i in range(len(lista_entrenadores)):
        for j in range(len(lista_entrenadores[i])):
            if ";" in lista_entrenadores[i][j]:
                lista_entrenadores[i][j] = lista_entrenadores[i][j].split(";")
            else:
                lista = []
                lista.append(lista_entrenadores[i][j])
                lista_entrenadores[i][j] = lista
    for elemento in lista_entrenadores:
        elemento[0] = elemento[0][0]
        elemento[2] = int(elemento[2][0])
    archivo.close()
    return lista_entrenadores

def crear_lista_programones() -> list:
    archivo = open("programones.csv")
    lista_readlines = archivo.readlines()
    lista_programones = []
    for linea in lista_readlines:
        programon = linea.strip("\n").split(",")
        lista_programones.append(programon)
    lista_programones.pop(0)
    for programon in lista_programones:
        programon[2] = int(programon[2])
        programon[3] = int(programon[3])
        programon[4] = int(programon[4])
        programon[5] = int(programon[5])
        programon[6] = int(programon[6])
    return lista_programones

def crear_lista_objetos() -> list:
    archivo = open("objetos.csv")
    lista_readlines = archivo.readlines()
    lista_objetos = []
    for linea in lista_readlines:
        objeto = linea.strip("\n").split(",")
        lista_objetos.append(objeto)
    lista_objetos.pop(0)
    return lista_objetos

def crear_clases_entrenadores(lista_entrenadores: list, lista_programones: list, 
lista_objetos: list) -> list:
    lista_entrenadores_clase = []
    for entrenador in lista_entrenadores:
        nombre_entrenador = entrenador[0]
        energia = entrenador[2]
        lista_programones_clase = []
        for programon in entrenador[1]:
            for busqueda_programon in lista_programones:
                if programon == busqueda_programon[0]:
                    if busqueda_programon[1] == "fuego":
                        nivel = busqueda_programon[2]
                        vida = busqueda_programon[3]
                        ataque = busqueda_programon[4]
                        defensa = busqueda_programon[5]
                        velocidad = busqueda_programon[6]
                        programon_clase = Fuego(programon, "fuego", nivel, vida, ataque, defensa, 
                        velocidad)
                        lista_programones_clase.append(programon_clase)
                    elif busqueda_programon[1] == "agua":
                        nivel = busqueda_programon[2]
                        vida = busqueda_programon[3]
                        ataque = busqueda_programon[4]
                        defensa = busqueda_programon[5]
                        velocidad = busqueda_programon[6]
                        programon_clase = Agua(programon, "agua", nivel, vida, ataque, defensa, 
                        velocidad)
                        lista_programones_clase.append(programon_clase)
                    elif busqueda_programon[1] == "planta":
                        nivel = busqueda_programon[2]
                        vida = busqueda_programon[3]
                        ataque = busqueda_programon[4]
                        defensa = busqueda_programon[5]
                        velocidad = busqueda_programon[6]
                        programon_clase = Planta(programon, "planta", nivel, vida, ataque, defensa, 
                        velocidad)
                        lista_programones_clase.append(programon_clase)
        lista_objetos_clase = []
        for objeto in entrenador[3]:
            for busqueda_objeto in lista_objetos:
                if objeto == busqueda_objeto[0]:
                    if busqueda_objeto[1] == "baya":
                        objeto_clase = Baya(objeto, "baya")
                        lista_objetos_clase.append(objeto_clase)
                    elif busqueda_objeto[1] == "pocion":
                        objeto_clase = Pocion(objeto, "pocion")
                        lista_objetos_clase.append(objeto_clase)
                    elif busqueda_objeto[1] == "caramelo":
                        objeto_clase = Caramelo(objeto, "caramelo")
                        lista_objetos_clase.append(objeto_clase)
        entrenador_clase = Entrenador(nombre_entrenador, energia, lista_programones_clase, 
        lista_objetos_clase)
        lista_entrenadores_clase.append(entrenador_clase)
    return lista_entrenadores_clase

def entrenar_programon(entrenador: Entrenador, programon: Programon):
    if programon.nivel >=100:
        print(f"{programon.nombre} ha llegado al nivel 100 (máximo). Ya no podrás seguir" + \
                f" entrenando a este programón")
    elif entrenador.energia >= ENERGIA_ENTRENAMIENTO:
        entrenador.energia -= ENERGIA_ENTRENAMIENTO
        experiencia = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        programon.experiencia += experiencia
        print(f"Tu energía ha disminuido {ENERGIA_ENTRENAMIENTO} unidades y ahora" + \
                f" tienes {entrenador.energia}")
        print(f"{programon.nombre} ha aumentado {experiencia} unidades de experiencia y ahora" + \
                f" tiene {programon.experiencia}\n")

    else:
        print(f"No tienes la energía suficiente para entrenar a un programón\n")

def generar_pares(entrenador: Entrenador, lista_entrenadores: list) -> list:
    posibles_rivales = []
    for elemento in lista_entrenadores:
        if entrenador != elemento:
            posibles_rivales.append(elemento)
    lista_pares = []
    rival_entrenador = randint(0,len(posibles_rivales) - 1)
    lista_pares.append([entrenador, posibles_rivales[rival_entrenador]])
    posibles_rivales.remove(posibles_rivales[rival_entrenador])
    while len(posibles_rivales) != 0:
        par = []
        for i in range(2):
            posicion_entrenador = randint(0, len(posibles_rivales) - 1)
            par.append(posibles_rivales[posicion_entrenador])
            posibles_rivales.remove(posibles_rivales[posicion_entrenador])
        lista_pares.append(par)
    return lista_pares
        

