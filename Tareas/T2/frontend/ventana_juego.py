from PyQt5 import uic
import parametros as p
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont



window_name, base_class = uic.loadUiType("ventana_juego.ui")


class VentanaJuego(window_name, base_class):

    senal_mostrar_ventana_juego = pyqtSignal()
    senal_comprobar_creacion_planta = pyqtSignal(str, int, int) #tipo, fila y columna
    senal_tipo_mapa = pyqtSignal(str) # envía al backend el tipo de mapa
    senal_click_derecho = pyqtSignal(dict) #dict con coordenada x e y
    senal_tecla = pyqtSignal(str) # str de las teclas presionadas
    senal_pausa = pyqtSignal()
    senal_eliminar_elementos_backend = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timers, self.girasoles, self.input, self.tipo_mapa = [], [], [], ""
        self.crear_elementos()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Juego")
        self.setMaximumHeight(588)
        self.setMaximumWidth(1060)
        self.timer_final = QTimer(self)
        self.timer_final.timeout.connect(self.eliminar_elementos_backend)
        self.timer_final.setInterval(3000)
        self.timer_final.setSingleShot(True)

    def comprobar_mapa(self, mapa: str):
        if mapa == "Jardin abuela":
            self.tipo_mapa, self.fondo = "Jardin abuela", QLabel(self)
            self.senal_tipo_mapa.emit("Jardin abuela")
            pixeles = QPixmap(p.RUTA_FONDO_ABUELA)
            self.fondo.setPixmap(pixeles)
            self.fondo.setScaledContents(True)
            self.fondo.setGeometry(100, 0, 1221, 491)
            self.crear_cruz_y_texto()
            self.senal_mostrar_ventana_juego.emit()
        elif mapa == "Salida nocturna":
            self.tipo_mapa, self.fondo = "Salida nocturna", QLabel(self)
            self.senal_tipo_mapa.emit("Salida nocturna")
            pixeles = QPixmap(p.RUTA_FONDO_NOCTURNO)
            self.fondo.setPixmap(pixeles)
            self.fondo.setScaledContents(True)
            self.fondo.setGeometry(100, 0, 1221, 491)
            self.crear_cruz_y_texto()
            self.senal_mostrar_ventana_juego.emit()

    def crear_cruz_y_texto(self):
        self.cruz = QLabel(self)
        pixeles = QPixmap(p.RUTA_CRUZ)
        self.cruz.setPixmap(pixeles)
        self.cruz.setScaledContents(True)
        self.cruz.setGeometry(100, 310, 181, 181)
        self.cruz.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.notificar_plata = QLabel(self)
        self.notificar_plata.setText("")
        self.notificar_plata.setGeometry(340, 390, 331, 21)
        self.notificar_plata.setStyleSheet("background-color: rgba(255, 255, 255, 0); color: rgb(254, 252, 255);")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if 320 < event.x() < 385 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 0)
            elif 385 < event.x() < 450 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 1)
            elif 450 < event.x() < 515 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 2)
            elif 515 < event.x() < 580 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 3)
            elif 580 < event.x() < 645 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 4)
            elif 645 < event.x() < 710 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 5)
            elif 710 < event.x() < 775 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 6)
            elif 775 < event.x() < 840 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 7)
            elif 840 < event.x() < 905 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 8)
            elif 905 < event.x() < 970 and 170 < event.y() < 250:
                self.intentar_crear_planta(0, 9)
            elif 320 < event.x() < 385 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 0)
            elif 385 < event.x() < 450 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 1)
            elif 450 < event.x() < 515 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 2)
            elif 515 < event.x() < 580 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 3)
            elif 580 < event.x() < 645 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 4)
            elif 645 < event.x() < 710 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 5)
            elif 710 < event.x() < 775 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 6)
            elif 775 < event.x() < 840 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 7)
            elif 840 < event.x() < 905 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 8)
            elif 905 < event.x() < 970 and 250 < event.y() < 330:
                self.intentar_crear_planta(1, 9)
        elif event.button() == Qt.RightButton:
            diccionario = {"coordenada_x": event.x(), "coordenada_y": event.y()}
            self.senal_click_derecho.emit(diccionario)

    def keyPressEvent(self, event):
        input = event.text()
        input = input.lower()
        if input == "p":
            self.senal_pausa.emit()
        elif len(self.input) < 3:
            self.input.append(input)
        else:
            self.input.pop(0)
            self.input.append(input)
            enviar = "".join(self.input)
            if "p" in enviar:
                self.senal_pausa.emit()
            else:
                self.senal_tecla.emit(enviar)

    def actualizar_datos_pantalla(self, diccionario: dict):
        self.n_soles.setText(str(diccionario["soles"]))
        self.nivel.setText(str(diccionario["nivel"]))
        self.puntaje.setText(str(diccionario["puntaje"]))
        self.nivel.setText(str(diccionario["nivel"]))
        self.z_destruidos.setText(str(diccionario["destruidos"]))
        self.z_restantes.setText(str(diccionario["restantes"]))
        self.cruz.show()
        self.crear_mensaje_derrota()
        self.crear_mensaje_victoria()

    def mostrar_sol(self, diccionario: dict):
        sol = diccionario["instancia"]
        sol.imagen.setParent(self)
        sol.imagen.show()
    
    def esconder_sol(self, diccionario: dict):
        sol = diccionario["instancia"]
        sol.imagen.setParent(self)
        sol.imagen.hide()

    def intentar_crear_planta(self, fila: int, columna: int):
        if self.boton_girasol.isChecked() == True:
            self.senal_comprobar_creacion_planta.emit("girasol", fila, columna)
        elif self.boton_clasica.isChecked() == True:
            self.senal_comprobar_creacion_planta.emit("clásica", fila, columna)
        elif self.boton_azul.isChecked() == True:
            self.senal_comprobar_creacion_planta.emit("azul", fila, columna)
        elif self.boton_papa.isChecked() == True:
            self.senal_comprobar_creacion_planta.emit("papa", fila, columna)
    
    def notificar_falta_de_soles(self, notificar: bool):
        if notificar == True:
            self.notificar_plata.setText("No tienes los soles necesarios para comprar la planta")
        else:
            self.notificar_plata.setText("")

    def loop_movimiento_girasol(self, diccionario: dict):
        girasol = diccionario["instancia"]
        girasol.pos_1.setParent(self)
        girasol.pos_2.setParent(self)
        if girasol.timer_movimiento.contador == 1:
            girasol.pos_2.hide()
            girasol.pos_1.show()
            girasol.timer_movimiento.contador += 1
        elif girasol.timer_movimiento.contador == 2:
            girasol.pos_1.hide()
            girasol.pos_2.show()
            girasol.timer_movimiento.contador -= 1

    def loop_movimiento_azul(self, diccionario: dict):
        azul = diccionario["instancia"]
        azul.pos_1.setParent(self)
        azul.pos_2.setParent(self)
        azul.pos_3.setParent(self)
        if azul.timer_movimiento.contador == 1:
            azul.pos_3.hide()
            azul.pos_1.show()
            azul.timer_movimiento.contador += 1
        elif azul.timer_movimiento.contador == 2:
            azul.pos_1.hide()
            azul.pos_2.show()
            azul.timer_movimiento.contador += 1
        elif azul.timer_movimiento.contador == 3:
            azul.pos_2.hide()
            azul.pos_3.show()
            azul.timer_movimiento.contador -= 2
    
    def loop_movimiento_clasica(self, diccionario: dict):
        clasica = diccionario["instancia"]
        clasica.pos_1.setParent(self)
        clasica.pos_2.setParent(self)
        clasica.pos_3.setParent(self)
        if clasica.timer_movimiento.contador == 1:
            clasica.pos_3.hide()
            clasica.pos_1.show()
            clasica.timer_movimiento.contador += 1
        elif clasica.timer_movimiento.contador == 2:
            clasica.pos_1.hide()
            clasica.pos_2.show()
            clasica.timer_movimiento.contador += 1
        elif clasica.timer_movimiento.contador == 3:
            clasica.pos_2.hide()
            clasica.pos_3.show()
            clasica.timer_movimiento.contador -= 2

    def movimiento_papa(self, diccionario: dict):
        papa = diccionario["instancia"]
        papa.pos_1.setParent(self)
        papa.pos_2.setParent(self)
        papa.pos_3.setParent(self)
        if papa.contador_imagen_actual == 1:
            papa.pos_1.show()
        elif papa.contador_imagen_actual == 2:
            papa.pos_1.hide()
            papa.pos_2.show()
        elif papa.contador_imagen_actual == 3:
            papa.pos_2.hide()
            papa.pos_3.show()
        elif papa.contador_imagen_actual == 0:
            papa.pos_3.hide()

    def ocultar_planta(self, diccionario: dict):
        planta = diccionario["instancia"]
        if planta.tipo == "girasol":
            planta.pos_1.setParent(self)
            planta.pos_2.setParent(self)
            planta.pos_1.hide()
            planta.pos_2.hide()
        else:
            planta.pos_1.setParent(self)
            planta.pos_2.setParent(self)
            planta.pos_3.setParent(self)
            planta.pos_1.hide()
            planta.pos_2.hide()
            planta.pos_3.hide()

    def loop_caminar(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.caminar_1.setParent(self)
        zombie.caminar_2.setParent(self)
        if zombie.timer_caminar.contador == 1:
            zombie.caminar_2.hide()
            zombie.caminar_1.show()
            zombie.timer_caminar.contador += 1
        elif zombie.timer_caminar.contador == 2:
            zombie.caminar_1.hide()
            zombie.caminar_2.show()
            zombie.timer_caminar.contador -= 1
    
    def ocultar_zombie_caminar(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.caminar_1.setParent(self)
        zombie.caminar_2.setParent(self)
        zombie.caminar_1.hide()
        zombie.caminar_2.hide()
        zombie.comer_3.setParent(self)
        zombie.comer_3.show()
    
    def ocultar_zombie_comer(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.comer_1.setParent(self)
        zombie.comer_2.setParent(self)
        zombie.comer_3.setParent(self)
        zombie.comer_1.hide()
        zombie.comer_2.hide()
        zombie.caminar_2.setParent(self)
        zombie.caminar_2.show()
        
    def ocultar_zombie(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.comer_1.setParent(self)
        zombie.comer_2.setParent(self)
        zombie.comer_3.setParent(self)
        zombie.caminar_1.setParent(self)
        zombie.caminar_2.setParent(self)
        zombie.comer_1.hide()
        zombie.comer_2.hide()
        zombie.comer_3.hide()
        zombie.caminar_1.hide()
        zombie.caminar_2.hide()

    def loop_comer(self, diccionario: dict):
        zombie = diccionario["instancia"]
        zombie.comer_1.setParent(self)
        zombie.comer_2.setParent(self)
        zombie.comer_3.setParent(self)
        if zombie.timer_comer.contador == 1:
            zombie.comer_3.hide()
            zombie.comer_1.show()
            zombie.timer_comer.contador += 1
        elif zombie.timer_comer.contador == 2:
            zombie.comer_1.hide()
            zombie.comer_2.show()
            zombie.timer_comer.contador += 1
        elif zombie.timer_comer.contador == 3:
            zombie.comer_2.hide()
            zombie.comer_3.show()
            zombie.timer_comer.contador -= 2
    
    def movimiento_disparo_guisante(self, diccionario: dict):
        guisante = diccionario["instancia"]
        guisante.disparado.setParent(self)
        guisante.impacto1.setParent(self)
        guisante.impacto2.setParent(self)
        if guisante.impacto == False:
            guisante.disparado.show()  
        elif guisante.impacto == True: 
            if guisante.timer_movimiento.contador == 1:
                guisante.disparado.hide()
                guisante.impacto1.show()
                guisante.timer_movimiento.contador += 1
            elif guisante.timer_movimiento.contador == 2:
                guisante.impacto1.hide()
                guisante.impacto2.show()
                guisante.timer_movimiento.contador += 1
            elif guisante.timer_movimiento.contador == 3:
                guisante.impacto2.hide()
    
    def ocultar_guisante(self, diccionario: dict):
        guisante = diccionario["instancia"]
        guisante.disparado.setParent(self)
        guisante.impacto1.setParent(self)
        guisante.impacto2.setParent(self)
        guisante.disparado.hide()
        guisante.impacto1.hide()
        guisante.impacto2.hide()

    def ocultar_ventana(self, diccionario: dict):
        lista_plantas, lista_girasoles= diccionario["plantas"], diccionario["girasoles"]
        lista_papas, lista_guisantes = diccionario["papas"], diccionario["guisantes"]
        lista_soles, lista_zombies = diccionario["soles"], diccionario["zombies"]
        for zombie in lista_zombies:
            self.ocultar_zombie({"instancia": zombie})
        for planta in lista_plantas:
            self.ocultar_planta({"instancia": planta})
        for girasol in lista_girasoles:
            self.ocultar_planta({"instancia": girasol})
        for papa in lista_papas:
            self.ocultar_planta({"instancia": papa})
        for sol in lista_soles:
            self.esconder_sol({"instancia": sol})
        for guisante in lista_guisantes:
            self.ocultar_guisante({"instancia": guisante})
        self.hide()
    
    def crear_mensaje_victoria(self):
        self.cruz_victoria = QLabel(self)
        pixeles = QPixmap(p.RUTA_CRUZ)
        self.cruz_victoria.setPixmap(pixeles)
        self.cruz_victoria.setScaledContents(True)
        self.cruz_victoria.setGeometry(250, 250, 241, 241)
        self.cruz_victoria.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.cruz_victoria.hide()
        self.texto_victoria = QLabel(self)
        self.texto_victoria.setText("¡Me has salvado!")
        self.texto_victoria.setGeometry(440, 180, 281, 171)
        self.texto_victoria.setStyleSheet("background-color: rgb(157, 233, 165);")
        self.texto_victoria.setFont(QFont("arial", 31))
        self.texto_victoria.wordWrap()
        self.texto_victoria.hide()

    def crear_mensaje_derrota(self):
        self.derrota = QLabel(self)
        pixeles = QPixmap(p.RUTA_BRAINS)
        self.derrota.setPixmap(pixeles)
        self.derrota.setScaledContents(True)
        self.derrota.setGeometry(370, 70, 521, 361)
        self.derrota.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.derrota.hide()

    def mensaje_final_cruz(self, victoria: bool):
        self.cruz.hide()
        if victoria == True:
            self.crear_mensaje_victoria()
            self.cruz_victoria.show()
            self.texto_victoria.show()
        else:
            self.crear_mensaje_derrota()
            self.derrota.show()
        self.timer_final.start()
    
    def eliminar_elementos_backend(self):
        self.senal_eliminar_elementos_backend.emit()
        self.derrota.hide()
        self.cruz_victoria.hide()
        self.texto_victoria.hide()
        self.hide()
    def mostrar_ventana(self):
        self.show()