from conexion import conexion

class emisor(conexion):

    def enviarMensaje(self)->None:
        pass
       #configurar parametros de la cola
        conn = stomp.Connection()
        conn.connect(self.username,self.password, wait=True)
        #enviar el mensaje
        conn.send(body='Listo para ejecutar', destination='/queue/hilo2')
        conn.disconnect() 


        
    def recibirMensaje(self)->None:
        pass

