def suma(lista: list[int], idx = 0):
    if idx == len(lista):
        return 0
    
    return lista[idx] + suma(lista, idx + 1)

def pension_total(lista: list[int]):
    if not lista:
        return 0
    
    pension = suma(lista) / len(lista) * 0.65
    return pension

