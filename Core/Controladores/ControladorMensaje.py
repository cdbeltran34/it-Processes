
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
from configparser import ConfigParser
import configparser

class ControladorMensaje:

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
            global finished
            finished=True

    def __init__(self):
        self.finished=False

    def recibirMensaje(self):
        #configuracion de parametros
        conn = stomp.Connection()
        conn.connect('admin', 'password', wait=True)
        print("Waiting for messages...")
        conn.set_listener('', MyListener(conn))
        conn.subscribe(destination='/queue/hilo1', id=1, ack='auto')
        