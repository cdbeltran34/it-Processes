from Core.Modelos.Carpeta import Carpeta
from Core.Controladores.ControladorCarpeta import ControladorCarpeta
from Core.Controladores.ControladorSistema import Sistema
import argparse
import sys
import stomp
import time
from stomp import *
import threading
from threading import Thread
import json
import traceback
from datetime import datetime



carpeta=Carpeta("./prueba/Manizales-49") 
carpeta2=Carpeta("./prueba/MnaizalesGPS")
controlador=ControladorCarpeta()
sistema=  Sistema()




#metodo para crear el archivo log en formato json
#parametro= dict(objeto diccionario con mensaje,fecha actual)
def logging(dict):
    loggingsFile='log.json'
    with open(loggingsFile,'w')as f:
        json.dump(dict,f,indent=4)
#metodo para generar fecha y hora
#retorna en formato UTC la fecha y hora del proceso
def fecha():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


#clase listener para captar el mensaje desde el broker stomp
class MyListener(object):
    def __init__(self, conn):
        self.conn = conn
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        try:
            print(5 / 0)
        except ZeroDivisionError:
            fullTraceback= str(traceback.format_exc())
            
        

            if message == "copiar":
                
                controlador.copiarArchivos(carpeta,carpeta2)
                logging({'operacion': message,'fecha':fecha(),'traceback':fullTraceback})
            elif message== "convertir":
                controlador.convertirArchivos(carpeta2)
                logging({'operacion': message,'fecha':fecha(),'traceback':fullTraceback})
            elif message=="comprimir":
                controlador.comprimirArchivosOBS(carpeta2)
                logging({'operacion': message,'fecha':fecha(),'traceback':fullTraceback})
            elif message=="todo":
                t1=threading.Thread(target=controlador.copiarArchivos,args=(carpeta,carpeta2,))
                t2=threading.Thread(target=controlador.convertirArchivos,args=(carpeta2,))
                t3=threading.Thread(target=controlador.comprimirArchivosOBS,args=(carpeta2,))
                t1.start()
                t1.join()
                t2.start()
                t2.join()
                t3.start()
                t3.join()
            elif message=="sistema":
                print('Ram: {},Ram Ocupada: {},Ram disp: {},Cpu: {}'.format(sistema.mostrarRam(),sistema.mostrarRamOcupada()
                ,sistema.mostrarRamDisponible(),sistema.mostrarCpu()))
                logging({'operacion': message,'fecha':fecha(),'traceback':fullTraceback})
            else:

                print('Mensaje que no tiene operacion:  "%s"' % message)
                self.conn.disconnect()

#metodo para recibir el mensaje del broker stomp
def recibirMensaje():
    global mandar
    mandar=True
    #configuracion de parametros
    conn = stomp.Connection()
    conn.connect('admin', 'password', wait=True)
    conn.set_listener('', MyListener(conn))
    conn.subscribe(destination='/queue/hilo1', id=1, ack='auto')
    print("Waiting for messages...")
    time.sleep(100)
    
    #conn.disconnect()


#metodo para responder el mensaje 

def mandarMensaje():
    global mandar
    mandar=False
    #configurar parametros de la cola
    conn = stomp.Connection()
    conn.connect('admin', 'password', wait=True)
    #enviar el mensaje
    conn.send(body='Listo para ejecutar', destination='/queue/hilo2')
    conn.disconnect()

recibirMensaje()
mandarMensaje()

        

    



                   

