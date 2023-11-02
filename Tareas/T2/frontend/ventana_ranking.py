from PyQt5 import uic
import parametros as p
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("ventana_ranking.ui")

class VentanaRanking(window_name, base_class):

    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crear_elementos()

    def crear_elementos(self):
        self.setWindowTitle("Ventana Ranking")
        self.setStyleSheet("VentanaRanking{background-image: url("f"{p.RUTA_FONDO}"")}")
        self.setMaximumHeight(490)
        self.setMinimumHeight(490)
        self.setMaximumWidth(580)
        self.setMinimumWidth(580)

    def mostrar_ventana(self, lista: list):
        self.n1.setText(lista[0][1])
        self.n2.setText(lista[1][1])
        self.n3.setText(lista[2][1])
        self.n4.setText(lista[3][1])
        self.n5.setText(lista[4][1])
        self.p1.setText(str(lista[0][0]))
        self.p2.setText(str(lista[1][0]))
        self.p3.setText(str(lista[2][0]))
        self.p4.setText(str(lista[3][0]))
        self.p5.setText(str(lista[4][0]))
        self.show()
    
    def volver_inicio(self):
        self.senal_volver_inicio.emit()
        self.hide()
        