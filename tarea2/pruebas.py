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
            
    #Tiempo de reserva: 7 dias y un segundo
    def testCalcularPecioC(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17,0,0,1)]
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
            
    #Tiempo de reserva: 7 dias
    def testCalcularPecioD(self):
        tiempo = [datetime(2015,1,10),datetime(2015,1,17)]
        tarifa = Tarifa(1,1)
        try:
            calcularPrecio(tarifa,tiempo)
        except: 
            self.fail("Resultado inesperado")
    
    #Una hora y un minuto = a dos horas
    '''    
    def testHoraCompleta(self):
        #una hora y un minuto
        tiempo1 = [datetime(2015,1,10,1),datetime(2015,1,10,2,1)]
        #dos horas
        tiempo2 = [datetime(2015,1,10,1),datetime(2015,1,10,3)]
        tarifa = Tarifa(1.3,1)
        
        self.assertEqual(calcularPrecio(tarifa,tiempo1), calcularPrecio(tarifa,tiempo2))
    '''#Esta prueba causa error porque se cobra por minuto, no por hora.
            
            
    '''MALICIOSOS'''
            
    #Letras como parametros de Tarifa
    def testTarifaLetras(self):
        tarifa = Tarifa("b",0)
        tiempo = [datetime(2015,4,25),datetime(2015,4,25,1)]
        try:
            calcularPrecio(tarifa,tiempo)
        except: pass
        else: 
            self.fail("Resultado inesperado")
        
    #Tarifa de semana distinta a tarifa del fin de semana
    #Si las tarifas son distintas, los precios son distintos
    def testTarifasDistintas(self):
        tarifa = Tarifa(1,0) 
        
        #frontera entre viernes y sabado
        #1 hora del dia viernes
        tiempo1 = [datetime(2015,4,24,22,59,59),datetime(2015,4,24,23,59,59)]
        #1 hora del dia sabado
        tiempo2 = [datetime(2015,4,25),datetime(2015,4,25,1)]
        
        precio1 = calcularPrecio(tarifa,tiempo1)
        precio2 = calcularPrecio(tarifa,tiempo2)
        self.assertFalse(tarifa.tasaDiaSemana == tarifa.tasaFinSemana or precio1 == precio2)
        
class TestCalcularPrecio(unittest.TestCase):

    def testFronteraA (self):
        fechas1=[datetime(2015,4,25),datetime(2015,4,25,0,15)]
        self.assertEqual(calcularPrecio(Tarifa(2**31,2**31),fechas1),Decimal(2**31/4))
    
    def testFueraRangoA (self): 
        #Analiza el caso donde las tarifas son negativas
        fechas1=[datetime(2015,4,25),datetime(2015,4,25,0,16)]
        try:
            calcularPrecio(Tarifa(-0.00001,0.0002),fechas1)
        except: pass #Se levanta la excepcion (resultado esperado)
        else: 
            self.fail("Resultado inesperado")
            
    def testFueraRangoB (self): 
        #Analiza el caso donde las tarifas son negativas
        fechas1=[datetime(2015,4,25),datetime(2015,4,25,0,16)]
        try:
            calcularPrecio(Tarifa("a","b"),fechas1)
        except: pass #Se levanta la excepcion (resultado esperado)
        else: 
            self.fail("Resultado inesperado")
                   
    def testMaliciaA(self):
        #Probamos calcular la tarifa cruzando con un ano bisiesto
        fechaBisiesta=[datetime(2016,2,28),datetime(2016,3,1)]
        self.assertEqual(calcularPrecio(Tarifa(1,1),fechaBisiesta),Decimal(48))

    
if __name__ == "__main__":
    unittest.main()
