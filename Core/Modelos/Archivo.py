
import os


class Archivo:
    def __init__(self,ruta,nombre):
        self.ruta=ruta
        self.nombre=nombre
        self.tamano=self.mostrarTamano()

    def mostrarTamano(self):
        return os.stat(self.ruta).st_size
    


    #metodo para mostrar la ultima fecha de modificacion de un archivo
    #retorna: fecha de modificacion en formato date
    