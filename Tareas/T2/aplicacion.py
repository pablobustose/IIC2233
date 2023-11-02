from PyQt5.QtWidgets import QApplication
from backend.logica_ranking import LogicaRanking
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_post_ronda import VentanaPostRonda
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from frontend.ventana_ranking import VentanaRanking


class DCCruz(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        #Se instancian las ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_ranking = VentanaRanking()
        self.ventana_post_ronda = VentanaPostRonda()


        #se instancia lo del "backend" #####
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego()
        self.logica_ranking = LogicaRanking()

        #se conectan las señales
        self.conectar_input_usuario_inicio()
        self.conectar_mapa()
        self.conectar_juego()

        #se conectan los botones
        self.conectar_botones()

    def conectar_input_usuario_inicio(self):
        self.ventana_inicio.senal_input_usuario.connect(self.logica_inicio.comprobar_input_usuario)
        self.ventana_inicio.senal_ver_ranking.connect(self.logica_ranking.crear_ranking)
        self.ventana_ranking.senal_volver_inicio.connect(self.ventana_inicio.mostrar_ventana)
        self.logica_inicio.senal_respuesta_input_usuario.connect(self.ventana_inicio.recibir_comprobacion)
        self.logica_inicio.senal_abrir_ventana_principal.connect(self.ventana_principal.mostrar_ventana)
        self.logica_ranking.senal_enviar_ranking.connect(self.ventana_ranking.mostrar_ventana)
        self.ventana_principal.senal_enviar_nombre_usuario.connect(self.logica_juego.nombre_usuario)

    def conectar_mapa(self):
        self.ventana_principal.senal_enviar_mapa.connect(self.ventana_juego.comprobar_mapa)
        self.ventana_juego.senal_tipo_mapa.connect(self.logica_juego.tipo_mapa)
        self.ventana_juego.senal_mostrar_ventana_juego.connect(self.ventana_juego.mostrar_ventana)
    
    def conectar_juego(self):
        self.ventana_juego.senal_tecla.connect(self.logica_juego.checkear_cheatcodes)
        self.ventana_juego.senal_pausa.connect(self.logica_juego.pausa)
        self.ventana_juego.senal_click_derecho.connect(self.logica_juego.comprobar_click_sol)
        self.ventana_juego.senal_comprobar_creacion_planta.connect(self.logica_juego.comprobar_creacion_planta)
        self.logica_juego.senal_actualizar_datos.connect(self.ventana_juego.actualizar_datos_pantalla)
        self.logica_juego.senal_enviar_movimiento_girasol.connect(self.ventana_juego.loop_movimiento_girasol)
        self.logica_juego.senal_enviar_movimiento_azul.connect(self.ventana_juego.loop_movimiento_azul)
        self.logica_juego.senal_enviar_movimiento_clasica.connect(self.ventana_juego.loop_movimiento_clasica)
        self.logica_juego.senal_enviar_movimiento_papa.connect(self.ventana_juego.movimiento_papa)
        self.logica_juego.senal_enviar_caminar.connect(self.ventana_juego.loop_caminar)
        self.logica_juego.senal_enviar_comer.connect(self.ventana_juego.loop_comer)
        self.logica_juego.senal_enviar_nuevo_sol.connect(self.ventana_juego.mostrar_sol)
        self.logica_juego.senal_ocultar_imagenes_caminar.connect(self.ventana_juego.ocultar_zombie_caminar)
        self.logica_juego.senal_ocultar_imagenes_comer.connect(self.ventana_juego.ocultar_zombie_comer)
        self.logica_juego.senal_ocultar_planta.connect(self.ventana_juego.ocultar_planta)
        self.logica_juego.senal_enviar_movimiento_guisante.connect(self.ventana_juego.movimiento_disparo_guisante)
        self.logica_juego.senal_esconder_sol.connect(self.ventana_juego.esconder_sol)
        self.logica_juego.senal_ocular_zombie.connect(self.ventana_juego.ocultar_zombie)
        self.logica_juego.senal_finalizar_ronda.connect(self.ventana_post_ronda.mostrar_ventana)
        self.ventana_post_ronda.senal_volver_inicio.connect(self.ventana_inicio.mostrar_ventana)
        self.ventana_post_ronda.senal_siguiente_ronda.connect(self.logica_juego.nueva_ronda)
        self.logica_juego.senal_mostrar_ventana.connect(self.ventana_juego.mostrar_ventana)
        self.logica_juego.senal_ocultar_elementos_y_ventana.connect(self.ventana_juego.ocultar_ventana)
        self.logica_juego.senal_falta_plata.connect(self.ventana_juego.notificar_falta_de_soles)
        self.logica_juego.senal_mostrar_mensaje_final.connect(self.ventana_juego.mensaje_final_cruz)
        self.ventana_juego.senal_eliminar_elementos_backend.connect(self.logica_juego.eliminar_elementos)

    def conectar_botones(self):
        self.ventana_inicio.boton_ranking.clicked.connect(self.ventana_inicio.ver_ranking)
        self.ventana_ranking.boton_volver.clicked.connect(self.ventana_ranking.volver_inicio)
        self.ventana_juego.boton_iniciar.clicked.connect(self.logica_juego.iniciar_ronda)
        self.ventana_juego.boton_pausa.clicked.connect(self.logica_juego.pausa)
        self.ventana_juego.boton_avanzar.clicked.connect(self.logica_juego.intentar_avanzar_ronda)
        self.ventana_juego.boton_salir.clicked.connect(self.logica_juego.finalizar_ronda)
        self.ventana_post_ronda.boton_salir.clicked.connect(self.ventana_post_ronda.volver_inicio)
        self.ventana_post_ronda.boton_siguiente_ronda.clicked.connect(self.ventana_post_ronda.siguiente_ronda)


    def iniciar_juego(self):
        self.ventana_inicio.show()
