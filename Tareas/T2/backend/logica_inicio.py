from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_input_usuario = pyqtSignal(str, bool, str)
    senal_abrir_ventana_principal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_input_usuario(self, usuario: str):
        if usuario == "":
            self.senal_respuesta_input_usuario.emit(usuario, False, "vacio")
        elif usuario.isalnum():
            if p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES:
                self.senal_respuesta_input_usuario.emit(usuario, True, "")
                self.senal_abrir_ventana_principal.emit(usuario)
            else:
                self.senal_respuesta_input_usuario.emit(usuario, False, "rango")
        elif usuario.isalnum() == False:
            self.senal_respuesta_input_usuario.emit(usuario, False, "alnum")
