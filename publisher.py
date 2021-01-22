
import time
import sys
import stomp
import threading
recibir=False


def enviarMensaje():
    global recibir
    recibir=True
    #configurar parametros de la cola
    conn = stomp.Connection()
    conn.connect('admin', 'password', wait=True)
    #enviar el mensaje
    conn.send(body=input("Mensaje a enviar: "), destination='/queue/hilo1')
    #conn.disconnect()
    


#para imprimir el mensaje
class MyListener(object):
    def __init__(self, conn):
        self.conn = conn
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('Mensaje:  "%s"' % message)
        if message == "apagar":
            print("entro al if de apagar")
        self.conn.disconnect()

def recibirMensaje():
    global recibir
    recibir=False
    #configuracion de parametros
    conn = stomp.Connection()
    conn.connect('admin', 'password', wait=True)
    conn.set_listener('', MyListener(conn))
    conn.subscribe(destination='/queue/hilo2', id=1, ack='auto')
    print("Waiting for messages...")
    #time.sleep(5)
    conn.disconnect()
    
    



enviarMensaje()

recibirMensaje()




     

