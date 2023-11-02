from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QPixmap
from backend.cartas import get_penguins
from utils import data_json
from os.path import join

window_name, base_class = uic.loadUiType("ventana_juego.ui")

class VentanaJuego(window_name, base_class):

    senal_enviar_mazo = pyqtSignal(dict)
    senal_seleccionar_carta = pyqtSignal(int)
    senal_confirmar_carta = pyqtSignal()
    senal_elegir_carta_azar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cartas = []
        self.crear_elementos()
    
    def crear_elementos(self):
        self.setWindowTitle("Ventana Juego")
        self.boton_seleccionar.clicked.connect(self.confirmar_carta_seleccionada)

        self.timer = QTimer()
        self.timer.activo = False
        self.timer.setInterval(1000) #se actualiza cada 1 segundo
        self.timer.timeout.connect(self.logica_timer)
        self.timer.contador = data_json("CUENTA_REGRESIVA_RONDA")
        self.triunfos_usuario = 0
        self.triunfos_rival = 0

    def logica_timer(self):
        if self.timer.activo == False:
            self.timer.activo = True
            self.timer.contador = data_json("CUENTA_REGRESIVA_RONDA")
            self.timer.start()
            self.temporizador.setText(str(self.timer.contador))
        elif self.timer.contador == 0:
            self.timer.stop()
            self.timer.activo = False
            self.senal_elegir_carta_azar.emit()
        else:
            self.timer.contador -= 1
            self.temporizador.setText(str(self.timer.contador))

    def parar_timer(self):
        self.timer.stop()
        self.timer.activo = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if 390 < event.y() < 480:
                if 120 < event.x() < 180:
                    self.senal_seleccionar_carta.emit(1)
                    #de izquierda a derecha de la pantalla (1,2,3,4,5)
                elif 210 < event.x() < 270:
                    self.senal_seleccionar_carta.emit(2)
                elif 300 < event.x() < 360:
                    self.senal_seleccionar_carta.emit(3)
                elif 390 < event.x() < 450:
                    self.senal_seleccionar_carta.emit(4)
                elif 480 < event.x() < 540:
                    self.senal_seleccionar_carta.emit(5)
                
    def iniciar_juego(self):
        dict_cartas = get_penguins()
        self.senal_enviar_mazo.emit(dict_cartas)
        self.iniciar_ronda()
    
    def iniciar_ronda(self):
        #iniciar qtimer con su logica respectiva
        self.logica_timer()
        self.texto_resultado_batalla.setText("")
    
    def crear_ruta_carta(self, color: str, tipo: str, numero: str):
        if color == "azul":
            color_ruta = "A"
        elif color == "rojo":
            color_ruta = "R"
        elif color == "verde":
            color_ruta = "V"
        if tipo == "agua":
            tipo_ruta = "A"
        elif tipo == "fuego":
            tipo_ruta = "F"
        elif tipo == "nieve":
            tipo_ruta = "N"
        elif color == "0" and tipo == "0" and numero == "0":
            color_ruta, tipo_ruta = "0", "0"
        ruta = join(*data_json(f"RUTA_{color_ruta}{tipo_ruta}{numero}"))
        return ruta
    
    def crear_ruta_ficha(self, color: str, tipo: str):
        if color == "azul":
            color_ruta = "A"
        elif color == "rojo":
            color_ruta = "R"
        elif color == "verde":
            color_ruta = "V"
        if tipo == "agua":
            tipo_ruta = "A"
        elif tipo == "fuego":
            tipo_ruta = "F"
        elif tipo == "nieve":
            tipo_ruta = "N"
        ruta = join(*data_json(f"RUTA_{tipo_ruta}{color_ruta}"))
        return ruta
        

    def actualizar_carta_seleccionada(self, diccionario):
        elemento = diccionario["elemento"]
        color = diccionario["color"]
        puntos = diccionario["puntos"]
        pixeles = QPixmap(self.crear_ruta_carta(color, elemento, puntos))
        self.carta_jugador.setPixmap(pixeles)
        self.carta_jugador.setScaledContents(True)
        self.carta_jugador.setGeometry(490, 100, 141, 211)
    
    def confirmar_carta_seleccionada(self):
        self.senal_confirmar_carta.emit()

    def actualizar_imagenes(self, diccionario):
        carta_1 = diccionario["carta_1"]
        elemento_1 = carta_1["elemento"]
        color_1 = carta_1["color"]
        puntos_1 = carta_1["puntos"]
        pixeles_1 = QPixmap(self.crear_ruta_carta(color_1, elemento_1, puntos_1))
        self.j1.setPixmap(pixeles_1)
        self.j1.setScaledContents(True)
        self.j1.setGeometry(120, 390, 61, 91)
        
        carta_2 = diccionario["carta_2"]
        elemento_2 = carta_2["elemento"]
        color_2 = carta_2["color"]
        puntos_2 = carta_2["puntos"]
        pixeles_2 = QPixmap(self.crear_ruta_carta(color_2, elemento_2, puntos_2))
        self.j2.setPixmap(pixeles_2)
        self.j2.setScaledContents(True)
        self.j2.setGeometry(210, 390, 61, 91)
        
        carta_3 = diccionario["carta_3"]
        elemento_3 = carta_3["elemento"]
        color_3 = carta_3["color"]
        puntos_3 = carta_3["puntos"]
        pixeles_3 = QPixmap(self.crear_ruta_carta(color_3, elemento_3, puntos_3))
        self.j3.setPixmap(pixeles_3)
        self.j3.setScaledContents(True)
        self.j3.setGeometry(300, 390, 61, 91)

        carta_4 = diccionario["carta_4"]
        elemento_4 = carta_4["elemento"]
        color_4 = carta_4["color"]
        puntos_4 = carta_4["puntos"]
        pixeles_4 = QPixmap(self.crear_ruta_carta(color_4, elemento_4, puntos_4))
        self.j4.setPixmap(pixeles_4)
        self.j4.setScaledContents(True)
        self.j4.setGeometry(390, 390, 61, 91)

        carta_5 = diccionario["carta_5"]
        elemento_5 = carta_5["elemento"]
        color_5 = carta_5["color"]
        puntos_5 = carta_5["puntos"]
        pixeles_5 = QPixmap(self.crear_ruta_carta(color_5, elemento_5, puntos_5))
        self.j5.setPixmap(pixeles_5)
        self.j5.setScaledContents(True)
        self.j5.setGeometry(480, 390, 61, 91)

        pixeles_carta_grande = QPixmap(self.crear_ruta_carta("0", "0", "0"))
        self.carta_jugador.setPixmap(pixeles_carta_grande)
        self.carta_jugador.setScaledContents(True)
        self.carta_jugador.setGeometry(490, 100, 141, 211)

        pixeles_carta_rival = QPixmap(self.crear_ruta_carta("0", "0", "0"))
        self.carta_rival.setPixmap(pixeles_carta_rival)
        self.carta_rival.setScaledContents(True)
        self.carta_rival.setGeometry(250, 100, 141, 211)

    def resultado_batalla(self, diccionario: dict):
        resultado = diccionario["resultado"]
        if resultado == "victoria":
            self.texto_resultado_batalla.setText("GANASTE LA BATALLA")
        elif resultado == "derrota":
            self.texto_resultado_batalla.setText("PERDISTE LA BATALLA")
        elif resultado == "empate":
            self.texto_resultado_batalla.setText("HUBO UN EMPATE")

    def mostrar_carta_rival(self, diccionario):
        carta_rival = diccionario["carta_rival"]
        elemento = carta_rival["elemento"]
        color = carta_rival["color"]
        puntos = carta_rival["puntos"]
        pixeles = QPixmap(self.crear_ruta_carta(color, elemento, puntos))
        self.carta_rival.setPixmap(pixeles)
        self.carta_rival.setScaledContents(True)
        self.carta_rival.setGeometry(250, 100, 141, 211)
    
    def actualizar_mazo_triunfos(self, diccionario: dict):
        persona = diccionario["persona_triunfante"]
        if persona == "usuario":
            acumulado = self.triunfos_usuario
        elif persona == "rival":
            acumulado = self.triunfos_rival
        color = diccionario["color"]
        elemento = diccionario["elemento"]
        pixeles = QPixmap(self.crear_ruta_ficha(color, elemento))
        if persona == "rival":
            if acumulado == 0:
                self.vu1.setPixmap(pixeles)
                self.vu1.setScaledContents(True)
                self.vu1.setGeometry(70, 50, 40, 40)
            elif acumulado == 1:
                self.vu2.setPixmap(pixeles)
                self.vu2.setScaledContents(True)
                self.vu2.setGeometry(70, 70, 40, 40)
            elif acumulado == 2:
                self.vu3.setPixmap(pixeles)
                self.vu3.setScaledContents(True)
                self.vu3.setGeometry(70, 90, 40, 40)
            elif acumulado == 3:
                self.vu4.setPixmap(pixeles)
                self.vu4.setScaledContents(True)
                self.vu4.setGeometry(70, 110, 40, 40)
            elif acumulado == 4:
                self.vu5.setPixmap(pixeles)
                self.vu5.setScaledContents(True)
                self.vu5.setGeometry(70, 130, 40, 40)
            elif acumulado == 5:
                self.vu6.setPixmap(pixeles)
                self.vu6.setScaledContents(True)
                self.vu6.setGeometry(70, 150, 40, 40)
            elif acumulado == 6:
                self.vu7.setPixmap(pixeles)
                self.vu7.setScaledContents(True)
                self.vu7.setGeometry(70, 170, 40, 40)
            elif acumulado == 7:
                self.vu8.setPixmap(pixeles)
                self.vu8.setScaledContents(True)
                self.vu8.setGeometry(70, 190, 40, 40)
            elif acumulado == 8:
                self.vu9.setPixmap(pixeles)
                self.vu9.setScaledContents(True)
                self.vu9.setGeometry(70, 210, 40, 40)
            elif acumulado == 9:
                self.vu10.setPixmap(pixeles)
                self.vu10.setScaledContents(True)
                self.vu10.setGeometry(70, 230, 40, 40)
            elif acumulado == 10:
                self.vu11.setPixmap(pixeles)
                self.vu11.setScaledContents(True)
                self.vu11.setGeometry(70, 250, 40, 40)
            elif acumulado == 11:
                self.vu12.setPixmap(pixeles)
                self.vu12.setScaledContents(True)
                self.vu12.setGeometry(70, 270, 40, 40)
            elif acumulado == 12:
                self.vu13.setPixmap(pixeles)
                self.vu13.setScaledContents(True)
                self.vu13.setGeometry(70, 290, 40, 40)
            elif acumulado == 13:
                self.vu14.setPixmap(pixeles)
                self.vu14.setScaledContents(True)
                self.vu14.setGeometry(70, 310, 40, 40)
            self.triunfos_rival += 1
        elif persona == "usuario":
            if acumulado == 0:
                self.vr1.setPixmap(pixeles)
                self.vr1.setScaledContents(True)
                self.vr1.setGeometry(780, 50, 40, 40)
            elif acumulado == 1:
                self.vr2.setPixmap(pixeles)
                self.vr2.setScaledContents(True)
                self.vr2.setGeometry(780, 70, 40, 40)
            elif acumulado == 2:
                self.vr3.setPixmap(pixeles)
                self.vr3.setScaledContents(True)
                self.vr3.setGeometry(780, 90, 40, 40)
            elif acumulado == 3:
                self.vr4.setPixmap(pixeles)
                self.vr4.setScaledContents(True)
                self.vr4.setGeometry(780, 110, 40, 40)
            elif acumulado == 4:
                self.vr5.setPixmap(pixeles)
                self.vr5.setScaledContents(True)
                self.vr5.setGeometry(780, 130, 40, 40)
            elif acumulado == 5:
                self.vr6.setPixmap(pixeles)
                self.vr6.setScaledContents(True)
                self.vr6.setGeometry(780, 150, 40, 40)
            elif acumulado == 6:
                self.vr7.setPixmap(pixeles)
                self.vr7.setScaledContents(True)
                self.vr7.setGeometry(780, 170, 40, 40)
            elif acumulado == 7:
                self.vr8.setPixmap(pixeles)
                self.vr8.setScaledContents(True)
                self.vr8.setGeometry(780, 190, 40, 40)
            elif acumulado == 8:
                self.vr9.setPixmap(pixeles)
                self.vr9.setScaledContents(True)
                self.vr9.setGeometry(780, 210, 40, 40)
            elif acumulado == 9:
                self.vr10.setPixmap(pixeles)
                self.vr10.setScaledContents(True)
                self.vr10.setGeometry(780, 230, 40, 40)
            elif acumulado == 10:
                self.vr11.setPixmap(pixeles)
                self.vr11.setScaledContents(True)
                self.vr11.setGeometry(780, 250, 40, 40)
            elif acumulado == 11:
                self.vr12.setPixmap(pixeles)
                self.vr12.setScaledContents(True)
                self.vr12.setGeometry(780, 270, 40, 40)
            elif acumulado == 12:
                self.vr13.setPixmap(pixeles)
                self.vr13.setScaledContents(True)
                self.vr13.setGeometry(780, 290, 40, 40)
            elif acumulado == 13:
                self.vr14.setPixmap(pixeles)
                self.vr14.setScaledContents(True)
                self.vr14.setGeometry(780, 310, 40, 40)
            self.triunfos_usuario += 1

    def mostrar(self):
        self.show()
        self.iniciar_juego()
    
    def ocultar(self):
        self.hide()