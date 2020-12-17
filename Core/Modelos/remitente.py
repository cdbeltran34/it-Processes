import stomp
from conexion import conexion
class remitente(conexion):
    
        
    def enviarMensaje(self)->None:
       #configurar parametros de la cola
        conn = stomp.Connection()
        conn.connect('admin','password', wait=True)
        #enviar el mensaje
        conn.send(body='Listo para ejecutar', destination='/queue/hilo2')
        conn.disconnect() 


        
   # def recibirMensaje(self)->None: