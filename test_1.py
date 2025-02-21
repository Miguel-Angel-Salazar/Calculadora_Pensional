import unittest
import pylogic 


class Pension_Total_Test(unittest.TestCase):

    def test_normal1(self):

        #lista con los salarios de los ultimos 10 años
        lista = [4000000, 3100000, 3200000, 3300000, 3400000, 3500000, 3600000, 3700000, 3800000, 3900000]
        genero = "femenino"
        edad = 57
        semanas = 1000
        num_hijos = 0

        #Datos de salida
        expected = 2307500

        #proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        #Comprobacion
        self.assertAlmostEqual(expected, result, 2)
    

    def test_normal2(self):
        #lista con los salarios de los ultimos 10 años
        lista = [5000000, 2400000, 2450000, 3150000, 3800000, 4100000, 4565000, 4825000, 4825000, 4985000]
        genero = "femenino"
        edad = 59
        semanas = 1000
        num_hijos = 0

        #Datos de salida
        expected = 2606500

        #proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)
    

    def test_normal3(self):
        #lista con los salarios de los ultimos 10 años
        lista = [10235685, 7100000, 7425690, 7956124, 8000000, 8245687, 8564752, 8900000, 9300000, 10000000]
        genero = "masculino"
        edad = 62
        semanas = 1300
        num_hijos = 0

        #Datos de salida
        expected =  5572315.97

        #proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)



    def test_extraordinario1(self):
        lista = [1300000, 689455, 737717, 781242, 828116, 877803, 908526, 1000000, 1160000, 1300000]
        genero = "masculino"
        edad = 65
        semanas = 1300
        num_hijos = 1

        #Datos de salida
        expected = 1423500

        #Proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)


    def test_extraordinario2(self):
        lista = [3900000, 1569875, 1750000, 1800000, 2000000, 2356987, 2565450, 2900000, 3250000, 3498520]
        genero = "femenino"
        edad = 57 
        semanas = 900
        num_hijos = 2

        #Datos de salida
        expected = 1663404.08

        #Proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)


    def test_extraordinario3(self):
        lista = [4000000, 2200000, 2400000, 2600000, 2800000, 2900000, 3000000, 5600000, 4100000, 4567898]
        genero = "femenino"
        edad = 59
        semanas = 850
        num_hijos = 3

        #Datos de salida
        expected = 2220913.37

        #Proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)


        self.assertAlmostEqual(expected, result, 2)
    

    def test_error1(self):
        lista = [5000000, 2450000, 3150000, 3800000, 2900000, 3250000, 3498520, 7100000, 7425690, 7956124]
        genero = "masculino"
        edad = 58
        semanas = 1300
        num_hijos = 1

        #Datos de salida
        expected = "No cumple con todos los requisitos"
        
        #Proceso 
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)
    

    def test_error2(self):
        lista = [6000000, 3556844, 3800000, 3900000, 4200000, 7956124, 8000000, 3800000, 5700000, 5987456]
        genero = "femenino"
        edad = 57
        semanas = 700
        num_hijos = 1

        #Datos de salida
        expected = "No cumple con todos los requisitos"

        #Proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)


    def test_error3(self):
        lista = [10000000, 3150000, 3556844, 4568788, 4789452, 5658795, 6350000, 7100000, 7425690, 7956124]
        genero = "femenino"
        edad = 55
        semanas = 740
        num_hijos = 2

        #Datos de salida
        expected = "No cumple con todos los requisitos"

        #Proceso
        result = pylogic.pension_total(lista, genero, edad, semanas, num_hijos)

        self.assertAlmostEqual(expected, result, 2)


if __name__ == "__main__":
    unittest.main()

