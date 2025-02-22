import pylogic

#Metodos
def gender_asigned(valor):
    match valor:
        case (1):
            return "Masculino"
        
        case (2):
            return "Femenino"

#Creacion de variables
lista = []
genero = ""
edad = 0
semanas = 0

#Comunicacion con el usuario
print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\nPorfavor ingresa tu salario de los ultimos 10 años\n")


gen_select = int(input(f"Por favor selecciona tu genero: \n\n 1. Masculino \n 2. Femenino \n\nSeleccion: "))
genero = gender_asigned(gen_select)

edad = int(input("Ingresa tu edad actual: "))
semanas = int(input("ingrese el total de semanas cotizadas: "))
num_hijos = int(input("Cuantos Hijos tienes: "))

for i in range(1, 11, 1):
    i = int(input(f"Ingrese su {i} salario: "))
    lista.append(i)


print(lista)


#Comunicacion con la logica
print(pylogic.pension_total(lista, genero, edad, semanas, num_hijos))

