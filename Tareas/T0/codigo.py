from menus import guardar_puntaje, menu_inicial, menu_juego, guardar_partida, cargar_partida,\
    ranking
from tablero import print_tablero
from funciones import creacion_tablero, cantidad_bestias, posicion_bestias, descubrir_sector,\
    despejar_sector, comprobar_rango
from parametros import POND_PUNT

nombre_usuario = input("Ingrese su nombre de usuario: ").capitalize()
inicio = menu_inicial()
puntaje = 0
finalizar_juego = False
partida_creada = True
while finalizar_juego == False:
    if inicio == "Crear partida":
        respuesta_volver = input("Si deseas volver atras, escribe 'volver'; si deseas" + \
            " continuar, presiona cualquier tecla ")
        if respuesta_volver.lower() == "volver":
            inicio = menu_inicial()
            continue
        print("Para comenzar debes ingresar las medidas del tablero")
        tablero_actual = creacion_tablero()
        numero_filas = len(tablero_actual)
        numero_columnas = len(tablero_actual[0])
        numero_bestias = cantidad_bestias(tablero_actual)
        ubicacion_bestias = posicion_bestias(numero_bestias, tablero_actual)
        casillas_descubiertas = 0
        seguir_jugando = True
        while seguir_jugando:
            print_tablero(tablero_actual)
            print("Este es el tablero actual.\n")
            if casillas_descubiertas == (len(tablero_actual) * len(tablero_actual[0])) - \
                    numero_bestias:
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias, 
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"Haz ganado {nombre_usuario}! Tu puntuacion ha sido de {puntaje}")
                guardar_puntaje(nombre_usuario, puntaje)
                puntaje = 0
                seguir_jugando = False
                inicio = menu_inicial()
                break
            siguiente_movimiento = menu_juego()
            if siguiente_movimiento == "Descubrir un sector":
                rangos_validos = False
                while rangos_validos == False:
                    fila = input("¿En que fila se ubica la posicion a desbloquear? ")
                    columna = input("¿En que columna se ubica la posicion a desbloquear? ")
                    if columna.isnumeric() == False:
                        for i in range(15):
                            if "ABCDEFGHIJLKLMN"[i] == columna.upper():
                                columna = str(i)
                    rangos_validos = comprobar_rango(numero_filas, numero_columnas, fila, columna)
                    if rangos_validos == False:
                        print("\nValores fuera del rango del tablero. Intentalo nuevamente\n")
                respuesta = descubrir_sector(fila, columna, ubicacion_bestias, tablero_actual)
                if respuesta == "Vacio":
                    tablero_actual, contador = despejar_sector(fila, columna, tablero_actual,
                    ubicacion_bestias)
                    tablero_actual[int(fila)][int(columna)] = contador
                    casillas_descubiertas += 1
                    puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                elif respuesta == "Bestia":
                    print("Haz perdido, en esa ubicación se encontraba una bestia")
                    guardar_puntaje(nombre_usuario, puntaje)
                    puntaje = 0
                    seguir_jugando = False
                    finalizar_juego = True
                elif respuesta == "Ocupado":
                    print("Ya has desbloqueado ese lugar! Intentalo con una zona no descubierta")
            elif siguiente_movimiento == "Guardar partida":
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias,
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"{nombre_usuario}, se ha guardado tu partida. Tienes un puntaje de {puntaje}")
            elif siguiente_movimiento == "Guardar y salir":
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias,
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"{nombre_usuario}, se ha guardado tu partida. Tienes un puntaje de {puntaje}")
                puntaje = 0
                seguir_jugando = False
                finalizar_juego = True
            elif siguiente_movimiento == "Volver al menu inicial":
                seguir_jugando = False
                inicio = menu_inicial() 
                continue
            elif siguiente_movimiento == "Salir":
                respuesta_salir = input("¿Estas seguro que quieres salir sin guardar? " + \
                "Si deseas salir escribe cualquier tecla. En caso contrario, escribe 'volver' ")
                if respuesta_salir.lower() == "volver":
                    continue
                puntaje = 0
                seguir_jugando = False
                finalizar_juego = True
            else:
                print("Respuesta no valida, por favor intentar nuevamente\n")
    elif inicio == "Cargar partida":
        puntaje, tablero_actual, ubicacion_bestias, casillas_descubiertas = \
            cargar_partida(nombre_usuario)
        seguir_jugando = True
        if puntaje == "No existe nadie":
            seguir_jugando = False
            inicio = menu_inicial()
        while seguir_jugando:
            numero_filas = len(tablero_actual)
            numero_columnas = len(tablero_actual[0]) 
            print_tablero(tablero_actual)
            print("Este es el tablero actual.\n")
            numero_bestias = len(ubicacion_bestias)
            if casillas_descubiertas == (len(tablero_actual) * len(tablero_actual[0])) - \
                    numero_bestias:
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias,
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"Haz ganado {nombre_usuario}! Tu puntuacion ha sido de {puntaje}")
                guardar_puntaje(nombre_usuario, puntaje)
                puntaje = 0
                seguir_jugando = False
                finalizar_juego = True
                break
            siguiente_movimiento = menu_juego()
            if siguiente_movimiento == "Descubrir un sector":
                rangos_validos = False
                while rangos_validos == False:
                    fila = input("¿En que fila se ubica la posicion a desbloquear? ")
                    columna = input("¿En que columna se ubica la posicion a desbloquear? ")
                    if columna.isnumeric() == False:
                        for i in range(15):
                            if "ABCDEFGHIJLKLMN"[i] == columna.upper():
                                columna = str(i)
                    rangos_validos = comprobar_rango(numero_filas, numero_columnas, fila, columna)
                    if rangos_validos == False:
                        print("\nValores fuera del rango del tablero. Intentalo nuevamente\n")
                respuesta = descubrir_sector(fila, columna, ubicacion_bestias, tablero_actual)
                if respuesta == "Vacio":
                    tablero_actual, contador = despejar_sector(fila, columna, tablero_actual,
                    ubicacion_bestias)
                    tablero_actual[int(fila)][int(columna)] = contador
                    casillas_descubiertas += 1
                    puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                elif respuesta == "Bestia":
                    print("Haz perdido, en esa ubicación se encontraba una bestia")
                    guardar_puntaje(nombre_usuario, puntaje)
                    puntaje = 0
                    seguir_jugando = False
                    finalizar_juego = True
                elif respuesta == "Ocupado":
                    print("Ya has desbloqueado ese lugar! Intentalo con una zona no descubierta")
            elif siguiente_movimiento == "Guardar partida":
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias,
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"{nombre_usuario}, se ha guardado tu partida. Tienes un puntaje de {puntaje}")
            elif siguiente_movimiento == "Guardar y salir":
                guardar_partida(nombre_usuario, tablero_actual, ubicacion_bestias,
                casillas_descubiertas)
                puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
                print(f"{nombre_usuario}, se ha guardado tu partida. Tienes un puntaje de {puntaje}")
                puntaje = 0
                seguir_jugando = False
                finalizar_juego = True
            elif siguiente_movimiento == "Volver al menu inicial":
                seguir_jugando = False
                inicio = menu_inicial()
                continue
            elif siguiente_movimiento == "Salir":
                respuesta_salir = input("¿Estas seguro que quieres salir sin guardar?" + \
                " Si deseas salir escribe cualquier tecla. En caso contrario, escribe 'volver' ")
                if respuesta_salir.lower() == "volver":
                    continue
                puntaje = 0
                seguir_jugando = False
                finalizar_juego = True
            else:
                print("Respuesta no valida, por favor intentar nuevamente\n")
    elif inicio == "Ver ranking":
        lista_ranking = ranking()
        inicio = menu_inicial()
    elif inicio == "Salir":
        respuesta_salir = input("¿Estas seguro que quieres salir? Si deseas salir escribe" + \
            " cualquier tecla. En caso contrario, escribe 'volver'")
        if respuesta_salir.lower() == "volver":
            inicio = menu_inicial()
            continue
        seguir_jugando = False
        finalizar_juego = True
