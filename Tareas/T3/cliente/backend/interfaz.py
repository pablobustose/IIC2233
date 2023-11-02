from PyQt5.QtCore import pyqtSignal, QObject
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal

class Interfaz(QObject):

    def __init__(self):
        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()
        self.ventana_final = VentanaFinal()
    
    def mostrar_ventana_inicio(self):
        self.ventana_inicio.mostrar()
    
    def abrir_ventana_espera(self):
        self.ventana_inicio.ocultar()
        self.ventana_espera.mostrar()
    
    def abrir_ventana_juego(self):
        self.ventana_espera.ocultar()
        self.ventana_juego.mostrar()

    def abrir_ventana_final(self):
        self.ventana_juego.ocultar()
        self.ventana_final.mostrar()
    
    def volver_inicio(self):
        self.ventana_final.ocultar()
        self.ventana_espera.ocultar()
        self.ventana_inicio.mostrar()