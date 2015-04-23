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
    
    def testA (self):
        pass 
    
    def testB (self): #Analiza los casos fronteras
        t1=Tarifa(100,-0.00000000000001)
        fechas1=[datetime(2015,1,20,13),datetime(2015,1,20,13,14,59,59)]
        
        """
        Prueba de Excepciones
        """
        try:
            calcularPrecio(t1,fechas1)
        except: self.assertTrue(True)
        else: 
            self.fail("Resultado inesperado")
            
    def testC (self):
        pass 
    
if __name__ == "__main__":
    unittest.main()