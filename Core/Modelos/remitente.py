import stomp


import traceback
from datetime import datetime,timedelta
import threading
from threading import Thread
from typing import List
import json
#para importar desde otras carpetas
import sys
sys.path.append("..")
from Core.Controladores.ControladorCarpeta import ControladorCarpeta
from Core.Controladores.ControladorSistema import Sistema
from configparser import ConfigParser
from Core.Modelos.Carpeta import Carpeta
from Core.Modelos.ObservadorPublisher import ObservadorPublisher
from Core.Modelos.SujetoRemitente import SujetoRemitente

from  EstadoStomp import conexion
import glob
#config file
parser = ConfigParser()
parser.read('D:/TRABAJO/it-processes/config.ini')



#Instancias
#D:/TRABAJO/Manizales-49/**/**/RefData.'+datetime.now().strftime('%y')+'/Month.'+datetime.now().strftime('%b')+'/Day.'+datetime.now().strftime('%d')+'/
#rutaOrigen=glob.glob('D:\TRABAJO\Manizales-49/**/**/RefData.20/Month.Sep/Day.02')
ayer=datetime.today()+timedelta(days=-1)
rutaOrigen=glob.glob('D:/TRABAJO/Manizales-49/**/**/RefData.'+ayer.strftime('%y')+'/Month.'+ayer.strftime('%b')+'/Day.'+ayer.strftime('%d')+'')
print(rutaOrigen)
parser.set('controller','source',str(rutaOrigen[0]))
carpeta=Carpeta(parser.get('controller','source')) 
carpeta2=Carpeta(parser.get('controller','destination'))
controlador=ControladorCarpeta()
sistema=  Sistema()
finished=False


#metodo para el log json 
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
                    if  controlador.existe(carpeta):
                    
                
                        if message == "copiar":
                            
                            controlador.copiarArchivos(carpeta,carpeta2)
                            logging(self,{'operacion': message,'fecha':fecha(self),'traceback':fullTraceback})

                        elif message== "convertir":
                            controlador.convertirArchivos(carpeta2)
                            logging(self,{'operacion': message,'fecha':fecha(self),'traceback':fullTraceback})

                        elif message=="comprimir":
                            controlador.comprimirArchivosOBS(carpeta2)
                            logging(self,{'operacion': message,'fecha':fecha(self),'traceback':fullTraceback})

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
                            logging(self,{'operacion': message,'fecha':fecha(self),'traceback':fullTraceback})
                        else:

                            print('Mensaje que no tiene operacion:  "%s"' % message)
                            self.conn.disconnect()
                    else:
                        print("Carpeta  de origen no econtrada")
                        #print(carpeta.ruta)
                global finished
                finished=True

class remitente(conexion,SujetoRemitente):
    estado:int=None
    observadores:List[ObservadorPublisher]=[]

    def suscribir(self,observador:ObservadorPublisher)->None:
        self.observadores.append(observador)

    def desuscribir(self,observador:ObservadorPublisher)->None:
        self.observadores.remove(observador)

    def notificar(self)->None:
        for observador in self.observadores:
            observador.actualizar(self)
            
    def enviarMensaje(self)->None:
        pass
       
    #logica del negocio
    def recibirMensaje(self)->None:
        #configuracion de parametros
        conn = stomp.Connection()
        conn.connect(self.username, self.password, wait=True)
        print("Waiting for messages...")
        conn.set_listener('', MyListener(conn))
        conn.subscribe(destination='/queue/hilo1', id=1, ack='auto')
                
        while not finished:
            #print("procesando")
            pass
        print("proceso terminado")
        conn.disconnect()
        self.estado=1
        self.notificar()  

    


        
    
            