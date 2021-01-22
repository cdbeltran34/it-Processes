
import sys
from Core.Modelos.EstadoStomp import conexion
from Core.Modelos.interfacesObserver import ObservadorPublisher
from Core.Modelos.interfacesObserver import SujetoRemitente
import stomp
class emisor(conexion,ObservadorPublisher):

    def enviarMensaje(self)->None:
        pass
       #configurar parametros de la cola
        conn = stomp.Connection()
        conn.connect(self.username,self.password, wait=True)
        #enviar el mensaje
        conn.send(body='Listo para ejecutar', destination='/queue/hilo2')
        conn.disconnect() 

    def actualizar(self,sujeto:SujetoRemitente)->None:
        if sujeto.estado==1:
            print("el estado es 1")
            self.enviarMensaje()
            
        
    def recibirMensaje(self)->None:
        pass

