import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class PlantaClasica(QObject):

    senal_movimiento_clasica = pyqtSignal(dict) # dict con la instancia de la clase
    senal_crear_guisante = pyqtSignal(dict) # dict con la instancia de la clase

    def __init__(self, fila, columna):
        super().__init__()
        self.tipo = "clásica"
        self.vida = p.VIDA_PLANTA
        self.fila = fila
        self.columna = columna
        self.coordenada_x = 320 + (self.columna) * 65
        self.coordenada_y = 170 + (self.fila) * 80
        self.intervalo_disparo = p.INTERVALO_DISPARO
        self.dano_proyectil = p.DANO_PROYECTIL
        self.crear_elementos()
    
    def crear_elementos(self):
        self.crear_imagenes()
        self.crear_timer()

    def crear_imagenes(self):

        self.pos_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_CLASICA1)
        self.pos_1.setPixmap(pixeles1)
        self.pos_1.setScaledContents(True)
        self.pos_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        
        self.pos_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_CLASICA2)
        self.pos_2.setPixmap(pixeles2)
        self.pos_2.setScaledContents(True)
        self.pos_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
        self.pos_3 = QLabel()
        pixeles3 = QPixmap(p.RUTA_CLASICA3)
        self.pos_3.setPixmap(pixeles3)
        self.pos_3.setScaledContents(True)
        self.pos_3.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    def crear_timer(self):
        self.timer_movimiento = QTimer() 
        self.timer_movimiento.contador = 1
        self.timer_movimiento.timeout.connect(self.loop_movimiento_clasica)
        self.timer_movimiento.setInterval(int(p.INTERVALO_DISPARO / 3))

        self.timer_disparo = QTimer() 
        self.timer_disparo.timeout.connect(self.crear_guisante)
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        
    
    def loop_movimiento_clasica(self):
        self.senal_movimiento_clasica.emit({"instancia": self})
    
    def crear_guisante(self):
        self.senal_crear_guisante.emit({"instancia": self})

class PlantaAzul(QObject):

    senal_movimiento_azul = pyqtSignal(dict) # dict con la instancia de la clase
    senal_crear_guisante_azul = pyqtSignal(dict) # dict con la instancia de la clase

    def __init__(self, fila, columna):
        super().__init__()
        self.tipo = "azul"
        self.vida = p.VIDA_PLANTA
        self.fila = fila
        self.columna = columna
        self.coordenada_x = 320 + (self.columna) * 65
        self.coordenada_y = 170 + (self.fila) * 80
        self.intervalo_disparo = p.INTERVALO_DISPARO
        self.dano_proyectil = p.DANO_PROYECTIL
        self.ralentizar = p.RALENTIZAR_ZOMBIE
        self.crear_elementos()
    
    def crear_elementos(self):
        self.crear_imagenes()
        self.crear_timer()
    
    def crear_imagenes(self):

        self.pos_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_AZUL1)
        self.pos_1.setPixmap(pixeles1)
        self.pos_1.setScaledContents(True)
        self.pos_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.pos_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_AZUL2)
        self.pos_2.setPixmap(pixeles2)
        self.pos_2.setScaledContents(True)
        self.pos_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
        self.pos_3 = QLabel()
        pixeles3 = QPixmap(p.RUTA_AZUL3)
        self.pos_3.setPixmap(pixeles3)
        self.pos_3.setScaledContents(True)
        self.pos_3.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    def crear_timer(self):
        self.timer_movimiento = QTimer() 
        self.timer_movimiento.contador = 1
        self.timer_movimiento.timeout.connect(self.loop_movimiento_clasica)
        self.timer_movimiento.setInterval(int(p.INTERVALO_DISPARO / 3))

        self.timer_disparo = QTimer() 
        self.timer_disparo.timeout.connect(self.crear_guisante)
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
    
    def loop_movimiento_clasica(self):
        self.senal_movimiento_azul.emit({"instancia": self})
    
    def crear_guisante(self):
        self.senal_crear_guisante_azul.emit({"instancia": self})

class Girasol(QObject):
    
    senal_movimiento_girasol = pyqtSignal(dict) # dict con la instancia de la clase
    senal_crear_sol = pyqtSignal(dict) # dict con las coordenadas de la planta

    def __init__(self, fila, columna):
        super().__init__()
        self.tipo = "girasol"
        self.vida = p.VIDA_PLANTA
        self.fila = fila
        self.columna = columna
        self.coordenada_x = 320 + (self.columna) * 65
        self.coordenada_y = 170 + (self.fila) * 80
        self.intervalo_soles = p.INTERVALO_SOLES_GIRASOL
        self.crear_elementos()

    def crear_elementos(self):
        self.crear_imagenes()
        self.crear_timer()
    
    def crear_imagenes(self):

        self.pos_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_GIRASOL1)
        self.pos_1.setPixmap(pixeles1)
        self.pos_1.setScaledContents(True)
        self.pos_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.pos_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_GIRASOL2)
        self.pos_2.setPixmap(pixeles2)
        self.pos_2.setScaledContents(True)
        self.pos_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
    def crear_timer(self):
        self.timer_movimiento = QTimer() 
        self.timer_movimiento.contador = 1
        self.timer_movimiento.timeout.connect(self.loop_movimiento_girasol)
        self.timer_movimiento.setInterval(p.INTERVALO_MOVIMIENTO_GIRASOL)

        self.timer_soles = QTimer() 
        self.timer_soles.timeout.connect(self.generar_soles)
        self.timer_soles.setInterval(p.INTERVALO_SOLES_GIRASOL)

    def loop_movimiento_girasol(self):
        self.senal_movimiento_girasol.emit({"instancia": self})
    
    def generar_soles(self):
        diccionario = {"coordenada_x": self.coordenada_x, "coordenada_y": self.coordenada_y}
        self.senal_crear_sol.emit(diccionario)

class Papa(QObject):

    senal_movimiento_papa = pyqtSignal(dict) # dict con la instancia de la clase

    def __init__(self, fila, columna):
        super().__init__()
        self.tipo = "papa"
        self.fila = fila
        self.columna = columna
        self.coordenada_x = 320 + (self.columna) * 65
        self.coordenada_y = 170 + (self.fila) * 80
        self._vida = p.VIDA_PLANTA * 2
        self.contador_imagen_actual = 1
        self.crear_elementos()
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor <= p.VIDA_PAPA_2 and self.contador_imagen_actual == 1:
            self.contador_imagen_actual += 1
            self.senal_movimiento_papa.emit({"instancia": self}) #para cambiar la imagen
            self._vida = nuevo_valor
        elif nuevo_valor <= p.VIDA_PAPA_3 and self.contador_imagen_actual == 2:
            self.contador_imagen_actual += 1
            self.senal_movimiento_papa.emit({"instancia": self}) #para cambiar la imagen
            self._vida = nuevo_valor
        elif nuevo_valor <= 0:
            self.contador_imagen_actual = 0
            self.senal_movimiento_papa.emit({"instancia": self}) #para sacar la imagen
            self._vida = 0
        else:
            self._vida = nuevo_valor

    def crear_elementos(self):
        self.crear_imagenes()
    
    def crear_imagenes(self):

        self.pos_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_PAPA1)
        self.pos_1.setPixmap(pixeles1)
        self.pos_1.setScaledContents(True)
        self.pos_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.pos_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_PAPA2)
        self.pos_2.setPixmap(pixeles2)
        self.pos_2.setScaledContents(True)
        self.pos_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.pos_3 = QLabel()
        pixeles3 = QPixmap(p.RUTA_PAPA3)
        self.pos_3.setPixmap(pixeles3)
        self.pos_3.setScaledContents(True)
        self.pos_3.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.pos_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

class Sol(QObject): 
    def __init__(self, coordenada_x, coordenada_y):
        super().__init__()
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.crear_imagen()
    
    def crear_imagen(self):
        self.imagen = QLabel()
        pixeles = QPixmap(p.RUTA_SOL)
        self.imagen.setPixmap(pixeles)
        self.imagen.setScaledContents(True)
        self.imagen.setGeometry(self.coordenada_x, self.coordenada_y, 40, 40)
        self.imagen.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

class Guisante(QObject):

    senal_movimiento_guisante = pyqtSignal(dict) #dict con la instancia

    def __init__(self, coordenada_x, coordenada_y):
        super().__init__()
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.impacto = False
        self.tipo = "verde"
        self.crear_imagen()
        self.crear_timer()
    
    def crear_imagen(self):
        self.disparado = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE1)
        self.disparado.setPixmap(pixeles)
        self.disparado.setScaledContents(True)
        self.disparado.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.disparado.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.impacto1 = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE2)
        self.impacto1.setPixmap(pixeles)
        self.impacto1.setScaledContents(True)
        self.impacto1.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.impacto1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.impacto2 = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE3)
        self.impacto2.setPixmap(pixeles)
        self.impacto2.setScaledContents(True)
        self.impacto2.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.impacto2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
    def crear_timer(self):
        self.timer_movimiento = QTimer() 
        self.timer_movimiento.setInterval(p.VELOCIDAD_GUISANTE)
        self.timer_movimiento.contador = 1
        self.timer_movimiento.timeout.connect(self.movimiento_guisante)
        self.timer_movimiento.start()

    def movimiento_guisante(self):
        self.senal_movimiento_guisante.emit({"instancia": self})
    

class GuisanteAzul(QObject):

    senal_movimiento_guisante_azul = pyqtSignal(dict) #dict con la instancia

    def __init__(self, coordenada_x, coordenada_y):
        super().__init__()
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.impacto = False
        self.tipo = "azul"
        self.crear_imagen()
        self.crear_timer()
    
    def crear_imagen(self):
        self.disparado = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE_AZUL1)
        self.disparado.setPixmap(pixeles)
        self.disparado.setScaledContents(True)
        self.disparado.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.disparado.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.impacto1 = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE_AZUL2)
        self.impacto1.setPixmap(pixeles)
        self.impacto1.setScaledContents(True)
        self.impacto1.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.impacto1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.impacto2 = QLabel()
        pixeles = QPixmap(p.RUTA_GUISANTE_AZUL3)
        self.impacto2.setPixmap(pixeles)
        self.impacto2.setScaledContents(True)
        self.impacto2.setGeometry(self.coordenada_x, self.coordenada_y, 30, 30)
        self.impacto2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
    def crear_timer(self):
        self.timer_movimiento = QTimer() 
        self.timer_movimiento.setInterval(p.VELOCIDAD_GUISANTE)
        self.timer_movimiento.contador = 1
        self.timer_movimiento.timeout.connect(self.movimiento_guisante)
        self.timer_movimiento.start()

    def movimiento_guisante(self):
        self.senal_movimiento_guisante_azul.emit({"instancia": self})

        