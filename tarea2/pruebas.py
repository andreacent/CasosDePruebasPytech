'''
Suite de casos de pruebas para la funcion CalcularPrecio() 
Creado el 22/04/2015
Equipo:Pytech
Autores:
Andrea Centeno 10-10138
Jose Patino 11-10745
Andrea Cutillas 11-11145
'''

import unittest
from tarea2 import * 
from datetime import datetime

class TestCalcularPrecio(unittest.TestCase):
    
    '''FRONTERAS'''
    
    #Tiempo de reserva: 14 minutos con 59 segundos
    def testCalcularPecioA(self):
        tiempo = [datetime(2015,1,1,8),datetime(2015,1,1,8,14,59)]
        tarifa = Tarifa(0,0)
        try:
            calcularPrecio(tarifa,tiempo)
        except: pass
        else: 
            self.fail("Resultado inesperado")
            
    #Tiempo de reserva de 15 minutos
    def testCalcularPecioB(self):
        tiempo = [datetime(2015,1,1,8),datetime(2015,1,1,8,15)]
        tarifa = Tarifa(1,1)
        try:
            calcularPrecio(tarifa,tiempo)
        except: 
            self.fail("Resultado inesperado")
            
    #Tiempo de reserva: 7 dias y un segundo
    def testCalcularPecioA(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17,0,0,1)]
        tarifa = Tarifa(0,0)
        try:
            calcularPrecio(tarifa,tiempo)
        except: pass
        else: 
            self.fail("Resultado inesperado")
            
    #Tiempo de reserva: 7 dias
    def testCalcularPecioB(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17)]
        tarifa = Tarifa(1,1)
        try:
            calcularPrecio(tarifa,tiempo)
        except: 
            self.fail("Resultado inesperado")
            
if __name__ == "__main__":
    unittest.main()