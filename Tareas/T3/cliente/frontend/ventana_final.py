from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
window_name, base_class = uic.loadUiType("ventana_final.ui")

class VentanaFinal(window_name, base_class):
    
    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crear_elementos()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Final")
        self.boton_volver.clicked.connect(self.volver_inicio)
    
    def volver_inicio(self):
        self.senal_volver_inicio.emit()
    
    def mostrar(self):
        self.show()
    
    def actualizar_mensaje_final(self, diccionario):
        ganador = diccionario["ganador"]
        if ganador == True:
            self.mensaje.setText("¡FELICIDADES, HAS GANADO!")
        else:
            self.mensaje.setText("PERDISTE LA PARTIDA")

    def ocultar(self):
        self.hide()