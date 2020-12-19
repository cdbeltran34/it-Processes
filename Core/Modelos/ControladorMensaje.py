
from conexion import conexion


class ControladorMensaje:
    _Estado=None

    
    def __init__(self,estado: conexion)->None:
        self.cambiarEstado(estado)


    def cambiarEstado(self,estado:conexion):
        self._Estado=estado
        self._Estado.conexion=self



    def recibirMensaje(self,estado):
        self._Estado.recibirMensaje()

    def enviarMensaje(self):
        self._Estado.enviarMensaje()

    