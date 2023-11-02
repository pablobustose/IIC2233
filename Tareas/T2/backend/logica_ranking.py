from PyQt5.QtCore import QObject, pyqtSignal

class LogicaRanking(QObject):

    senal_enviar_ranking = pyqtSignal(list) #lista ordenada con tipo [puntaje, nombre]

    def __init__(self):
        super().__init__()
    
    def crear_ranking(self):
        archivo = open("puntajes.txt")
        lista_readlines = archivo.readlines()
        lista_puntajes = []
        for linea in lista_readlines:
            jugador = linea.strip("\n").split(",")
            jugador_agregar = [int(jugador[1]), jugador[0]] #[puntaje, usuario]
            lista_puntajes.append(jugador_agregar)
        lista_puntajes.sort(reverse=True)
        while len(lista_puntajes) > 5:
            lista_puntajes.pop()
        self.senal_enviar_ranking.emit(lista_puntajes)


