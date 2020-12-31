
#from EstadoStomp import conexion

#clase contexto del patron state
class ControladorMensaje(object):
    _Estado=None

    
    def __init__(self,estado: None)->None:
        self.cambiarEstado(estado)


    def cambiarEstado(self,estado):
        self._Estado=estado
        self._Estado.conexion=self


    #metodos propios de los estados
    def recibirMensaje(self):
        self._Estado.recibirMensaje()

    def enviarMensaje(self):
        self._Estado.enviarMensaje()

    