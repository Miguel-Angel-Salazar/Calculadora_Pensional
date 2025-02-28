class InvalidAgeError(Exception):
    def __init__(self, edad):
        super().__init__(f"""Edad inferior a la permitida para solicitar un fondo de pensiones. {edad}"""
)
    

def calculo_IBL(lista: list[int], idx = 0):
    if idx == len(lista):
        return 0
    
    return lista[idx] + calculo_IBL(lista, idx + 1)

def pension_total(lista: list[int], genero: str, edad: int, semanas: int, num_hijos: int):
    if not lista:
        return 0
    
    if genero == "Femenino" and edad < 57:
        raise InvalidAgeError(edad)
    if genero == "Masculino" and edad < 62:
        raise InvalidAgeError(edad)
    
    pension = calculo_IBL(lista) / len(lista) * 0.65

    if (genero == "Masculino" and edad >= 62 and semanas >= 1300):
        if pension < 1423500:
            return 1423500
        else:
            return pension
    
    if (genero == "Femenino" and edad >= 57):
        if edad < 57:
            raise Exception("No cumple con la edad requerida")
        if pension < 1423500:
            return 1423500
        
        if num_hijos > 3: 
            num_hijos = 3
        
        cuenta_semanas = 1000 - (50 * num_hijos)

        if (semanas >= cuenta_semanas):
            return pension
        
        else:
            return "No cumple con todos los requisitos"

    else:
        return "No cumple con todos los requisitos"
    

