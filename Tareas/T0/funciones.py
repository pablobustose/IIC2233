def creacion_tablero() -> list:
    seguir_filas = True
    seguir_columnas = True
    n_filas_tablero = ""
    n_columnas_tablero = ""
    while seguir_filas:
        n_filas = input("¿Cuantas filas tiene el tablero? Debe ser un valor entre 3 y 15 ")
        if n_filas.isnumeric() == False:
            print("Debe ser un valor numerico")
        elif 3 <= int(n_filas) <= 15:
            n_filas_tablero = int(n_filas)
            seguir_filas = False
        else:
            print("El valor debe estar entre 3 y 15")
    while seguir_columnas:
        n_columnas = input("¿Cuantas columnas tiene el tablero? Debe ser un valor entre 3 y 15 ")
        if n_columnas.isnumeric() == False:
            print("Debe ser un valor numerico")
        elif 3 <= int(n_columnas) <= 15:
            n_columnas_tablero = int(n_columnas)
            seguir_columnas = False
        else:
            print("El valor debe estar entre 3 y 15")
    tablero = [[" " for i in range(int(n_columnas_tablero))] for j in range(int(n_filas_tablero))]
    #se crea tablero de i x j donde cada ubicacion está compuesta solo por un " "
    return tablero

def cantidad_bestias(tablero: list) -> int: 
    from parametros import PROB_BESTIA
    from math import ceil
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    numero = numero_columnas * numero_filas * PROB_BESTIA
    numero_final = ceil(numero)
    return numero_final

def posicion_bestias(numero_bestias: int, tablero: list) -> list:
    from random import randint
    posicion_bestias = []
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    for i in range(numero_bestias):
        seguir = True
        while seguir:
            fila = randint(0,numero_filas - 1)
            columna = randint(0,numero_columnas - 1)
            posicion = [fila, columna]
            if posicion not in posicion_bestias:
                posicion_bestias.append(posicion)
                seguir = False
    return posicion_bestias

def despejar_sector(fila: str, columna: str, tablero_actual: list, ubicacion_bestias: list):
    if columna.isnumeric() == False:
        for i in range(15):
            if "ABCDEFGHIJLKLMN"[i] == columna.upper():
                columna = str(i)
    fila = int(fila)
    columna = int(columna)
    posicion = [fila, columna]
    for elemento in tablero_actual:
        elemento.insert(0, " ")
        elemento.append(" ")
    agregar = [" "]*len(tablero_actual[0])
    tablero_actual.insert(0, agregar)
    tablero_actual.append(agregar)
    coordenada_fila = posicion[0]
    coordenada_columna = posicion[1]
    contador = 0
    if [(coordenada_fila - 1), (coordenada_columna - 1)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila - 1), (coordenada_columna)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila - 1), (coordenada_columna + 1)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila), (coordenada_columna - 1)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila), (coordenada_columna + 1)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila + 1), (coordenada_columna - 1)] in ubicacion_bestias:
        contador +=1
    elif [(coordenada_fila + 1), (coordenada_columna)] in ubicacion_bestias:
        contador +=1
    if [(coordenada_fila + 1), (coordenada_columna + 1)] in ubicacion_bestias:
        contador +=1
    tablero_actual.pop(-1)
    tablero_actual.pop(0)
    for elemento1 in tablero_actual:
        elemento1.pop(-1)
        elemento1.pop(0)
    return tablero_actual, contador

def descubrir_sector(fila: str, columna: str, ubicacion_bestias: list, tablero_actual: list) -> str:
    if columna.isnumeric() == False:
        for i in range(15):
            if "ABCDEFGHIJLKLMN"[i] == columna.upper():
                columna = str(i)
    fila = int(fila)
    columna = int(columna)
    posicion = [fila, columna]
    if posicion in ubicacion_bestias:
        return "Bestia"
    elif tablero_actual[fila][columna] == " ":
        return "Vacio"
    else:
        return "Ocupado"

def comprobar_rango(numero_filas: int, numero_columnas: int, fila_ingresada: str, 
columna_ingresada: str):
    if columna_ingresada.isnumeric() == False:
        for i in range(15):
            if "ABCDEFGHIJLKLMN"[i] == columna_ingresada.upper():
                columna_ingresada = str(i)
    if fila_ingresada.isnumeric() == False or columna_ingresada.isnumeric() == False:
        return False
    if 0 <= int(fila_ingresada) <= (numero_filas - 1) and 0 <= int(columna_ingresada) <= (numero_columnas - 1):
        return True
    else:
        return False
