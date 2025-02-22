#Metodos
def gender_asigned(valor):
    match valor:
        case (1):
            return "Masculino"
        
        case (2):
            return "Femenino"



#Comunicacion y creacion de variables
print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\nPorfavor ingresa tu salario de los ultimos 10 años\n")

lista = []
genero = ""

gen_select = int(input(f"Por favor selecciona tu genero: \n\n 1. Masculino \n 2. Femenino \n\nSeleccion: "))
genero = gender_asigned(gen_select)


for i in range(1, 11, 1):
    i = int(input(f"Ingrese su {i} salario: "))
    lista.append(i)


print(lista)


