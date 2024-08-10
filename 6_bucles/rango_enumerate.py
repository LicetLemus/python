# range en python es una función que nos permite generar una secuencia de números, en un rango determinado.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in range(3, 9):
    print(numero)

# range(inicio, fin, paso)
# inicio: número de inicio de la secuencia
# fin: número final de la secuencia
# paso: incremento entre cada número de la secuencia

for numero in range(1, 10, 2):
    print(numero) # imprime los números impares del 1 al 10


# enumerate en python es una función que nos permite iterar sobre una secuencia de elementos, devolviendo el índice y el valor de cada elemento.

lista_productos = ['manzana', 'pera', 'uva', 'sandía', 'papaya']

for indice, valor in enumerate(lista_productos):
    print(indice, valor)

# enumerate(secuencia, inicio)
# secuencia
# inicio: número de inicio de la secuencia

for indice, valor in enumerate(lista_productos, start=1):
    print(f"{indice}. {valor}")