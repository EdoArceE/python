# Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos

lista = []
i = 1
while len(lista) < 10:
    lista.append(i)
    i = i + 1
lista[4] = lista[4] * 2
lista[7] = lista[7] * 2
lista[9] = lista[9] * 2
print(lista)
