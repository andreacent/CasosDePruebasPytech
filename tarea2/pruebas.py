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
        tiempo = [datetime(2015,1,1,8),datetime(2015,1,1,9)]
        tarifa = Tarifa(1,1)
        try:
            calcularPrecio(tarifa,tiempo)
        except: 
            self.fail("Resultado inesperado")
            
    #Tiempo de reserva: 7 dias y un segundo
    def testCalcularPecioC(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17,0,0,1)]
        tarifa = Tarifa(0,0)
        try:
            calcularPrecio(tarifa,tiempo)
        except: pass
        else: 
            self.fail("Resultado inesperado")
            
    #Tiempo de reserva: 7 dias
    def testCalcularPecioD(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17)]
        tarifa = Tarifa(1,1)
        try:
            calcularPrecio(tarifa,tiempo)
        except: 
            self.fail("Resultado inesperado")
            
            
    '''MALICIOSOS'''
            
    #Tarifa de semana distinta a tarifa del fin de semana
    #evaluando la frontera del viernes con la del sabado
    #despues de una hora, los precios son distintos
    def testTarifasDistintas(self):
        tarifa = Tarifa(2,0) 
        
        #1 hora antes del sabado
        tiempo1 = [datetime(2015,4,24,22,59,59),datetime(2015,4,24,23,59,59)]
        #1 hora del dia sabado
        tiempo2 = [datetime(2015,4,25),datetime(2015,4,25,1)]
        
        precio1 = calcularPrecio(tarifa,tiempo1)
        precio2 = calcularPrecio(tarifa,tiempo2)
        self.assertFalse(tarifa.tasaDiaSemana == tarifa.tasaFinSemana or precio1 == precio2)
            
if __name__ == "__main__":
    unittest.main()