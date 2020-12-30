from configparser import ConfigParser
from abc import ABC, abstractmethod
from ControladorMensaje import ControladorMensaje





#clase estado del patron state que define los metodos abstractos de los estados concretos
class conexion(ABC):
    
    #archivo de coniguracion
    parser=ConfigParser()
    parser.read('E:/TRABAJO/it-processes/config.ini')

    
    def __init__(self):
        
        self.username=self.parser.get('ConectionController','username')
        self.password=self.parser.get('ConectionController','password')
        self.wait=self.parser.getboolean('ConectionController','wait')

    @property
    def context(self) ->ControladorMensaje:
        return self.cone



    @context.setter
    def context(self, conexion: ControladorMensaje)->None:
        self.cone=conexion

    @abstractmethod
    def cambiarEstado(self):
        pass

    #metodos abtractos del la clase estado
    @abstractmethod
    def enviarMensaje(self):
        pass
    @abstractmethod
    def recibirMensaje(self):
        pass
        
