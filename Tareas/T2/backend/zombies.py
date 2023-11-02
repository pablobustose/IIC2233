import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class ZombieLento(QObject):

    senal_caminar_zombie_lento = pyqtSignal(dict) # diccionario con la instancia de la clase
    senal_morder_lento = pyqtSignal(dict) # diccionario con la instancia de la clase
    senal_muerte_zombie_lento = pyqtSignal(dict) # diccionario con la instancia de la clase

    def __init__(self, fila):
        super().__init__()
        self._vida = p.VIDA_ZOMBIE
        self.dano_mordida = p.DANO_MORDIDA
        self.intervalo_mordida = p.INTERVALO_TIEMPO_MORDIDA
        self.fila = fila
        self.coordenada_x = p.POSICION_X_INICIAL_ZOMBIE
        self.coordenada_y = 170 + (self.fila) * 80
        self.proxima_coordenada = 10
        self.relentizado = False
        self.crear_elementos()
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor <= 0:
            self.senal_muerte_zombie_lento.emit({"instancia": self})
        else:
            self._vida = nuevo_valor

    def crear_elementos(self):
        self.crear_imagenes()
        self.crear_timer()

    def crear_imagenes(self):

        self.caminar_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_ZOMBIE_LENTO_CAMINANDO_1)
        self.caminar_1.setPixmap(pixeles1)
        self.caminar_1.setScaledContents(True)
        self.caminar_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.caminar_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        
        self.caminar_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_ZOMBIE_LENTO_CAMINANDO_2)
        self.caminar_2.setPixmap(pixeles2)
        self.caminar_2.setScaledContents(True)
        self.caminar_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.caminar_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
        self.comer_1 = QLabel()
        pixeles3 = QPixmap(p.RUTA_ZOMBIE_LENTO_COMIENDO_1)
        self.comer_1.setPixmap(pixeles3)
        self.comer_1.setScaledContents(True)
        self.comer_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.comer_2 = QLabel()
        pixeles4 = QPixmap(p.RUTA_ZOMBIE_LENTO_COMIENDO_2)
        self.comer_2.setPixmap(pixeles4)
        self.comer_2.setScaledContents(True)
        self.comer_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.comer_3 = QLabel()
        pixeles5 = QPixmap(p.RUTA_ZOMBIE_LENTO_COMIENDO_3)
        self.comer_3.setPixmap(pixeles5)
        self.comer_3.setScaledContents(True)
        self.comer_3.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    def crear_timer(self):
        self.timer_caminar = QTimer() 
        self.timer_caminar.contador = 1
        self.timer_caminar.timeout.connect(self.loop_caminar_lento)
        self.timer_caminar.setInterval(p.VELOCIDAD_ZOMBIE)
        self.timer_caminar.start()

        self.timer_comer = QTimer() 
        self.timer_comer.contador = 1
        self.timer_comer.timeout.connect(self.loop_morder)
        self.timer_comer.setInterval(p.INTERVALO_TIEMPO_MORDIDA)

    def loop_caminar_lento(self):
        self.senal_caminar_zombie_lento.emit({"instancia": self})

    def loop_morder(self):
        self.senal_morder_lento.emit({"instancia": self})



class ZombieRapido(QObject):

    senal_caminar_zombie_rapido = pyqtSignal(dict) # diccionario con la instancia de la clase
    senal_morder_rapido = pyqtSignal(dict) # diccionario con la instancia de la clase
    senal_muerte_zombie_rapido = pyqtSignal(dict) # diccionario con la instancia de la clase

    def __init__(self, fila):
        super().__init__()
        self._vida = p.VIDA_ZOMBIE
        self.dano_mordida = p.DANO_MORDIDA
        self.intervalo_mordida = p.INTERVALO_TIEMPO_MORDIDA
        self.fila = fila
        self.coordenada_x = p.POSICION_X_INICIAL_ZOMBIE
        self.coordenada_y = 170 + (self.fila) * 80
        self.proxima_coordenada = 10
        self.relentizado = False
        self.crear_elementos()
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor <= 0:
            self.senal_muerte_zombie_rapido.emit({"instancia": self})
        else:
            self._vida = nuevo_valor
            
    def crear_elementos(self):
        self.crear_imagenes()
        self.crear_timer()

    def crear_imagenes(self):

        self.caminar_1 = QLabel()
        pixeles1 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_CAMINANDO_1)
        self.caminar_1.setPixmap(pixeles1)
        self.caminar_1.setScaledContents(True)
        self.caminar_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.caminar_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        
        self.caminar_2 = QLabel()
        pixeles2 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_CAMINANDO_2)
        self.caminar_2.setPixmap(pixeles2)
        self.caminar_2.setScaledContents(True)
        self.caminar_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.caminar_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    
        self.comer_1 = QLabel()
        pixeles3 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_1)
        self.comer_1.setPixmap(pixeles3)
        self.comer_1.setScaledContents(True)
        self.comer_1.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.comer_2 = QLabel()
        pixeles4 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_2)
        self.comer_2.setPixmap(pixeles4)
        self.comer_2.setScaledContents(True)
        self.comer_2.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.comer_3 = QLabel()
        pixeles5 = QPixmap(p.RUTA_ZOMBIE_RAPIDO_COMIENDO_3)
        self.comer_3.setPixmap(pixeles5)
        self.comer_3.setScaledContents(True)
        self.comer_3.setGeometry(self.coordenada_x, self.coordenada_y, 65, 80)
        self.comer_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    def crear_timer(self):
        self.timer_caminar = QTimer() 
        self.timer_caminar.contador = 1
        self.timer_caminar.timeout.connect(self.loop_caminar_rapido)
        self.timer_caminar.setInterval(int(p.VELOCIDAD_ZOMBIE / 1.5))
        self.timer_caminar.start()

        self.timer_comer = QTimer() 
        self.timer_comer.contador = 1
        self.timer_comer.timeout.connect(self.loop_morder)
        self.timer_comer.setInterval(int(p.INTERVALO_TIEMPO_MORDIDA / 1.5))

    def loop_caminar_rapido(self):
        self.senal_caminar_zombie_rapido.emit({"instancia": self})

    def loop_morder(self):
        self.senal_morder_rapido.emit({"instancia": self})