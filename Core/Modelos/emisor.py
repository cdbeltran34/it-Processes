
import sys
from EstadoStomp import conexion
from ObservadorPublisher import ObservadorPublisher
from SujetoRemitente import SujetoRemitente
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
            self.enviarMensaje()
            
        
    def recibirMensaje(self)->None:
        pass

