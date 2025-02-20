def suma(lista: list[int], idx = 0):
    if idx == len(lista):
        return 0
    
    return lista[idx] + suma(lista, idx + 1)

def promedio(lista: list[int]):
    if not lista:
        return 0
    
    return suma(lista) / len(lista)