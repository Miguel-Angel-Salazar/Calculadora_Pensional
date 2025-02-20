def suma(lista: list[int], idx = 0):
    if idx == len(lista):
        return 0
    
    return lista[idx] + suma(lista, idx + 1)

def pension_total(lista: list[int], genero: str, edad: int, semanas: int, num_hijos: int):
    if not lista:
        return 0
    
    pension = suma(lista) / len(lista) * 0.65

    if (genero == "masculino" and edad >= 62 and semanas >= 1300):
        if pension < 1423500:
            return 1423500
        else:
            return pension
    
    elif (genero == "femenino" and edad >= 57):
        if num_hijos > 3:
            num_hijos = 3
        
        cuenta_semanas = semanas - (50 * num_hijos)

        if (cuenta_semanas >= semanas):
            return pension

    else:
        return "No cumple con todos los requisitos"
    

