import unittest
import pylogic 


class CalculatorTest(unittest.TestCase):

    def test_normal1(self):

        #lista con los salarios de los ultimos 10 años
        lista = [4000000, 3100000, 3200000, 3300000, 3400000, 3500000, 3600000, 3700000, 3800000, 3900000]

        #Datos de salida
        expected = 2307500

        #proceso
        result = pylogic.pension_total(lista)

        #Comprobacion
        self.assertAlmostEqual(expected, result, 2)
    

    def test_normal2(self):
        #lista con los salarios de los ultimos 10 años
        lista = [5000000, 2400000, 2450000, 3150000, 3800000, 4100000, 4565000, 4825000, 4825000, 4985000]

        #Datos de salida
        expected = 2606500

        result = pylogic.pension_total(lista)

        self.assertAlmostEqual(expected, result, 2)
        


if __name__ == "__main__":
    unittest.main()

