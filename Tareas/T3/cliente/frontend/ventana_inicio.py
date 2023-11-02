from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt

window_name, base_class = uic.loadUiType("ventana_inicio.ui")

class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(dict)
    senal_cambiar_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.socket_cliente = None
        self.crear_elementos()
        self.mostrar()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Inicio")
        self.input_usuario.setText("")
        self.input_usuario.setPlaceholderText("Ingrese usuario")
        self.boton_jugar.clicked.connect(self.enviar_usuario)
        self.puerta_amarilla.hide()
        self.setMouseTracking(True)
        self.puerta_amarilla.setMouseTracking(True)
        self.fondo.setMouseTracking(True)
        self.centralwidget.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if 400 < event.x() < 510 and 210 < event.y() < 310:
                self.enviar_usuario()
    
    def mouseMoveEvent(self, event):
        posicion = event.pos()
        if 400 < posicion.x() < 510 and 210 < posicion.y() < 310:
            self.puerta_amarilla.show()
        else:
            self.puerta_amarilla.hide()

    def enviar_usuario(self):
        nombre_usuario = self.input_usuario.text().lower()
        self.senal_enviar_login.emit({"tipo":"login", "nombre_usuario": nombre_usuario})
    
    def verificacion_usuario(self, diccionario: dict):
        if diccionario["largo"] == False:
            self.input_usuario.setText("")
            self.respuesta.setText("Valor fuera de rango")
        elif diccionario["alfanumerico"] == False:
            self.input_usuario.setText("")
            self.respuesta.setText("Debe ser alfanumérico")
        elif diccionario["usado"] == True:
            self.input_usuario.setText("")
            self.respuesta.setText("Nombre ya en uso")
        elif diccionario["pasar_sala_espera"] == False:
            self.input_usuario.setText("")
            self.respuesta.setText("Sala de espera llena")
        else:
            self.input_usuario.setText("")
            self.respuesta.setText("")
            self.senal_cambiar_ventana.emit()
    
    def mostrar(self):
        self.show()
    
    def ocultar(self):
        self.hide()