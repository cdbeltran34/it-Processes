from Core.Modelos.Carpeta import Carpeta
from Core.Controladores.ControladorCarpeta import ControladorCarpeta
from Core.Controladores.ControladorSistema import Sistema
import argparse

#Argumentos
parser = argparse.ArgumentParser(
    description='Esto es un programa que copia y cambia la extension de los archivos .T02 a .obs, .nav y .met ',
)
parser.add_argument('-o','--origen',metavar='',help='direccion carpeta origen entre comillas dobles')
group =parser.add_mutually_exclusive_group()
group.add_argument('-r','--ram',action='store_true',help='Ram del equipo')
group.add_argument('-m','--ocu',action='store_true',help='Ram ocupada del equipo')
group.add_argument('-d','--disp',action='store_true',help='Ram disponible del equipo')
group.add_argument('-c','--cpu',action='store_true',help='cpu del equipo')
args=parser.parse_args()
#"./prueba/Manizales-49"

#procesos
carpeta=Carpeta(args.origen) 
carpeta2=Carpeta("./prueba/MnaizalesGPS")
controlador=ControladorCarpeta()
controlador.copiarArchivos(carpeta,carpeta2)
controlador.convertirArchivos(carpeta2)
controlador.comprimirArchivosOBS(carpeta2)

#informacion
sistema=  Sistema()
if args.ram:
    print('Ram: {}'.format(sistema.mostrarRam())) 
elif args.ocu:
    print('Ram Ocupada: {}'.format(sistema.mostrarRamOcupada())) 
elif args.disp:
    print('Ram disp: {}'.format(sistema.mostrarRamDisponible())) 
elif args.cpu:
    print('Cpu: {}'.format(sistema.mostrarCpu())) 

        

        

    



                   

