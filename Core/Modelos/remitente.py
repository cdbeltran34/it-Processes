import stomp
from conexion import conexion
import traceback
from datetime import datetime
import threading
from threading import Thread
from datetime import datetime
import json


class remitente(conexion):
    finished=False
    
    def enviarMensaje(self)->None:
        pass
       

    def logging(self,dict):
        loggingsFile='log.json'
        
        with open(loggingsFile,'w')as f:
            json.dump(dict,f,indent=4)

    def fecha(self):
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


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


        
    def recibirMensaje(self)->None:
        #configuracion de parametros
        conn = stomp.Connection()
        conn.connect(self.username, self.password, wait=True)
        print("Waiting for messages...")
        conn.set_listener('', MyListener(conn))
        conn.subscribe(destination='/queue/hilo1', id=1, ack='auto')
        
        
        while not finished:
            print("procesando")
        print("proceso terminado")
        conn.disconnect()  
            