from PyQt5.QtCore import pyqtSignal, QObject
from backend.cripto import encriptar, desencriptar
import socket
import threading
import json
from random import randint, shuffle

class Cliente(QObject): 

    senal_actualizar_login = pyqtSignal(dict) #dict con verificación realizada en servidor
    senal_volver_inicio = pyqtSignal()
    senal_actualizar_nombre_espera = pyqtSignal(dict) #dict por si es usuario 1 o 2
    senal_iniciar_timer = pyqtSignal()
    senal_parar_timer_espera = pyqtSignal()
    senal_actualizar_carta_seleccionada = pyqtSignal(dict) #con color, tipo y puntos
    senal_actualizar_imagenes_cartas = pyqtSignal(dict) #con los 5 dict de las cartas
    senal_enviar_resultado_batalla = pyqtSignal(dict) #le avisa al front si ganó o perdió
    senal_mostrar_rival = pyqtSignal(dict) #con la carta rival
    senal_actualizar_mazo_triunfos = pyqtSignal(dict)
    senal_parar_timer = pyqtSignal()
    senal_siguiente_ronda = pyqtSignal()
    senal_mensaje_final = pyqtSignal(dict)
    senal_abrir_ventana_final = pyqtSignal()

    def __init__(self, host, port):
        super().__init__()
        self.port = port
        self.host = host
        self.socket_cliente = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.cartas = []
        self.mazo_triunfos_usuario = []
        self.mazo_triunfos_rival = []
        self.carta_seleccionada = None 
        self.carta_confirmada = False
        self.conectar_server()
        self.crear_thread()
    
    def conectar_server(self):
        self.socket_cliente.connect((self.host, self.port))

    def crear_thread(self):
        thread = threading.Thread(target=self.interaccion_servidor, daemon=True)
        thread.start()

    def interaccion_servidor(self):
        try:
            while True:
                mensaje = self.recibir_mensaje()
                self.interpretar_mensaje(mensaje)
        except ConnectionResetError:
            print('Hubo un error de conexión con el servidor')
        finally:
            self.socket_cliente.close()

    def recibir_mensaje(self):
        bytes_mensaje= self.socket_cliente.recv(4096)
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def decodificar_mensaje(self, mensaje: bytes):
        try:
            largo = mensaje[:4]
            largo = int.from_bytes(largo, byteorder='big')
            resto = largo % 32
            if resto == 0:
                numero_bloques = largo // 32
            else:
                numero_bloques = (largo // 32) + 1
            mensaje_bytes = b''
            for i in range(numero_bloques):
                mensaje_bytes += mensaje[4 + (4 * (i + 1))+ (32 * i):4 + (4 * (i + 1))+ (32 * i) + 32] 
            mensaje_bytes = mensaje_bytes[:largo]
            mensaje_bytes = desencriptar(mensaje_bytes)
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print('Error al decodificar')
            return b''

    def interpretar_mensaje(self, mensaje):
        if mensaje["tipo"] == "login":
            self.senal_actualizar_login.emit(mensaje)
        elif mensaje["tipo"] == "actualizar_nombres":
            diccionario = {"nombre_usuario": mensaje["nombre_usuario"], "numero_usuario": mensaje["numero_usuario"]}
            self.senal_actualizar_nombre_espera.emit(diccionario)
        elif mensaje["tipo"] == "iniciar_timer":
            self.senal_iniciar_timer.emit()
        elif mensaje["tipo"] == "parar_timer_espera":
            self.senal_parar_timer_espera.emit()
        elif mensaje["tipo"] == "resultado_batalla":
            self.interpretar_resultado_batalla(mensaje)
        elif mensaje["tipo"] == "carta_rival":
            self.senal_mostrar_rival.emit(mensaje)
        elif mensaje["tipo"] == "terminar_timer":
            self.senal_parar_timer.emit()
        elif mensaje["tipo"] == "actualizar_triunfos":
            self.logica_mazo_triunfos(mensaje)
        elif mensaje["tipo"] == "siguiente_ronda":
            self.logica_nueva_ronda()
        elif mensaje["tipo"] == "finalizar_partida":
            self.finalizar_partida(mensaje)

    def codificar_mensaje(self, mensaje) -> bytes: 
        try:
            mensaje_json = json.dumps(mensaje)
            bytes_mensaje = mensaje_json.encode('utf-8')
            mensaje_encriptado = encriptar(bytes_mensaje)
            largo = len(mensaje_encriptado)
            resto = largo % 32 
            mensaje_final = b''
            mensaje_final += largo.to_bytes(4, byteorder='big')
            if resto == 0:
                numero_bloques = largo // 32
            else:
                numero_bloques = (largo // 32) + 1
            for i in range(numero_bloques - 1):
                mensaje_final += (i+1).to_bytes(4, byteorder='little')
                mensaje_final += mensaje_encriptado[(32 * i) : 32 * (i + 1)]
            mensaje_final += numero_bloques.to_bytes(4, byteorder='little')
            mensaje_final += mensaje_encriptado[32 * (numero_bloques - 1):32 * (numero_bloques - 1) + resto]
            for j in range(32 - resto):
                mensaje_final += b'\x00'
            return mensaje_final
        except json.JSONDecodeError:
            print('Error al codificar')
            return b''

    def enviar(self, mensaje: dict):
        mensaje_codificado = self.codificar_mensaje(mensaje)
        self.socket_cliente.sendall(mensaje_codificado)
    
    def inicio_partida(self):
        diccionario = {"tipo": "inicio_partida"}
        self.enviar(diccionario)
    
    def logica_nueva_ronda(self):
        if self.carta1 == self.carta_seleccionada:
            self.carta1 = self.cartas[4] #como se sacó la utilizada, se elige la de la posicion 5 porque las otras estan seleccionadas 
        elif self.carta2 == self.carta_seleccionada:
            self.carta2 = self.cartas[4]
        elif self.carta3 == self.carta_seleccionada:
            self.carta3 = self.cartas[4]
        elif self.carta4 == self.carta_seleccionada:
            self.carta4 = self.cartas[4]
        elif self.carta5 == self.carta_seleccionada:
            self.carta5 = self.cartas[4]
        self.carta_confirmada = False
        self.carta_seleccionada = None
        #actualizar mazo e imagenes
        self.actualizar_imagenes_cartas()
        #iniciar timer 
        self.senal_siguiente_ronda.emit()

    def recibir_mazo(self, dict):
        for i in range(15):
            self.cartas.append(dict[str(i)])
        shuffle(self.cartas)
        self.carta1 = self.cartas[0]
        self.carta2 = self.cartas[1]
        self.carta3 = self.cartas[2]
        self.carta4 = self.cartas[3]
        self.carta5 = self.cartas[4]
        self.actualizar_imagenes_cartas()
    
    def seleccionar_carta(self, posicion):
        if self.carta_confirmada == False:
            if posicion == 1:
                self.carta_seleccionada = self.carta1
                self.posicion_seleccionada = 1
            elif posicion == 2:
                self.carta_seleccionada = self.carta2
                self.posicion_seleccionada = 2
            elif posicion == 3:
                self.carta_seleccionada = self.carta3
                self.posicion_seleccionada = 3
            elif posicion == 4:
                self.carta_seleccionada = self.carta4
                self.posicion_seleccionada = 4
            elif posicion == 5:
                self.carta_seleccionada = self.carta5
                self.posicion_seleccionada = 5
            elemento = self.carta_seleccionada["elemento"]
            color = self.carta_seleccionada["color"]
            puntos = self.carta_seleccionada["puntos"]
            diccionario = {"elemento": elemento, "color": color, "puntos": puntos}
            self.senal_actualizar_carta_seleccionada.emit(diccionario)

    def confirmar_seleccion_carta(self):
        self.carta_confirmada = True
        elemento = self.carta_seleccionada["elemento"]
        color = self.carta_seleccionada["color"]
        puntos = self.carta_seleccionada["puntos"]
        diccionario = {"tipo": "carta_seleccionada", "elemento": elemento, "color": color, "puntos": puntos}
        self.enviar(diccionario)
        
    def actualizar_imagenes_cartas(self):
        diccionario = {"carta_1": self.carta1}
        diccionario["carta_2"] = self.carta2
        diccionario["carta_3"] = self.carta3
        diccionario["carta_4"] = self.carta4
        diccionario["carta_5"] = self.carta5
        self.senal_actualizar_imagenes_cartas.emit(diccionario)
    
    def logica_mazo_triunfos(self, diccionario): ################### ver si no está en la lista y agregarlo
        lista_triunfos_cliente = diccionario["triunfos_jugador"]
        if len(self.mazo_triunfos_usuario) < len(lista_triunfos_cliente):
            agregar_triunfo_cliente = lista_triunfos_cliente[-1]
            agregar_triunfo_cliente["persona_triunfante"] = "usuario" 
            self.senal_actualizar_mazo_triunfos.emit(agregar_triunfo_cliente)
            self.mazo_triunfos_usuario.append(agregar_triunfo_cliente)
        lista_triunfos_rival = diccionario["triunfos_rival"]
        if len(self.mazo_triunfos_rival) < len(lista_triunfos_rival):
            agregar_triunfo_rival = lista_triunfos_rival[-1]
            agregar_triunfo_rival["persona_triunfante"] = "rival" 
            self.senal_actualizar_mazo_triunfos.emit(agregar_triunfo_rival)
            self.mazo_triunfos_rival.append(agregar_triunfo_rival)

    def interpretar_resultado_batalla(self, diccionario: dict):
        resultado = diccionario["resultado"]
        self.senal_enviar_resultado_batalla.emit(diccionario)
        if self.posicion_seleccionada == 1:
            self.cartas.pop(0)
        elif self.posicion_seleccionada == 2:
            self.cartas.pop(1)
        elif self.posicion_seleccionada == 3:
            self.cartas.pop(2)
        elif self.posicion_seleccionada == 4:
            self.cartas.pop(3)
        elif self.posicion_seleccionada == 5:
            self.cartas.pop(4)
        if resultado == "derrota" or resultado == "empate":
            self.cartas.append(self.carta_seleccionada)

    def escoger_carta_azar(self):
        if self.carta_confirmada == False:
            posicion = randint(1, 5)
            if posicion == 1:
                self.carta_seleccionada = self.carta1
                self.posicion_seleccionada = 1
            elif posicion == 2:
                self.carta_seleccionada = self.carta2
                self.posicion_seleccionada = 2
            elif posicion == 3:
                self.carta_seleccionada = self.carta3
                self.posicion_seleccionada = 3
            elif posicion == 4:
                self.carta_seleccionada = self.carta4
                self.posicion_seleccionada = 4
            elif posicion == 5:
                self.carta_seleccionada = self.carta5
                self.posicion_seleccionada = 5
            elemento = self.carta_seleccionada["elemento"]
            color = self.carta_seleccionada["color"]
            puntos = self.carta_seleccionada["puntos"]
            diccionario = {"elemento": elemento, "color": color, "puntos": puntos}
            self.senal_actualizar_carta_seleccionada.emit(diccionario)
            self.confirmar_seleccion_carta()
            self.enviar({"tipo": "azar"})
    
    def finalizar_partida(self, diccionario):
        self.senal_mensaje_final.emit(diccionario)
        self.senal_abrir_ventana_final.emit()

    def volver_inicio(self):
        mensaje = {"tipo": "volver_inicio"}
        self.enviar(mensaje)
        self.senal_volver_inicio.emit()
