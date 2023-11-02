from PyQt5 import uic
import parametros as p
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventana_post_ronda.ui")

class VentanaPostRonda(window_name, base_class):

    senal_volver_inicio = pyqtSignal()
    senal_siguiente_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crear_elementos()

    def crear_elementos(self):
        self.setWindowTitle("Ventana Post-Ronda")
        self.setStyleSheet("VentanaPostRonda{background-image: url("f"{p.RUTA_FONDO}"")}")
        self.setMaximumHeight(490)
        self.setMinimumHeight(490)
        self.setMaximumWidth(580)
        self.setMinimumWidth(580)

    def mostrar_ventana(self, diccionario: dict):
        self.v1.setText(str(diccionario["ronda actual"]))
        self.v2.setText(str(diccionario["soles restantes"]))
        self.v3.setText(str(diccionario["zombies destruidos"]))
        self.v4.setText(str(diccionario["puntaje ronda"]))
        self.v5.setText(str(diccionario["puntaje total"]))
        if diccionario["victoria"] == True:
            self.ganado = True
            self.resultado.setText("¡Puedes combatir la siguiente oleada!")
            self.resultado.setStyleSheet("background-color: rgb(0, 215, 0);") #verde
        else:
            self.ganado = False
            self.resultado.setText("¡Los zombies cumplieron su objetivo! Perdiste :(")
            self.resultado.setStyleSheet("background-color: rgb(234, 62, 66);") #rojo
        self.show()
    
    def volver_inicio(self):
        self.senal_volver_inicio.emit()
        self.hide()
    
    def siguiente_ronda(self):
        if self.ganado == True:
            self.senal_siguiente_ronda.emit()
            self.hide()
        