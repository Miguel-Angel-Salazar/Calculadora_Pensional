import pylogic


#Metodos
def gender_asigned(valor):
    match valor:
        case (1):
            return "Masculino"
        
        case (2):
            return "Femenino"
        
        case(3):
            raise ValueError("Selección inválida. Debe ser 1 (Masculino) o 2 (Femenino)")

#Creacion de variables
lista = []
genero = ""
edad = 0
semanas = 0

# Comunicación con el usuario
print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\nPor favor ingresa tu salario de los últimos 10 años\n")

try:
    gen_select = int(input("Por favor selecciona tu género: \n\n 1. Masculino \n 2. Femenino \n\nSelección: "))
    genero = gender_asigned(gen_select)

    edad = int(input("Ingresa tu edad actual: "))
    semanas = int(input("Ingrese el total de semanas cotizadas: "))
    num_hijos = int(input("¿Cuántos hijos tienes?: "))

    lista = []
    for i in range(1, 11):
        salario = int(input(f"Ingrese su salario {i}: "))
        lista.append(salario)

    print(lista)

    # Comunicación con la lógica
    print(pylogic.pension_total(lista, genero, edad, semanas, num_hijos))

except Exception as e:
    print(f"\n❌ Error: {e}") 

