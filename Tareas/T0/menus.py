def menu_inicial() -> str:
    modo_juego = input("\nSeleccione una opcion:\n[1] Crear partida\n[2] Cargar" + \
            " partida\n[3] Ver ranking\n[0] Salir\n")
    seguir_modo_juego = True
    while seguir_modo_juego:
        if modo_juego == "1":
            modo_juego = "Crear partida"
            seguir_modo_juego = False
            return modo_juego
        elif modo_juego == "2":
            modo_juego = "Cargar partida"
            seguir_modo_juego = False
            return modo_juego
        elif modo_juego == "3":
            modo_juego = "Ver ranking"
            seguir_modo_juego = False
            return modo_juego
        elif modo_juego == "0":
            modo_juego = "Salir"
            seguir_modo_juego = False
            return modo_juego
        else:
            print("Respuesta no valida, por favor intentar nuevamente\n")
            modo_juego = input("Seleccione una opcion:\n[1] Crear partida\n[2] " + \
            "Cargar partida\n[3] Ver ranking\n[0] Salir\n")
def menu_juego() -> str:
    siguiente_jugada = input("Seleccione una opcion:\n[1] Descubrir un sector\n[2] Guardar" + \
            " partida\n[3] Guardar y salir\n[4] Volver al menu inicial\n[0] Salir\n")
    seguir_siguiente_jugada = True
    while seguir_siguiente_jugada:
        if siguiente_jugada == "1":
            siguiente_jugada = "Descubrir un sector"
            seguir_siguiente_jugada = False
            return siguiente_jugada
        elif siguiente_jugada == "2":
            siguiente_jugada = "Guardar partida"
            seguir_siguiente_jugada = False
            return siguiente_jugada
        elif siguiente_jugada == "3":
            siguiente_jugada = "Guardar y salir"
            seguir_siguiente_jugada = False
            return siguiente_jugada
        elif siguiente_jugada == "4":
            siguiente_jugada = "Volver al menu inicial"
            seguir_siguiente_jugada = False
            return siguiente_jugada
        elif siguiente_jugada == "0":
            siguiente_jugada = "Salir"
            seguir_siguiente_jugada = False
            return siguiente_jugada
        else:
            print("Respuesta no valida, por favor intentar nuevamente\n")
            siguiente_jugada = input("Seleccione una opcion:\n[1] Descubrir un sector\n[2] " + \
            "Guardar partida\n[3] Salir con guardar\n[0] Salir sin guardar\n")

def guardar_partida(nombre_usuario: str, tablero_actual: list, ubicacion_bestias: list, 
casillas_descubiertas: int):
    from os import path
    from parametros import POND_PUNT
    direccion = path.join("partidas", nombre_usuario + ".txt")
    archivo = open(direccion, "w")
    puntaje = len(ubicacion_bestias) * casillas_descubiertas * POND_PUNT
    archivo.write(str(puntaje) + "\n")
    elemento_para_escribir = "-".join(str(elemento) for elemento in tablero_actual)
    archivo.write(elemento_para_escribir + "\n")
    ubicacion_para_escribir = "-".join(str(ubicacion) for ubicacion in ubicacion_bestias)
    archivo.write(ubicacion_para_escribir + "\n") 
    archivo.write(str(casillas_descubiertas))
    archivo.close()

def cargar_partida(nombre_usuario: str):
    from os import path, listdir
    archivos = listdir("partidas")
    nombres = []
    for elemento in archivos:
        elemento = elemento.strip(".txt")
        nombres.append(elemento)
    if nombre_usuario in nombres:
        direccion = path.join("partidas", nombre_usuario + ".txt")
        archivo = open(direccion)
        lista = archivo.readlines()
        puntaje = int(lista[0])
        lista.pop(0)
        casillas_descubiertas = int(lista[-1])
        lista.pop(-1)
        tablero_actual_str = lista[0].split("-")
        ubicacion_bestias_str = lista[1].split("-")
        tablero_actual = []
        ubicacion_bestias = []
        for elemento in tablero_actual_str:
            elemento = elemento.strip("\n")
            elemento_tablero_triple_comilla = elemento.strip('][').split(', ')
            elemento_final = []
            for a in elemento_tablero_triple_comilla:
                a = a.replace("'", "")
                elemento_final.append(a)
            tablero_actual.append(elemento_final)
        for ubicacion in ubicacion_bestias_str:
            ubicacion = ubicacion.strip("\n")
            agregar_ubicacion = ubicacion.strip('][').split(', ')
            ubicacion_bestias.append(agregar_ubicacion)
        for bestia in ubicacion_bestias:
            bestia[0] = int(bestia[0])
            bestia[1] = int(bestia[1])
        archivo.close()
        return puntaje, tablero_actual, ubicacion_bestias, casillas_descubiertas
    else:
        print("No existe una partida guardada con tu nombre de usuario. Deberas crear una" + \
            " partida nueva para jugar")
        return "No existe nadie", "", "", ""

def guardar_puntaje(nombre_usuario: str, puntaje: int):
    archivo = open("puntajes.txt", "a")
    puntaje_nombre= f"{puntaje}-{nombre_usuario}"
    archivo.write(str(puntaje_nombre) + "\n")
    archivo.close()

def ranking():
    archivo = open("puntajes.txt")
    lista = archivo.readlines()
    ranking = []
    for puntaje_persona in lista:
        puntaje_persona = puntaje_persona.strip("\n")
        puntaje_persona = puntaje_persona.split("-")
        puntaje_persona[0] = int(puntaje_persona[0])
        ranking.append(puntaje_persona)
    ranking = sorted(ranking, reverse = True)
    print("")
    if len(ranking) <= 10:
        for posicion in ranking:
            print(f"{posicion[0]} es la puntuacion de {posicion[1]}")
    else:
        for i in range(10):
            print(f"{ranking[i][0]} es la puntuacion de {ranking[i][1]}")
