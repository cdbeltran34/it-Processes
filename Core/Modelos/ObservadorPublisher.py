
from abc import ABC,abstractmethod
from Core.Modelos.SujetoRemitente import SujetoRemitente

#La interface del observador(Publisher) declara el metodo actualizar usado por el sujeto (remitente)
class ObservadorPublisher(ABC):
    @abstractmethod
    def actualizar(self,sujeto:SujetoRemitente)->None:
        """
        recibe actualizaciones del sujeto(remitente)
        """
        pass