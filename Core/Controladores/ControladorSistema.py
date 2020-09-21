import os
import psutil

class Sistema:

    #metodo para imprimir cantidad de memoria RAM del sistema
    def mostrarRam (self):
        giga=1000000000
        return("RAM: "+str(psutil.virtual_memory().total/giga)+"GB")

    #metodo para imprimir porcentaje de RAM ocupada en el sistema
    
    def mostrarRamOcupada(self):
        return("Porcentaje RAM ocupada: "+str(psutil.virtual_memory().percent)+"%")

    #metodo para imprimir porcentaje de Ram disponible
    def mostrarRamDisponible(self):
        return("Porcentaje de RAM disponbile: "+str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)+" %")
    
    #metodo para mostrar Cpu del sistema
    def mostrarCpu(self):
        return("Porcentaje de CPU ocupado: "+str(psutil.cpu_percent())+"%")
