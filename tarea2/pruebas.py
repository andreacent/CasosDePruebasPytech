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
    
    '''Revisa el tiempo de reserva de 14:59 minutos'''
    def testDomTarifa(self):
        tiempo = [datetime(2015,1,1,8,0,0),datetime(2015,1,1,8,14,59)]
        tarifa = Tarifa(0,0)
        try:
            calcularPrecio(t,fechas)
        except: pass
        else: 
            self.fail("Resultado inesperado")
            
if __name__ == "__main__":
    unittest.main()