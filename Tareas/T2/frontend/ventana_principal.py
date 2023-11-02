from PyQt5 import uic
import parametros as p
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventana_principal.ui")

class VentanaPrincipal(window_name, base_class):

    senal_enviar_mapa = pyqtSignal(str)
    senal_enviar_nombre_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crear_elementos()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Principal")
        self.setStyleSheet("VentanaPrincipal{background-image: url("f"{p.RUTA_FONDO}"")}")
        self.setMaximumHeight(516)
        self.setMinimumHeight(516)
        self.setMaximumWidth(800)
        self.setMinimumWidth(800)

        self.boton_iniciar_juego.clicked.connect(self.enviar_mapa)

    def enviar_mapa(self):
        if self.boton_jardin_abuela.isChecked() == True:
            self.senal_enviar_mapa.emit("Jardin abuela")
            self.hide()
        elif self.boton_salida_nocturna.isChecked() == True:
            self.senal_enviar_mapa.emit("Salida nocturna")
            self.hide()

    def mostrar_ventana(self, usuario):
        self.show()
        self.senal_enviar_nombre_usuario.emit(usuario)