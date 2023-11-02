from funciones import crear_clases_entrenadores, crear_lista_entrenadores, crear_lista_objetos, \
    crear_lista_programones, entrenar_programon, generar_pares, validar_respuesta
from liga import LigaProgramon
from menus import menu_inicial, menu_entrenador

nueva_partida = True
while nueva_partida:
    lista_entrenadores = crear_clases_entrenadores(crear_lista_entrenadores(), \
        crear_lista_programones(), crear_lista_objetos())
    liga_programon = LigaProgramon(lista_entrenadores)
    lista_objetos = crear_lista_objetos()
    eleccion = menu_inicial()
    for posible_entrenador in lista_entrenadores:
        if posible_entrenador.nombre == eleccion:
            entrenador = posible_entrenador
            print(f"\nHaz seleccionado a {entrenador.nombre} para combatir en el DCCampeonato\n")
    if eleccion == "Salir":
        seguir_partida_actual = False
        nueva_partida = False
    else:
        seguir_partida_actual = True

    while seguir_partida_actual:
        accion = menu_entrenador()
        if accion == "Entrenamiento":
            for i in range(len(entrenador.programones)):
                print(f"[{i + 1}] {entrenador.programones[i].nombre}")
            respuesta_valida = False
            while respuesta_valida == False:
                programon_a_entrenar = input("¿A qué programón te gustaría entrenar? ")
                print()
                if validar_respuesta(1, len(entrenador.programones), programon_a_entrenar) == True:
                    respuesta_valida = True
            programon_a_entrenar = entrenador.programones[int(programon_a_entrenar) - 1]
            entrenar_programon(entrenador, programon_a_entrenar)
        elif accion == "Simular Ronda":
            generar_pares(entrenador, lista_entrenadores)
            resultado = liga_programon.simular_ronda(entrenador)
            if resultado == False:
                seguir_partida_actual = False
            else:
                for competidor in lista_entrenadores:
                    competidor.energia = 100
        elif accion == "Resumen Campeonato":
            liga_programon.resumen_campeonato()
        elif accion == "Crear Objeto":
            tipos_objetos = ["Baya", "Pocion", "Caramelo", "Volver", "Salir"]
            for i in range(5):
                print(f"[{i + 1}] {tipos_objetos[i]}")
            respuesta_valida = False
            while respuesta_valida == False:
                objeto_a_crear = input("¿Qué tipo de objeto te gustaría crear? ")
                print()
                if validar_respuesta(1, 5, objeto_a_crear) == True:
                    respuesta_valida = True
            objeto_a_crear = tipos_objetos[int(objeto_a_crear) - 1].lower()
            if objeto_a_crear == "baya":
                entrenador.crear_objeto("baya")
            elif objeto_a_crear == "pocion":
                entrenador.crear_objeto("pocion")
            elif objeto_a_crear == "caramelo":
                entrenador.crear_objeto("caramelo")
            elif objeto_a_crear == "volver":
                pass
            elif objeto_a_crear == "salir":
                pass
        elif accion == "Utilizar Objeto":
            if len(entrenador.objetos) == 0:
                print("No tienes objetos disponibles. Si quieres utilizar uno, debes ir" + \
                " a crearlos!\n")
            else:
                for i in range(len(entrenador.objetos)):
                    print(f"[{i + 1}] {entrenador.objetos[i].nombre}")
                respuesta_valida = False
                while respuesta_valida == False:
                    objeto_a_utilizar = input("¿Qué objeto te gustaría utilizar? ")
                    print()
                    if validar_respuesta(1, len(entrenador.objetos), objeto_a_utilizar) == True:
                        respuesta_valida = True
                objeto_a_utilizar = entrenador.objetos[int(objeto_a_utilizar) - 1]
                for j in range(len(entrenador.programones)):
                    print(f"[{j + 1}] {entrenador.programones[j].nombre}")
                respuesta_valida = False
                while respuesta_valida == False:
                    programon_a_aplicar = input(f"¿A qué programón te gustaría aplicarle: " + \
                    f"{objeto_a_utilizar.nombre}? ")
                    print()
                    if validar_respuesta(1, len(entrenador.programones), programon_a_aplicar) \
                         == True:
                        respuesta_valida = True
                programon_a_aplicar = entrenador.programones[int(programon_a_aplicar) - 1]
                objeto_a_utilizar.aplicar_objeto(programon_a_aplicar)
                entrenador.objetos.remove(objeto_a_utilizar)
        elif accion == "Estado Entrenador":
            entrenador.estado()
            respuesta_valida = False
            while respuesta_valida == False:
                respuesta = input("¿Qué deseas realizar? ")
                if respuesta == "1":
                    respuesta_valida = True
                elif respuesta == "2":
                    seguir_partida_actual = False
                    nueva_partida = False
                    respuesta_valida = True
                else:
                    print("Respuesta no válida")
        elif accion == "Volver":
            seguir_partida_actual = False
        elif accion == "Salir":
            seguir_partida_actual = False
            nueva_partida = False