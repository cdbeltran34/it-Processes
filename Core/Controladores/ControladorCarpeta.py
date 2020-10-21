
import shutil
from glob import glob 
import os
import os.path
import zipfile
#from Modelos.Carpeta import Carpeta

class ControladorCarpeta:
    
    """metodo para copiar los archivos de una carpeta a otra
    #parametros: carpetaOrg(carpeta origen),carpetaDest(carpeta destino)"""
    def copiarArchivos(self,carpetaOrg,carpetaDest):
        for archivo in carpetaOrg.archivos:
            shutil.copy2(str(carpetaOrg.ruta)+"/"+archivo.name,str(carpetaDest.ruta)+"/"+archivo.name)

    
    
    """metodo que copia y convierte el archivo con extension .T02 a .OBS en la misma carpeta """
    #parametros: nombreArchivo(ruta completa incluyendo el nombre del archivo con la extension)
    #nombre (ruta del archivo excepto la extension)
    def OBS(self,nombreArchivo,nombre):
            shutil.copy2(nombreArchivo,nombre+str('.OBS'))
            #print("El archivo '{}' se llama '{}' y tiene la extensión '{}'".format(
            #fname, nombre, extension))
            #print(fname)


    """metodo que copia y convierte el archivo con extension .T02 a .NAV en la misma carpeta """
    def NAV(self,nombreArchivo,nombre):
        shutil.copy2(nombreArchivo,nombre+str('.NAV'))


    """metodo que copia y convierte el archivo con extension .T02 a .MET en la misma carpeta """
    def MET(self,nombreArchivo,nombre):
        shutil.copy2(nombreArchivo,nombre+str('.MET'))




    """metodo que recorre los archivos de la carpeta, y llama las tres funciones con el nombre completo del archivo
        (con extension) y el nombre sin extension
        Parametros: path de la carpeta
    """
    def convertirArchivos(self,carpeta):
        for fname in glob(str(carpeta.ruta)+'/*.T02'):
            nombre,extension= os.path.splitext(fname)
            self.OBS(fname,nombre)
            self.NAV(fname,nombre)
            self.MET(fname,nombre)

            
    #metodo que comprime los archivos .OBS y los copia a la misma carpeta donde estan
    def comprimirArchivosOBS(self,carpeta):
        for fname in glob(str(carpeta.ruta)+'/*.OBS'):
            nombre,extension=os.path.splitext(fname)
            jungle_zip = zipfile.ZipFile(nombre+str('.zip'), 'w')
            jungle_zip.write(fname, compress_type=zipfile.ZIP_DEFLATED)
            jungle_zip.close()


        

    





