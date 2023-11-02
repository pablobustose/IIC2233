import json
import socket
import threading
from threading import Lock
import time
from cripto import desencriptar, encriptar

class Servidor:

    lock_enviar_respuesta = Lock()

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.clientes = [] #{socket_cliente: direccion, nombre_usuario: nombre, ...}
        self.sala_espera = ["", ""] #{socket_cliente: direccion, nombre_usuario: nombre, ...}
        self.jugador1 = None
        self.jugador2 = None
        self.carta_jugador1 = None
        self.carta_jugador2 = None
        self.mazo_triunfos_j1 = []
        self.mazo_triunfos_j2 = []
        self.bind_and_listen()
        thread = threading.Thread(target=self.aceptar_conexion, daemon=True)
        thread.start()

    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f'Servidor escuchando en {self.host} : {self.port}')
    
    def aceptar_conexion(self):
        try:
            while True:
                socket_cliente, address = self.socket_server.accept()
                self.clientes.append({"socket_cliente": socket_cliente, "address": address, "nombre_usuario": ""}) #se agrega a la lista de clientes
                self.log("", "Conexión cliente nuevo", f'Cliente con dirección {address} se ha conectado al servidor')
                thread_cliente = threading.Thread(target=self.interaccion_cliente, args=(socket_cliente, ), daemon = True)
                thread_cliente.start()
        except ConnectionError:
            self.log("", "Error de conexión", "Se ha desconectado un cliente")

    def interaccion_cliente(self, socket_cliente):
        try:
            while True:
                mensaje = socket_cliente.recv(4096)
                if len(mensaje) > 0:
                    mensaje = self.decodificar_mensaje(mensaje)
                    mensaje["socket_cliente"] = socket_cliente
                    self.interpretar_mensaje(mensaje)
        except ConnectionError:
            self.log("", "Error de conexión", "Se ha desconectado un cliente")

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

    def interpretar_mensaje(self, mensaje: dict): 
        if mensaje == None:
            mensaje = {}
            return mensaje
        socket_cliente = mensaje["socket_cliente"]
        if mensaje["tipo"] == "login":
            respuesta = self.comprobar_login(mensaje)
            respuesta_codificada = self.codificar_mensaje(respuesta)
            self.enviar_respuesta(respuesta_codificada, socket_cliente)
        elif mensaje["tipo"] == "volver_inicio":
            for i in range(2):
                if type(self.sala_espera[i]) == dict:
                    if self.sala_espera[i]["socket_cliente"] == mensaje["socket_cliente"]:
                        self.sala_espera.remove(self.sala_espera[i])
                        self.sala_espera.insert(i, "")
            dicc = self.codificar_mensaje({"tipo": "parar_timer_espera"})
            self.enviar_mensaje_a_todos(dicc)
        elif mensaje["tipo"] == "inicio_partida":
            self.inicio_partida()
        elif mensaje["tipo"] == "carta_seleccionada": 
            self.confirmar_eleccion_carta(socket_cliente, mensaje) 
        elif mensaje["tipo"] == "azar":
            if socket_cliente == self.jugador1["socket_cliente"]:
                self.log(self.jugador1["nombre_usuario"], "Finalizó tiempo timer","")
            elif socket_cliente == self.jugador2["socket_cliente"]:
                self.log(self.jugador2["nombre_usuario"], "Finalizó tiempo timer","")
        
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

    def enviar_respuesta(self, respuesta, sock_cliente):
        with self.lock_enviar_respuesta:
            sock_cliente.sendall(respuesta)

    def enviar_mensaje_a_todos(self, mensaje):
        for cliente in self.clientes:
            socket_cliente = cliente["socket_cliente"]
            self.enviar_respuesta(mensaje, socket_cliente)

    def comprobar_login(self, diccionario: dict):
        usuario = diccionario["nombre_usuario"]
        socket_usuario = diccionario["socket_cliente"]
        usado = False
        for cliente in self.clientes:
            if usuario.lower() == cliente["nombre_usuario"].lower():
                usado = True
        alfanumerico = True
        if usuario.isalnum() == False:
            alfanumerico = False
        largo_valido = True
        if len(usuario) < 1 or len(usuario) > 10:
            largo_valido = False
        if usado == False and alfanumerico == True and largo_valido == True:
            for persona in self.clientes:
                if persona["socket_cliente"] == socket_usuario:
                    persona["nombre_usuario"] = usuario
        diccionario = {"tipo": "login", "usado": usado, "alfanumerico": alfanumerico, "largo": largo_valido, "nombre_usuario": usuario}
        if usado == False and alfanumerico == True and largo_valido == True:
            self.log(usuario, "Validación nombre de usuario", "Nombre válido")
            if self.sala_espera[0] == "":
                diccionario["pasar_sala_espera"] = True
                diccionario["numero_usuario"] = 1
                self.sala_espera[0] = {"socket_cliente": socket_usuario, "nombre_usuario": usuario}
                mensaje = {"tipo": "actualizar_nombres", "numero_usuario": 1, "nombre_usuario": usuario}
                mensaje = self.codificar_mensaje(mensaje)
                self.enviar_mensaje_a_todos(mensaje)
                self.log(usuario, "Ingresa a Sala Espera", "")
            elif self.sala_espera[1] == "":
                diccionario["pasar_sala_espera"] = True
                diccionario["numero_usuario"] = 2
                self.sala_espera[1] = {"socket_cliente": socket_usuario, "nombre_usuario": usuario}
                mensaje = {"tipo": "actualizar_nombres", "numero_usuario": 2, "nombre_usuario": usuario}
                mensaje = self.codificar_mensaje(mensaje)
                self.enviar_mensaje_a_todos(mensaje)
                self.log(usuario, "Ingresa a Sala Espera", "")
            else:
                diccionario["pasar_sala_espera"] = False
                self.log(usuario, "No ingresa a Sala Espera", "Sala de Espera llena")
        else:
            self.log(usuario, "Validación nombre de usuario", "Nombre inválido")
        if self.sala_espera[0] != "" and self.sala_espera[1] != "": #si hay dos personas en la sala de espera
            self.iniciar_timer()
        return diccionario

    def inicio_partida(self):
        self.jugador1 = self.sala_espera[0] #{socket_cliente: direccion, nombre_usuario: nombre, ...}
        self.jugador2 = self.sala_espera[1] #{socket_cliente: direccion, nombre_usuario: nombre, ...}
        self.log("", "Inicio Partida", f"Jugadores: {self.jugador1['nombre_usuario']} - {self.jugador2['nombre_usuario']}")

    def confirmar_eleccion_carta(self, socket_cliente, carta: dict): #{"elemento": elemento, "color": color, "puntos": puntos}
        if socket_cliente == self.jugador1["socket_cliente"]:
            self.carta_jugador1 = carta
            self.log(self.jugador1["nombre_usuario"], "Carta Lanzada", f"Carta tipo {carta['elemento']}, {carta['color']}, {carta['puntos']}")
        elif socket_cliente == self.jugador2["socket_cliente"]:
            self.carta_jugador2 = carta
            self.log(self.jugador2["nombre_usuario"], "Carta Lanzada", f"Carta tipo {carta['elemento']}, {carta['color']}, {carta['puntos']}")
        if self.carta_jugador1 != None and self.carta_jugador2 != None:
            diccionario = self.codificar_mensaje({"tipo": "terminar_timer"})
            self.enviar_mensaje_a_todos(diccionario)
            self.enviar_cartas_rivales()
            self.espera_post_carta_rival()
    
    def simular_batalla(self):
        dic_victoria = {"tipo": "resultado_batalla", "resultado": "victoria"}
        dic_victoria = self.codificar_mensaje(dic_victoria)
        dic_derrota = {"tipo": "resultado_batalla", "resultado": "derrota"}
        dic_derrota = self.codificar_mensaje(dic_derrota)
        dic_empate = {"tipo": "resultado_batalla", "resultado": "empate"}
        dic_empate = self.codificar_mensaje(dic_empate)
        if self.carta_jugador1["elemento"] == "fuego" and self.carta_jugador2["elemento"] == "nieve": #gana j1
            self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j1.append(self.carta_jugador1)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
        elif self.carta_jugador1["elemento"] == "nieve" and self.carta_jugador2["elemento"] == "agua": #gana j1
            self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j1.append(self.carta_jugador1)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
        elif self.carta_jugador1["elemento"] == "agua" and self.carta_jugador2["elemento"] == "fuego": #gana j1
            self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j1.append(self.carta_jugador1)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
        elif self.carta_jugador2["elemento"] == "fuego" and self.carta_jugador1["elemento"] == "nieve": #gana j2
            self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j2.append(self.carta_jugador2)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
        elif self.carta_jugador2["elemento"] == "nieve" and self.carta_jugador1["elemento"] == "agua": #gana j2
            self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j2.append(self.carta_jugador2)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
        elif self.carta_jugador2["elemento"] == "agua" and self.carta_jugador1["elemento"] == "fuego": #gana j2
            self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
            self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
            self.mazo_triunfos_j2.append(self.carta_jugador2)
            self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
        elif self.carta_jugador1["elemento"] == "fuego" and self.carta_jugador2["elemento"] == "fuego":
            if int(self.carta_jugador1["puntos"]) > int(self.carta_jugador2["puntos"]): #gana j1
                self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j1.append(self.carta_jugador1)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
            elif int(self.carta_jugador1["puntos"]) < int(self.carta_jugador2["puntos"]): #gana j2
                self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j2.append(self.carta_jugador2)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
            else: #empate  
                self.enviar_respuesta(dic_empate, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_empate, self.jugador2["socket_cliente"])
                self.log("", "Resultado Batalla", "Ganador: EMPATE")
        elif self.carta_jugador1["elemento"] == "nieve" and self.carta_jugador2["elemento"] == "nieve":
            if int(self.carta_jugador1["puntos"]) > int(self.carta_jugador2["puntos"]): #gana j1
                self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j1.append(self.carta_jugador1)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
            elif int(self.carta_jugador1["puntos"]) < int(self.carta_jugador2["puntos"]): #gana j2
                self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j2.append(self.carta_jugador2)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
            else: #empate 
                self.enviar_respuesta(dic_empate, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_empate, self.jugador2["socket_cliente"])
                self.log("", "Resultado Batalla", "Ganador: EMPATE")
        elif self.carta_jugador1["elemento"] == "agua" and self.carta_jugador2["elemento"] == "agua":
            if int(self.carta_jugador1["puntos"]) > int(self.carta_jugador2["puntos"]): #gana j1
                self.enviar_respuesta(dic_victoria, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_derrota, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j1.append(self.carta_jugador1)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador1['nombre_usuario']}")
            elif int(self.carta_jugador1["puntos"]) < int(self.carta_jugador2["puntos"]): #gana j2
                self.enviar_respuesta(dic_derrota, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_victoria, self.jugador2["socket_cliente"])
                self.mazo_triunfos_j2.append(self.carta_jugador2)
                self.log("", "Resultado Batalla", f"Ganador: {self.jugador2['nombre_usuario']}")
            else: #empate 
                self.enviar_respuesta(dic_empate, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_empate, self.jugador2["socket_cliente"])
                self.log("", "Resultado Batalla", "Ganador: EMPATE")
        self.actualizar_cartas_victoria()
        self.carta_jugador1 = None
        self.carta_jugador2 = None

    def espera_post_carta_rival(self):
        momento_ejecucion = time.time()
        seguir = True
        while seguir:
            if time.time() >= (momento_ejecucion + 1):
                self.simular_batalla()
                seguir = False
        
    def enviar_cartas_rivales(self):
        if "socket_cliente" in self.carta_jugador1:
            del self.carta_jugador1["socket_cliente"]
        if "socket_cliente" in self.carta_jugador2:
            del self.carta_jugador2["socket_cliente"]
        carta_rival_j1 = {"tipo": "carta_rival", "carta_rival": self.carta_jugador2}
        carta_rival_j1 = self.codificar_mensaje(carta_rival_j1)
        self.enviar_respuesta(carta_rival_j1, self.jugador1["socket_cliente"])
        carta_rival_j2 = {"tipo": "carta_rival", "carta_rival": self.carta_jugador1}
        carta_rival_j2 = self.codificar_mensaje(carta_rival_j2)
        self.enviar_respuesta(carta_rival_j2, self.jugador2["socket_cliente"])

    def actualizar_cartas_victoria(self):
        momento_ejecucion = time.time()
        seguir = True
        while seguir:
            if time.time() >= (momento_ejecucion + 0.5):
                seguir = False
        dict_j1 = {"tipo": "actualizar_triunfos", "triunfos_jugador": self.mazo_triunfos_j1, "triunfos_rival": self.mazo_triunfos_j2}
        dict_j1 = self.codificar_mensaje(dict_j1)
        self.enviar_respuesta(dict_j1, self.jugador1["socket_cliente"])
        dict_j2 = {"tipo": "actualizar_triunfos", "triunfos_jugador": self.mazo_triunfos_j2, "triunfos_rival": self.mazo_triunfos_j1}
        dict_j2 = self.codificar_mensaje(dict_j2)
        self.enviar_respuesta(dict_j2, self.jugador2["socket_cliente"])
        hay_ganador, persona_ganadora = self.comprobar_victoria_partida()
        if hay_ganador == True:
            self.log(persona_ganadora["nombre_usuario"], "Ha ganado la partida", "")
            dic_ganador = self.codificar_mensaje({"tipo": "finalizar_partida", "ganador": True})
            dic_perdedor = self.codificar_mensaje({"tipo": "finalizar_partida", "ganador": False})
            if persona_ganadora == self.jugador1:
                self.enviar_respuesta(dic_ganador, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_perdedor, self.jugador2["socket_cliente"])
            elif persona_ganadora == self.jugador2:
                self.enviar_respuesta(dic_perdedor, self.jugador1["socket_cliente"])
                self.enviar_respuesta(dic_ganador, self.jugador2["socket_cliente"])
            self.sala_espera[0] = ""
            self.sala_espera[1] = ""
        else:
            self.log("", "Siguiente ronda", "")
            diccionario = self.codificar_mensaje({"tipo": "siguiente_ronda"})
            self.enviar_mensaje_a_todos(diccionario)

    def comprobar_victoria_partida(self) -> bool:
        elementos_rojo_j1 = []
        elementos_verde_j1 = []
        elementos_azul_j1 = []
        for carta_vj1 in self.mazo_triunfos_j1:
            if carta_vj1["color"] == "rojo":
                elementos_rojo_j1.append(carta_vj1["elemento"])
            elif carta_vj1["color"] == "verde":
                elementos_verde_j1.append(carta_vj1["elemento"])
            elif carta_vj1["color"] == "azul":
                elementos_azul_j1.append(carta_vj1["elemento"])
        if len(elementos_rojo_j1) > 0 and len(elementos_verde_j1) > 0 and len(elementos_azul_j1) > 0:
            for elemento_rojo_j1 in elementos_rojo_j1: #todos mismo elemento j1
                for elemento_azul_j1 in elementos_azul_j1:
                    if elemento_rojo_j1 == elemento_azul_j1:
                        for elemento_verde_j1 in elementos_verde_j1:
                            if elemento_rojo_j1 == elemento_verde_j1:
                                self.ganador = self.jugador1
                                return True, self.jugador1
            for elemento_rojo_j1_ in elementos_rojo_j1: #todos diferente elemento j1
                for elemento_azul_j1_ in elementos_azul_j1:
                    if elemento_rojo_j1_ != elemento_azul_j1_:
                        for elemento_verde_j1_ in elementos_verde_j1:
                            if elemento_rojo_j1_ != elemento_verde_j1_ and elemento_azul_j1_ != elemento_verde_j1_:
                                self.ganador = self.jugador1
                                return True, self.jugador1
        elementos_rojo_j2 = []
        elementos_verde_j2 = []
        elementos_azul_j2 = []
        for carta_vj2 in self.mazo_triunfos_j2:
            if carta_vj2["color"] == "rojo":
                elementos_rojo_j2.append(carta_vj2["elemento"])
            elif carta_vj2["color"] == "verde":
                elementos_verde_j2.append(carta_vj2["elemento"])
            elif carta_vj2["color"] == "azul":
                elementos_azul_j2.append(carta_vj2["elemento"])
        if len(elementos_rojo_j2) > 0 and len(elementos_verde_j2) > 0 and len(elementos_azul_j2) > 0:
            for elemento_rojo_j2 in elementos_rojo_j2: #todos mismo elemento j2
                for elemento_azul_j2 in elementos_azul_j2:
                    if elemento_rojo_j2 == elemento_azul_j2:
                        for elemento_verde_j2 in elementos_verde_j2:
                            if elemento_rojo_j2 == elemento_verde_j2:
                                self.ganador = self.jugador2
                                return True, self.jugador2
            for elemento_rojo_j2_ in elementos_rojo_j2: #todos diferente elemento j2
                for elemento_azul_j2_ in elementos_azul_j2:
                    if elemento_rojo_j2_ != elemento_azul_j2_:
                        for elemento_verde_j2_ in elementos_verde_j2:
                            if elemento_rojo_j2_ != elemento_verde_j2_ and elemento_azul_j2_ != elemento_verde_j2_:
                                self.ganador = self.jugador1
                                return True, self.jugador2
        return False, None

    def iniciar_timer(self):
        diccionario = {"tipo": "iniciar_timer"}
        diccionario_codificado = self.codificar_mensaje(diccionario)
        self.enviar_mensaje_a_todos(diccionario_codificado)
    
    def log(self, cliente: str, evento: str, detalle: str):
        print()
        print(f"Cliente: {cliente}")
        print(f"Evento: {evento}")
        print(f"Detalles: {detalle}")