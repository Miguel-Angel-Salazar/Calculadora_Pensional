import unittest
import pylogic 


class CalculatorTest(unittest.TestCase):

    def test_normal1(self):

        #lista con los salarios de los ultimos 10 años
        lista = [1,2,3,4,5,6,7,8,9,10]

        #Datos de salida
        expected = 5.5

        #proceso
        result = pylogic.promedio(lista)

        #Comprobacion
        self.assertAlmostEqual(expected, result, 2)


if __name__ == "__main__":
    unittest.main()

