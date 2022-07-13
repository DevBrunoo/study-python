def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[1, 3, 5])
print(promedio) #vai mostrar o valor entre 1 e 5 que e 3