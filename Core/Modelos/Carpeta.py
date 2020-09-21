import os
from os import scandir


class Carpeta:


    #contructor de la clase
    #parametros: ruta(path de la carpeta) 
    def __init__(self,ruta):
        self.ruta=ruta
        self.archivos=self.obtenerArchivos()

    #metodo para obtener los archivos contenidos en la carpet
    #retorno: lista con los archivos de la carpeta
    def obtenerArchivos(self):
        return [obj for obj in scandir(self.ruta) if obj.is_file()]
    

    #mostrar el nombre de los archivos que tiene una carpeta por su nombre
    def mostrarArchivos(self):
        for file in self.archivos:
            print(file)

    def cantidadArchivos(self):
        return len(self.archivos)
    

