from __future__ import annotations

from configparser import ConfigParser
from abc import ABC, abstractmethod
from Core.Modelos.ControladorMensaje import ControladorMensaje





#clase estado del patron state que define los metodos abstractos de los estados concretos
class conexion(ABC):
    @abstractmethod
    def enviarMensaje(self)->None:
        pass
    

    @abstractmethod
    def recibirMensaje(self)->None:
        pass


    
    #archivo de coniguracion
    parser=ConfigParser()
    parser.read('D:/TRABAJO/it-processes/config.ini')

    
    def __init__(self):
        
        self.username=self.parser.get('ConectionController','username')
        self.password=self.parser.get('ConectionController','password')
        self.wait=self.parser.getboolean('ConectionController','wait')

    #metodos abtractos del la clase estado
    
    
    
        
