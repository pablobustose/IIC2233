from random import randint
from entrenador import Entrenador
from funciones import validar_respuesta, generar_pares


class LigaProgramon():
    def __init__(self, entrenadores: list):
        self.entrenadores = entrenadores
        self.perdedores = []
        self.ronda_actual = 1
        self.campeon = ""
        self.entrenadores_iniciales = []
        for entrenador in self.entrenadores:
            self.entrenadores_iniciales.append(entrenador.nombre)
    
    def resumen_campeonato(self):
        print("--------------- Resumen campeonato ---------------")
        print("Participantes:")
        for entrenador in self.entrenadores_iniciales:
            print(entrenador)
        print(f"\nRonda actual: {self.ronda_actual}\n")
        print("Entrenadores que siguen en competencia:")
        for entrenador in self.entrenadores:
            if entrenador not in self.perdedores:
                print(entrenador.nombre)
        print()

    def simular_ronda(self, entrenador: Entrenador) -> bool: #True si gana y false si pierda
        self.ronda_actual += 1
        for i in range(len(entrenador.programones)):
            print(f"[{i + 1}] {entrenador.programones[i].nombre}")
        respuesta_valida = False
        while respuesta_valida == False:
            programon_a_luchar = input("¿Con cual programón te gustaría luchar? ")
            print()
            if validar_respuesta(1, len(entrenador.programones), programon_a_luchar) == True:
                respuesta_valida = True
        programon_a_luchar = entrenador.programones[int(programon_a_luchar) - 1]
        print(f"Haz seleccionado a {programon_a_luchar.nombre} para luchar\n")
        lista_pares = generar_pares(entrenador, self.entrenadores)
        rival_usuario = lista_pares[0][1]
        programon_rival_usuario = randint(0,len(rival_usuario.programones) - 1)
        programon_rival_usuario = rival_usuario.programones[programon_rival_usuario]
        print(f"{entrenador.nombre} usando al programón {programon_a_luchar.nombre}, se enfren" + \
               f"ta a {rival_usuario.nombre} usando al programón {programon_rival_usuario.nombre}")
        resultado = programon_a_luchar.luchar(programon_rival_usuario)
        if resultado == True:
            print(f"{entrenador.nombre} ha ganado la batalla.")
            self.entrenadores.remove(rival_usuario)
        else:
            print(f"{rival_usuario.nombre} ha ganado la batalla.")
            self.entrenadores.remove(entrenador)
            print(f"Haz perdido el campeonato") 
            return False
        lista_pares.pop(0) #elimina el combate del usuario para que no sea ejecutado nuevamente
        for combate in lista_pares:
            entrenador1 = combate[0]
            entrenador2 = combate[1]
            programon_entrenador1 = randint(0,len(entrenador1.programones) - 1)
            programon_entrenador1 = entrenador1.programones[programon_entrenador1]
            programon_entrenador2 = randint(0,len(entrenador2.programones) - 1)
            programon_entrenador2 = entrenador2.programones[programon_entrenador2]
            print(f"{entrenador1.nombre} usando al programón {programon_entrenador1.nombre}," + \
                f" se enfrenta a {entrenador2.nombre} usando al " + \
                f"programón {programon_entrenador2.nombre}")
            resultado = programon_entrenador1.luchar(programon_entrenador2)
            if resultado == True:
                print(f"{entrenador1.nombre} ha ganado la batalla.")
                self.entrenadores.remove(entrenador2)
            else:
                print(f"{entrenador2.nombre} ha ganado la batalla.")
                self.entrenadores.remove(entrenador1)
        return True

