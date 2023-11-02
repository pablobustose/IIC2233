import sys
from os.path import join
from PyQt5.QtWidgets import QApplication
from backend.cliente import Cliente
from backend.interfaz import Interfaz
from utils import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    try:
        # =========> Instanciamos la APP <==========
        app = QApplication(sys.argv)

        # =========> Iniciamos el cliente <==========
        cliente = Cliente(HOST, PORT)
        interfaz = Interfaz()
        #############interfaz.ventana_inicio.socket_cliente = cliente.socket_cliente

        # =========> Conectamos señales <==========
        #Señales ventanas
        interfaz.ventana_espera.senal_volver_inicio.connect(cliente.volver_inicio)
        interfaz.ventana_final.senal_volver_inicio.connect(interfaz.volver_inicio)
        cliente.senal_volver_inicio.connect(interfaz.volver_inicio)
        cliente.senal_parar_timer_espera.connect(interfaz.ventana_espera.parar_timer)
        interfaz.ventana_inicio.senal_enviar_login.connect(cliente.enviar)
        cliente.senal_actualizar_login.connect(interfaz.ventana_inicio.verificacion_usuario)
        interfaz.ventana_inicio.senal_cambiar_ventana.connect(interfaz.abrir_ventana_espera)
        cliente.senal_actualizar_nombre_espera.connect(interfaz.ventana_espera.actualizar_nombres)
        cliente.senal_iniciar_timer.connect(interfaz.ventana_espera.logica_timer)
        interfaz.ventana_espera.senal_iniciar_partida.connect(interfaz.abrir_ventana_juego)
        cliente.senal_abrir_ventana_final.connect(interfaz.abrir_ventana_final)
        cliente.senal_mensaje_final.connect(interfaz.ventana_final.actualizar_mensaje_final)

        #señales juego
        interfaz.ventana_juego.senal_enviar_mazo.connect(cliente.recibir_mazo)
        interfaz.ventana_juego.senal_seleccionar_carta.connect(cliente.seleccionar_carta)
        cliente.senal_actualizar_carta_seleccionada.connect(interfaz.ventana_juego.actualizar_carta_seleccionada)
        cliente.senal_actualizar_imagenes_cartas.connect(interfaz.ventana_juego.actualizar_imagenes)
        interfaz.ventana_espera.senal_inicio_partida.connect(cliente.inicio_partida)
        interfaz.ventana_juego.senal_confirmar_carta.connect(cliente.confirmar_seleccion_carta)
        cliente.senal_enviar_resultado_batalla.connect(interfaz.ventana_juego.resultado_batalla)
        cliente.senal_mostrar_rival.connect(interfaz.ventana_juego.mostrar_carta_rival)
        cliente.senal_actualizar_mazo_triunfos.connect(interfaz.ventana_juego.actualizar_mazo_triunfos)
        cliente.senal_parar_timer.connect(interfaz.ventana_juego.parar_timer)
        interfaz.ventana_juego.senal_elegir_carta_azar.connect(cliente.escoger_carta_azar)
        cliente.senal_siguiente_ronda.connect(interfaz.ventana_juego.iniciar_ronda)

        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        cliente.salir()
        sys.exit()