from PyQt5 import uic
import parametros as p
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventana_inicio.ui")

class VentanaInicio(window_name, base_class):

    senal_input_usuario = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crear_elementos()

    def crear_elementos(self):
        self.setWindowTitle("Ventana Inicio")
        self.setStyleSheet("VentanaInicio{background-image: url("f"{p.RUTA_FONDO}"")}")
        self.setMaximumHeight(515)
        self.setMinimumHeight(515)
        self.setMaximumWidth(624)
        self.setMinimumWidth(624)

        self.input_usuario.setPlaceholderText("Ingrese usuario")
        self.boton_jugar.clicked.connect(self.enviar_usuario)
        self.boton_salir.clicked.connect(self.close)

    def enviar_usuario(self):
        if self.senal_input_usuario:
            self.senal_input_usuario.emit(self.input_usuario.text())
    
    def recibir_comprobacion(self, usuario: str, valido: bool, error: str):
        if valido == True:
            self.hide()
        elif error == "vacio":
            self.input_usuario.setText("")
            self.input_usuario.setPlaceholderText("Debe ingresar un usuario")
        elif error == "rango":
            self.input_usuario.setText("")
            self.input_usuario.setPlaceholderText("Valor fuera de rango")
        elif error == "alnum":
            self.input_usuario.setText("")
            self.input_usuario.setPlaceholderText("Debe ser un valor alfanumérico")
    
    def ver_ranking(self):
        self.senal_ver_ranking.emit()
        self.hide()
    
    def mostrar_ventana(self):
        self.show()





