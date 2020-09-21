from Core.Modelos.Carpeta import Carpeta
from Core.Controladores.ControladorCarpeta import ControladorCarpeta
from Core.Controladores.ControladorSistema import Sistema
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os


#imprimir los archivos de una carpeta
#con el /

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('350x200')
        self.raiz.configure(bg = 'beige')
        self.raiz.title('IT-PROCESSES')
        self.carpetaOrigen=''
        self.sistema=Sistema()
        
        #botonoes
        self.btn1=Button(self.raiz,text='Seleccionar Carpeta',command=self.explorarCarpeta)
        self.btn1.grid(column=0,row=2)
        self.bnt2=Button(self.raiz,text='Procesar',command=self.procesar)
        self.bnt2.grid(column=1,row=2)
        self.bnt3=Button(self.raiz,text='SO info',command=self.mostrarInfo)
        self.bnt3.grid(column=2,row=2)


        #labels
        self.lbl1=Label(self.raiz,text="IT PROCESSES")
        self.lbl1.grid(column=1,row=0)
        self.lbl2=Label(self.raiz,text="Carpeta Origen")
        self.lbl2.grid(column=0,row=1)
        

        #textArea
        self.T = Text(self.raiz, height = 5, width = 20)
        self.T.grid(column=1,row=3)
        

        self.raiz.mainloop()
    #metodo para abrir el explorador de archivos y seleccionar la capeta origen de los archivos
    def explorarCarpeta(self):
        directorio=filedialog.askdirectory()
        self.carpetaOrigen=directorio
        

    #metodo para copiar y convertir los archivos T02 a la carpeta ManizalesGPS
    def procesar(self):
        carpeta=Carpeta(self.carpetaOrigen) 
        carpeta2=Carpeta("./prueba/MnaizalesGPS")
        controlador=ControladorCarpeta()
        controlador.copiarArchivos(carpeta,carpeta2)
        controlador.convertirArchivos(carpeta2)
        messagebox.showinfo(message="Procesamiento Terminado", title="Título")

    #metodo para mostrar informacion del SO
    def mostrarInfo(self):
        info=self.sistema.mostrarRam()+"\n"
        info +=self.sistema.mostrarRamOcupada()+"\n"
        info +=self.sistema.mostrarRamDisponible()+"\n"
        info += self.sistema.mostrarCpu()+"\n"
        self.T.insert(END, info)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()



                   

