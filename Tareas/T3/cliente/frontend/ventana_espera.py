from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer
from utils import data_json

window_name, base_class = uic.loadUiType("ventana_espera.ui")

class VentanaEspera(window_name, base_class):

    senal_volver_inicio = pyqtSignal()
    senal_actualizar_ventana_espera = pyqtSignal()
    senal_iniciar_partida = pyqtSignal()
    senal_inicio_partida = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.usuarios = []
        self.crear_elementos()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Espera")
        self.boton_volver.clicked.connect(self.volver_inicio)
        self.timer_espera = QTimer()
        self.timer_espera.activo = False
        self.timer_espera.setInterval(1000) #se actualiza cada 1 segundo
        self.timer_espera.timeout.connect(self.logica_timer)

    def logica_timer(self):
        if self.timer_espera.activo == False:
            self.timer_espera.activo = True
            self.timer_espera.start()
            self.contador_timer = data_json("CUENTA_REGRESIVA_INICIO")
            self.temporizador.setText(str(self.contador_timer))
        elif self.contador_timer == 0:
            self.timer_espera.stop()
            self.timer_espera.activo = False
            #enviar señal para empezar la partida
            self.senal_iniciar_partida.emit()
            self.senal_inicio_partida.emit()
        else:
            self.contador_timer -= 1
            self.temporizador.setText(str(self.contador_timer))
    
    def parar_timer(self):
        self.timer_espera.stop()
        self.timer_espera.activo = False

    def actualizar_nombres(self, diccionario):
        if "numero_usuario" in diccionario:
            if diccionario["numero_usuario"] == 1:
                self.jugador_1.setText(diccionario["nombre_usuario"])
            elif diccionario["numero_usuario"] == 2:
                self.jugador_2.setText(diccionario["nombre_usuario"])

    def volver_inicio(self):
        self.senal_volver_inicio.emit()

    def mostrar(self):
        self.show()
    
    def ocultar(self):
        self.hide()

    