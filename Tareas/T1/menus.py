from funciones import crear_lista_entrenadores
def menu_inicial() -> str:
    lista_entrenadores = crear_lista_entrenadores()
    print("*****   Menu de Inicio   *****")
    print("-"*30)
    for i in range(len(lista_entrenadores)):
        if type(lista_entrenadores[i][1]) == list: #los que tienen un solo programon, no son listas
            programones = ", ".join(lista_entrenadores[i][1])
        else:
            programones = lista_entrenadores[i][1]
        print(f"[{i+1}] {lista_entrenadores[i][0]}: {programones}")
    print(f"[{len(lista_entrenadores) + 1}] Salir")
    entrenador = input("¿Qué entrenador te gustaría escoger? ")
    entrenador_valido = False
    while entrenador_valido == False:
        if entrenador == str(len(lista_entrenadores) + 1):
            entrenador = "Salir"
            entrenador_valido = True
            return entrenador
        elif entrenador.isdigit() == True:
            if 1 <= int(entrenador) <= len(lista_entrenadores):
                entrenador = lista_entrenadores[int(entrenador) - 1][0]
                entrenador_valido = True
                return entrenador
            else:
                print("Número fuera de rango. Inténtelo nuevamente\n")
                entrenador = input("¿Qué entrenador te gustaría escoger? ")
        else:
            print("Respuesta no valida, debe ser un número. Por favor intentar nuevamente\n")
            entrenador = input("¿Qué entrenador te gustaría escoger? ")

def menu_entrenador() -> str:
    acciones = ["Entrenamiento", "Simular Ronda", "Resumen Campeonato", "Crear Objeto", 
    "Utilizar Objeto", "Estado Entrenador", "Volver", "Salir"]
    for i in range(len(acciones)):
        print(f"[{i + 1}] {acciones[i]}")
    accion = input("¿Qué acción te gustaría realizar? ")
    print()
    accion_valida = False
    while accion_valida == False:
        if accion == "8":
            accion = "Salir"
            accion_valida = True
            return accion
        elif accion == "7":
            accion = "Volver"
            accion_valida = True
            return accion
        elif accion.isdigit() == True:
            if 1 <= int(accion) <= 6:
                accion = acciones[int(accion) - 1]
                accion_valida = True
                return accion
            else:
                print("Número fuera de rango. Inténtelo nuevamente\n")
                accion = input("¿Qué acción te gustaría realizar? ")
        else:
            print("Respuesta no valida, debe ser un número. Por favor intentar nuevamente\n")
            accion = input("¿Qué acción te gustaría realizar? ")

