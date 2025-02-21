#buenas tardes queridos senadores de la republica les comento que aca van todo lo que se le muestra al usuario en pantalla como bien dice frontend
print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\nPorfavor ingresa tu salario de los ultimos 10 años\n")

lista = []
for i in range(1, 11, 1):
    i = int(input(f"Ingrese su {i} salario: "))
    lista.append(i)


print(lista)


