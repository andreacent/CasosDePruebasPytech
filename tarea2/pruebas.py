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

class Tester(unittest.TestCase):
    
    '''Revisa que el tiempo de reserva con un segundo antes de 15 minutos.'''
    def testDomTarifa(self):
        tiempo = [datetime(year=2015,month=1,day=1,hour=8,minute=0,second=0),datetime(year=2015,month=1,day=1,hour=8,minute=14,second=59)]
        tarifa = Tarifa(0,0)
        precio = calcularPrecio(tarifa,tiempo)
        assert precio == 0.00
    
if __name__ == "__main__":
    unittest.main()