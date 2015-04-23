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
    
    def testB (self):
        t=Tarifa(100,120)
        fechas=[datetime(2015,1,20,13),datetime(2015,1,20,13,14,59)]
        """
        Prueba de Excepciones
        """
        try:
            calcularPrecio(t,fechas)
        except: pass
        else: 
            self.fail("Resultado inesperado")
            
    def testC (self):
        pass 
    
if __name__ == "__main__":
    unittest.main()