lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

# concatenar listas

lista_3 = lista_1 + lista_2 # [1, 2, 3, 4, 5, 6]

# repetir elementos de una lista

lista_4 = lista_1 * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# sacar el máximo y mínimo de una lista

maximo = max(lista_1) # 3
minimo = min(lista_1) # 1

# sacar una sublista de una lista original (slice) 

sublista = lista_1[1:3] # [2, 3]


# sacar el índice de un elemento en una lista

indice = lista_1.index(2) # 1

# ordernar una lista .sort()

lista_1.sort() # [1, 2, 3]
lista_1.sort(reverse=True) # [3, 2, 1]
sorted(lista_1) # [1, 2, 3]
