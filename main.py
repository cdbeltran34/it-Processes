from Core.Modelos.Carpeta import Carpeta
from Core.Controladores.ControladorCarpeta import ControladorCarpeta
from Core.Modelos.ControladorMensaje import ControladorMensaje
from Core.Modelos.remitente import remitente
from Core.Modelos.emisor import emisor
from Core.Controladores.ControladorSistema import Sistema
import argparse
import sys
import stomp
import time
from stomp import *
import threading
from threading import Thread
import json
import traceback
from datetime import datetime
from configparser import ConfigParser
import configparser




receptor=remitente()
emisor= emisor()
receptor.suscribir(emisor)  

controlador= ControladorMensaje(receptor)

controlador.recibirMensaje()
controlador.cambiarEstado(emisor)
#controlador.enviarMensaje() esto ya lo notifica con el patron observer

                   

