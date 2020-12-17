from configparser import ConfigParser
from abc import ABC, abstractmethod

class conexion(ABC):
    #archivo de coniguracion
    parser=ConfigParser()
    parser.read('../config.ini')

    
    def __init__(self):
        super().__init__()
        self.username=self.parser.get('ConectionController','username')
        self.password=self.parser.get('ConectionController','password')
        self.wait=self.parser.getboolean('ConectionController','wait')

    

    #metodos abtractos del la clase estado
    @abstractmethod
    def enviarMensaje(self)-> None:
        pass
    @abstractmethod
    def recibirMensaje(self)-> None:
        pass
