# tuplas son inmutables y se definen con parentesis en lugar de corchetes 


lista = [1, 2, 3, 4]
type(lista) # <class 'list'>

# se puede convertir una lista en una tupla con la función tuple()

tupla_nueva = tuple(lista)

tupla = ()
type(tupla) # <class 'tuple'>

tupla = (1, 2, 3, 4)

# no se puede agregar elementos a una tupla, pero se puede concatenar

tupla = tupla + (5, 6, 7) # (1, 2, 3, 4, 5, 6, 7)

# se puede convertir una tupla en una lista con la función list()

lista_nueva = list(tupla)