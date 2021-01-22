

from abc import ABC,abstractmethod
from Core.Modelos.ObservadorPublisher import ObservadorPublisher
#interface de la clase remitent que define los metodos abstractos para gestionar los suscriptores
class SujetoRemitente(ABC):

    @abstractmethod
    def suscribir(self,observador:ObservadorPublisher)->None:
        """
        suscribe el observador (publisher) al sujeto
        """
    pass


    @abstractmethod
    def desuscribir(self,observador:ObservadorPublisher)->None:
        """
        desuscribe un observador del sujeto
        """
        pass

    @abstractmethod
    def notificar(self)->None:
        """notifica al observador(publisher) de un evento"""
        pass
