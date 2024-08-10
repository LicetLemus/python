# lista en python es una estructura de datos que permite almacenar una colección de elementos

# Crear una lista

colores = ['rojo', 'verde', 'azul', 'amarillo']

colores[0] # 'rojo'
len(colores) # 4


# agregar un elemento a la lista
colores.append('naranja')

# quitar un elemento de la lista
colores.remove('verde')

# insertar un elemento en una posición específica
colores.insert(1, 'blanco')

print(colores) # 

# modificar un elemento de la lista
colores[0] = "purpura"
print(colores) # ['purpura', 'blanco', 'azul', 'amarillo', 'naranja']


# in 

if 'blanco' in colores:
    print('blanco está en la lista')