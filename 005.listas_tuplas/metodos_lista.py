# metodos de listas 


frutas = ["manzana", "naranja", "platano"]

frutas.append("uva") # ['manzana', 'naranja', 'platano', 'uva']


vegetales = ["tomate", "lechuga", "pepino"]

# extender la lista de frutas con la lista de vegetales

frutas.extend(vegetales) # ['manzana', 'naranja', 'platano', 'uva', 'tomate', 'lechuga', 'pepino']


#inserar un elemento en una posición específica

frutas.insert(1, "pera") # ['manzana', 'pera', 'naranja', 'platano', 'uva', 'tomate', 'lechuga', 'pepino']

# quitar un elemento de la lista

frutas.remove("naranja") # ['manzana', 'pera', 'platano', 'uva', 'tomate', 'lechuga', 'pepino']

# quitar un elemento de la lista por su índice

frutas.pop(2) # ['manzana', 'pera', 'uva', 'tomate', 'lechuga', 'pepino']

# quitar el último elemento de la lista

frutas.pop() # ['manzana', 'pera', 'uva', 'tomate', 'lechuga']

# indice de un elemento en la lista

indice = frutas.index("uva") # 2

# contar cuantas veces aparece un elemento en la lista

frutas.count("uva") # 1

# invertir el orden de los elementos de la lista

frutas.reverse() # ['lechuga', 'tomate', 'uva', 'pera', 'manzana']