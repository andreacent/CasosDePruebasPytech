'''
Suite de casos de pruebas para la funcion CalcularPrecio() 
Creado el 22/04/2015
Equipo:Pytech
Autores:
Andrea Centeno 10-10138
Jose Patiño 11-10745
Andrea Cutillas 11-11145
'''

import unittest
from tarea2 import * 
        
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