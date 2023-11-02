from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.zombies import ZombieLento, ZombieRapido
import parametros as p
from backend.plantas import Guisante, GuisanteAzul, PlantaClasica, PlantaAzul, Girasol, Papa, Sol
from random import randint
from backend.aparicion_zombies import intervalo_aparicion

class LogicaJuego(QObject):

    senal_actualizar_datos = pyqtSignal(dict) #dict con n_soles, nivel, puntaje, zombies destruidos y restantes
    senal_enviar_movimiento_girasol = pyqtSignal(dict) # dict con instancia de girasol
    senal_enviar_movimiento_azul = pyqtSignal(dict) # dict con instancia de azul
    senal_enviar_movimiento_clasica = pyqtSignal(dict) # dict con instancia de clásica
    senal_enviar_movimiento_papa = pyqtSignal(dict) # dict con instancia de papa
    senal_enviar_caminar = pyqtSignal(dict) # dict con instancia de zombie
    senal_enviar_comer = pyqtSignal(dict) # dict con instancia de zombie
    senal_enviar_nuevo_sol = pyqtSignal(dict) # dict con instancia de sol
    senal_ocultar_imagenes_caminar = pyqtSignal(dict) # dict con instancia de clase
    senal_ocultar_imagenes_comer = pyqtSignal(dict) # dict con instancia de clase
    senal_ocultar_planta = pyqtSignal(dict) # dict con instancia de clase
    senal_enviar_movimiento_guisante = pyqtSignal(dict) # dict con instancia de clase
    senal_esconder_sol = pyqtSignal(dict) # dict con instancia de clase
    senal_ocular_zombie = pyqtSignal(dict) # dict con instancia de clase
    senal_finalizar_ronda = pyqtSignal(dict) # dict con la info para post_ronda
    senal_mostrar_ventana = pyqtSignal()
    senal_ocultar_elementos_y_ventana = pyqtSignal(dict) # dict con las instancias de cada clase
    senal_falta_plata = pyqtSignal(bool) #True si falta plata y false si se puede comprar
    senal_mostrar_mensaje_final = pyqtSignal(bool) #True si ganó y False si perdió

    def __init__(self):
        super().__init__()
        self.posiciones = [["", "", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", "", ""]]
        self.zombies = []
        self.girasoles = []
        self.papas = []
        self.plantas_que_disparan = []
        self.instancias_soles = []
        self.guisantes = []
        self.soles = p.SOLES_INICIALES
        self.nivel = 0
        self.puntaje = 0
        self.puntaje_total = 0
        self.zombies_destruidos = 0
        self.zombies_restantes = 0
        self.ronda_actual = 0
        self.ronda_en_curso = False
        self.victoria = False
        self.n_zombies_f1 = p.N_ZOMBIES
        self.n_zombies_f2 = p.N_ZOMBIES
        self.pausa_actual = False
        self.actualizar_datos()

    def nombre_usuario(self, nombre: str):
        self.nombre = nombre

    def tipo_mapa(self, tipo: str):
        if tipo == "Jardin abuela":
            self.mapa = "Jardin abuela"
            self.ponderador = p.PONDERADOR_DIURNO
        elif tipo == "Salida nocturna":
            self.mapa = "Salida nocturna"
            self.ponderador = p.PONDERADOR_NOCTURNO

    def nueva_ronda(self):
        self.eliminar_elementos()
        self.soles, self.zombies_destruidos, self.puntaje = p.SOLES_INICIALES, 0, 0
        self.actualizar_datos()
        self.senal_mostrar_ventana.emit()

    def iniciar_ronda(self):
        if self.ronda_en_curso == False:
            self.ronda_en_curso = True
            self.ronda_actual += 1
            self.zombies_restantes = 2 * p.N_ZOMBIES
            self.n_zombies_f1, self.n_zombies_f2 = p.N_ZOMBIES, p.N_ZOMBIES
            self.actualizar_datos() #actualizar datos
            self.iniciar_movimientos()#iniciar plantas movimiento, soles y disparo
            self.timer_aparicion_soles = QTimer() #iniciar aparicion de soles random
            self.timer_aparicion_soles.timeout.connect(self.crear_soles_aleatorios)
            self.timer_aparicion_soles.setInterval(p.INTERVALO_APARICION_SOLES)
            self.timer_aparicion_soles.start()
            intervalo = int(intervalo_aparicion(self.ronda_actual, self.ponderador) * 10000)
            self.timer_aparicion_zombies = QTimer() #iniciar aparicion zombies (con su respectivo intervalo)
            self.timer_aparicion_zombies.timeout.connect(self.crear_instancia_zombie)
            self.timer_aparicion_zombies.setInterval(intervalo)
            self.timer_aparicion_zombies.start()

    def iniciar_movimientos(self):
        for girasol in self.girasoles:
            girasol.timer_movimiento.start()
            girasol.timer_soles.start()
        for planta in self.plantas_que_disparan:
            planta.timer_movimiento.start()
            planta.timer_disparo.start()
        for zombie in self.zombies:
            zombie.timer_caminar.start()
            zombie.timer_comer.start()
        for guisante in self.guisantes:
            guisante.timer_movimiento.start()
    
    def pausar_movimientos(self):
        for girasol in self.girasoles:
            girasol.timer_movimiento.stop()
            girasol.timer_soles.stop()
        for planta in self.plantas_que_disparan:
            planta.timer_movimiento.stop()
            planta.timer_disparo.stop()
        for zombie in self.zombies:
            zombie.timer_caminar.stop()
            zombie.timer_comer.stop()
        for guisante in self.guisantes:
            guisante.timer_movimiento.stop()

    def pausa(self):
        if self.ronda_en_curso == True:
            self.pausa_actual = True
            self.ronda_en_curso = False
            self.pausar_movimientos()
            self.timer_aparicion_soles.stop()
            self.timer_aparicion_zombies.stop()
        elif self.ronda_en_curso == False:
            self.pausa_actual = False
            self.ronda_en_curso = True
            self.iniciar_movimientos()
            self.timer_aparicion_soles.start()
            self.timer_aparicion_zombies.start()
    
    def actualizar_datos(self):
        diccionario = {"soles": self.soles, "nivel": self.nivel, "puntaje": self.puntaje, 
            "destruidos": self.zombies_destruidos, "restantes": self.zombies_restantes}
        self.senal_actualizar_datos.emit(diccionario)

    def checkear_cheatcodes(self, input: str):
        if input == p.CHEATCODE_SOLES_EXTRA:
            self.soles += p.SOLES_EXTRA
            self.actualizar_datos()
        elif input == p.CHEATCODE_KILL_ZOMBIES:
            for zombie in self.zombies:
                zombie.vida = 0
                self.zombies_destruidos += 1
            self.zombies_restantes = 0
            self.actualizar_datos()
            self.finalizar_ronda()

    def comprobar_creacion_planta(self, tipo: str, fila: int, columna: int):
        if self.pausa_actual == False:
            if self.posiciones[fila][columna] == "":
                if tipo == "girasol" and self.soles >= p.COSTO_GIRASOL:
                    self.crear_instancia_planta(tipo, fila, columna)
                    self.soles -= p.COSTO_GIRASOL
                    self.senal_falta_plata.emit(False)
                elif tipo == "clásica" and self.soles >= p.COSTO_LANZAGUISANTE:
                    self.crear_instancia_planta(tipo, fila, columna)
                    self.soles -= p.COSTO_LANZAGUISANTE
                    self.senal_falta_plata.emit(False)
                elif tipo == "azul" and self.soles >= p.COSTO_LANZAGUISANTE_HIELO:
                    self.crear_instancia_planta(tipo, fila, columna)
                    self.soles -= p.COSTO_LANZAGUISANTE_HIELO
                    self.senal_falta_plata.emit(False)
                elif tipo == "papa" and self.soles >= p.COSTO_PAPA:
                    self.crear_instancia_planta(tipo, fila, columna)
                    self.soles -= p.COSTO_PAPA
                    self.senal_falta_plata.emit(False)
                else:
                    self.senal_falta_plata.emit(True)
        self.actualizar_datos()

    def crear_instancia_planta(self, tipo, fila: int, columna: int):
        if tipo == "clásica" and self.posiciones[fila][columna] == "":
            nueva_planta = PlantaClasica(fila, columna)
            self.posiciones[fila][columna] = nueva_planta
            nueva_planta.senal_movimiento_clasica.connect(self.movimiento_clasica)
            nueva_planta.senal_movimiento_clasica.emit({"instancia": nueva_planta})
            nueva_planta.senal_crear_guisante.connect(self.crear_guisante)
            self.plantas_que_disparan.append(nueva_planta)
            if self.ronda_en_curso == True:
                nueva_planta.timer_movimiento.start()
                nueva_planta.timer_disparo.start()
        elif tipo == "azul" and self.posiciones[fila][columna] == "":
            nueva_planta = PlantaAzul(fila, columna)
            self.posiciones[fila][columna] = nueva_planta  
            nueva_planta.senal_movimiento_azul.connect(self.movimiento_azul) #conexión entre instancia y logica_juego
            nueva_planta.senal_movimiento_azul.emit({"instancia": nueva_planta})
            nueva_planta.senal_crear_guisante_azul.connect(self.crear_guisante_azul)
            self.plantas_que_disparan.append(nueva_planta)
            if self.ronda_en_curso == True:
                nueva_planta.timer_movimiento.start()
                nueva_planta.timer_disparo.start()
        elif tipo == "girasol" and self.posiciones[fila][columna] == "":
            nueva_planta = Girasol(fila, columna)
            self.posiciones[fila][columna] = nueva_planta  
            nueva_planta.senal_movimiento_girasol.connect(self.movimiento_girasoles) #conexión entre instancia y logica_juego
            nueva_planta.senal_movimiento_girasol.emit({"instancia": nueva_planta})
            nueva_planta.senal_crear_sol.connect(self.crear_soles_girasol)
            self.girasoles.append(nueva_planta)
            if self.ronda_en_curso == True:
                nueva_planta.timer_movimiento.start()
                nueva_planta.timer_soles.start()
        elif tipo == "papa" and self.posiciones[fila][columna] == "":
            nueva_planta = Papa(fila, columna)
            self.posiciones[fila][columna] = nueva_planta
            nueva_planta.senal_movimiento_papa.connect(self.movimiento_papa) #conexión entre instancia y logica_juego
            nueva_planta.senal_movimiento_papa.emit({"instancia": nueva_planta})
            self.papas.append(nueva_planta)
    
    def crear_instancia_zombie(self): 
        if self.zombies_restantes > 0:
            tipo = randint(0,1) #0 es lento y 1 es rápido
            if self.n_zombies_f1 > 0 and self.n_zombies_f2 > 0:
                fila = randint(0,1)
                if fila == 0:
                    self.n_zombies_f1 -= 1
                else:
                    self.n_zombies_f2 -= 1
            elif self.n_zombies_f1 == 0:
                fila = 1
            elif self.n_zombies_f2 == 0:
                fila = 0
            if tipo == 0:
                nuevo_zombie = ZombieLento(fila)
                self.zombies.append(nuevo_zombie)
                nuevo_zombie.senal_caminar_zombie_lento.connect(self.caminar_zombie) #conexión entre instancia y logica_juego
                nuevo_zombie.senal_morder_lento.connect(self.comer_zombie) #conexión entre instancia y logica_juego
                nuevo_zombie.senal_muerte_zombie_lento.connect(self.muerte_zombie)
                self.zombies_restantes -= 1
            elif tipo == 1:
                nuevo_zombie = ZombieRapido(fila)
                self.zombies.append(nuevo_zombie)
                nuevo_zombie.senal_caminar_zombie_rapido.connect(self.caminar_zombie) #conexión entre instancia y logica_juego
                nuevo_zombie.senal_morder_rapido.connect(self.comer_zombie) #conexión entre instancia y logica_juego
                nuevo_zombie.senal_muerte_zombie_rapido.connect(self.muerte_zombie)
                self.zombies_restantes -= 1
            self.actualizar_datos()

    def crear_soles_aleatorios(self):
        if self.mapa == "Jardin abuela":
            coordenada_x, coordenada_y = randint(330, 950), randint(0, 430)
            nuevo_sol = Sol(coordenada_x, coordenada_y)
            self.instancias_soles.append(nuevo_sol)
            self.senal_enviar_nuevo_sol.emit({"instancia": nuevo_sol})
    
    def crear_soles_girasol(self, diccionario: dict):
        for i in range(p.CANTIDAD_SOLES):
            coordenada_x, coordenada_y = diccionario["coordenada_x"], diccionario["coordenada_y"]
            suma_coordenada_x, suma_coordenada_y = randint(-30, 60), randint(-30, 60)
            nuevo_sol = Sol(coordenada_x + suma_coordenada_x, coordenada_y + suma_coordenada_y)
            self.instancias_soles.append(nuevo_sol)
            self.senal_enviar_nuevo_sol.emit({"instancia": nuevo_sol})

    def movimiento_girasoles(self, diccionario: dict):
        girasol = diccionario["instancia"]
        self.senal_enviar_movimiento_girasol.emit({"instancia": girasol})
    
    def movimiento_azul(self, diccionario:dict):
        azul = diccionario["instancia"]
        self.senal_enviar_movimiento_azul.emit({"instancia": azul})
    
    def movimiento_clasica(self, diccionario:dict):
        clasica = diccionario["instancia"]
        self.senal_enviar_movimiento_clasica.emit({"instancia": clasica})

    def movimiento_guisante(self, diccionario:dict):
        guisante = diccionario["instancia"]
        for zombie in self.zombies:
            if zombie.coordenada_x == guisante.coordenada_x and zombie.coordenada_y == (guisante.coordenada_y - 5):
                if guisante.impacto == False:
                    guisante.impacto = True
                    zombie.vida -= p.DANO_PROYECTIL
                    if guisante.tipo == "azul" and zombie.relentizado == False:
                        zombie.relentizado = True
                        nuevo_intervalo = int(zombie.timer_caminar.interval() * (1 + p.RALENTIZAR_ZOMBIE))
                        zombie.timer_caminar.setInterval(nuevo_intervalo)
        if guisante.impacto == False:
            guisante.coordenada_x += 13
            guisante.disparado.move(guisante.coordenada_x, guisante.coordenada_y)
            guisante.impacto1.move(guisante.coordenada_x, guisante.coordenada_y)
            guisante.impacto2.move(guisante.coordenada_x, guisante.coordenada_y)
        self.senal_enviar_movimiento_guisante.emit({"instancia": guisante})

    def movimiento_papa(self, diccionario:dict):
        papa = diccionario["instancia"]
        self.senal_enviar_movimiento_papa.emit({"instancia": papa})
    
    def caminar_zombie(self, diccionario: dict):
        zombie = diccionario["instancia"]
        if self.posiciones[zombie.fila][zombie.proxima_coordenada] == "": #comprobar que no haya planta
            zombie.coordenada_x -= 13
            if zombie.coordenada_x < 320:
                self.finalizar_ronda() #perdió
            elif (zombie.coordenada_x - 320) % 65 == 0: #actualiza cual es la casilla próxima en el caso que ya adelantó una
                zombie.proxima_coordenada -= 1
            zombie.caminar_1.move(zombie.coordenada_x, zombie.coordenada_y)
            zombie.caminar_2.move(zombie.coordenada_x, zombie.coordenada_y)
            zombie.comer_1.move(zombie.coordenada_x, zombie.coordenada_y)
            zombie.comer_2.move(zombie.coordenada_x, zombie.coordenada_y)
            zombie.comer_3.move(zombie.coordenada_x, zombie.coordenada_y)
            self.senal_enviar_caminar.emit({"instancia": zombie})
        else:
            self.senal_ocultar_imagenes_caminar.emit({"instancia": zombie}) #para ocultar las imagenes de caminar
            zombie.timer_comer.contador = 1
            zombie.timer_caminar.stop()
            zombie.timer_comer.start()
            
    def comer_zombie(self, diccionario: dict):
        zombie = diccionario["instancia"]
        coordenada_planta = zombie.proxima_coordenada
        planta_a_morder = self.posiciones[zombie.fila][coordenada_planta]
        if planta_a_morder != "": #si hay una planta en la posición...
            if planta_a_morder.vida > 0:
                planta_a_morder.vida -= zombie.dano_mordida
                self.senal_enviar_comer.emit({"instancia": zombie})
            elif planta_a_morder.vida <= 0:
                self.posiciones[zombie.fila][coordenada_planta] = ""
                if planta_a_morder in self.girasoles:
                    self.girasoles.remove(planta_a_morder)
                elif planta_a_morder in self.plantas_que_disparan:
                    self.plantas_que_disparan.remove(planta_a_morder)
                elif planta_a_morder in self.papas:
                    self.papas.remove(planta_a_morder)
                self.senal_ocultar_planta.emit({"instancia": planta_a_morder})
                self.senal_ocultar_imagenes_comer.emit({"instancia": zombie}) #para ocultar las imagenes de comer
                zombie.timer_caminar.contador = 1
                zombie.timer_comer.stop()
                zombie.timer_caminar.start()
        else:
            self.senal_ocultar_imagenes_comer.emit({"instancia": zombie}) #para ocultar las imagenes de comer
            zombie.timer_comer.stop()
            zombie.timer_caminar.start()


    def muerte_zombie(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.timer_caminar.stop()
        zombie.timer_comer.stop()
        self.senal_ocular_zombie.emit({"instancia": zombie})
        self.zombies_destruidos += 1
        self.zombies.remove(zombie)
        if self.mapa == "Jardin abuela":
            self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
        elif self.mapa == "Salida nocturna":
            self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
        self.actualizar_datos()
        if self.zombies_destruidos == (2 * p.N_ZOMBIES): #si es que gana...
            puntaje_extra = self.puntaje * self.ponderador
            self.puntaje += puntaje_extra
            self.victoria = True
            self.finalizar_ronda()

    def crear_guisante(self, diccionario: dict):
        planta = diccionario["instancia"]
        guisante = Guisante(planta.coordenada_x + 65, planta.coordenada_y + 5)
        self.guisantes.append(guisante)
        guisante.senal_movimiento_guisante.connect(self.movimiento_guisante)

    def crear_guisante_azul(self, diccionario: dict):
        planta = diccionario["instancia"]
        guisante = GuisanteAzul(planta.coordenada_x + 65, planta.coordenada_y + 5)
        self.guisantes.append(guisante)
        guisante.senal_movimiento_guisante_azul.connect(self.movimiento_guisante)

    def comprobar_click_sol(self, diccionario:dict):
        coordenada_x, coordenada_y = diccionario["coordenada_x"], diccionario["coordenada_y"]
        for sol in self.instancias_soles:
            if sol.coordenada_x <= coordenada_x <= (sol.coordenada_x + 40): 
                if sol.coordenada_y <= coordenada_y <= (sol.coordenada_y + 40):
                    if self.mapa == "Jardin abuela":
                        self.soles += 2 * p.SOLES_POR_RECOLECCION
                        self.instancias_soles.remove(sol)
                    elif self.mapa == "Salida nocturna":
                        self.soles += p.SOLES_POR_RECOLECCION
                        self.instancias_soles.remove(sol)
                    self.senal_esconder_sol.emit({"instancia": sol})
                    self.actualizar_datos()

    def intentar_avanzar_ronda(self):
        if self.soles >= p.COSTO_AVANZAR:
            self.soles -= p.COSTO_AVANZAR
            self.victoria = True
            self.finalizar_ronda()

    def eliminar_elementos(self):
        diccionario = {"zombies": self.zombies,"plantas": self.plantas_que_disparan, "girasoles": self.girasoles, "papas": self.papas, "guisantes": self.guisantes, "soles": self.instancias_soles}
        self.senal_ocultar_elementos_y_ventana.emit(diccionario)
        self.plantas_que_disparan, self.girasoles, self.papas, self.guisantes, self.instancias_soles, self.zombies = [], [], [], [], [], []
        self.posiciones = [["", "", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", "", ""]]
        diccionario = {"ronda actual": self.ronda_actual, "soles restantes": self.soles, "zombies destruidos": self.zombies_destruidos, "puntaje ronda": self.puntaje, "puntaje total": self.puntaje_total, "victoria": self.victoria}
        self.senal_finalizar_ronda.emit(diccionario)

    def finalizar_ronda(self):
        self.puntaje_total += self.puntaje
        if self.ronda_en_curso == True:
            self.timer_aparicion_zombies.stop()
            self.timer_aparicion_soles.stop()
        self.ronda_en_curso = False
        if self.victoria == False:
            self.guardar_puntaje()
            self.senal_mostrar_mensaje_final.emit(False)
        else:
            self.senal_mostrar_mensaje_final.emit(True)
    
    def guardar_puntaje(self):
        self.ronda_actual = 0
        archivo = open("puntajes.txt", "a")
        archivo.write(f"\n{self.nombre},{self.puntaje_total}")
        archivo.close()