import sys
from aplicacion import DCCruz

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    juego = DCCruz(sys.argv)
    juego.iniciar_juego()
    sys.exit(juego.exec())
