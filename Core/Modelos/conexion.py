from configparser import ConfigParser
from abc import ABC, abstractmethod

class conexion(ABC):
    
    #archivo de coniguracion
    parser=ConfigParser()
    parser.read('E:/TRABAJO/it-processes/config.ini')

    
    def __init__(self):
        
        self.username=self.parser.get('ConectionController','username')
        self.password=self.parser.get('ConectionController','password')
        self.wait=self.parser.getboolean('ConectionController','wait')

    @property
    def conexion(self) ->conexion:
        return self.cone
    @conexion.setter
    def conexion(self, cone: conexion)->None:
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
        
