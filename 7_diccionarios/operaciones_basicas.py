# operaciones basicas con diccionarios 

# Crear un diccionario vacio

datos_personales = {
    'nombre': 'juan',
    'edad': 25,
    'ciudad': 'Bogotá'
}

# agregar un nuevo par clave-valor a un diccionario

datos_personales['apellido'] = 'Parra'

print(datos_personales) # {'nombre': 'juan', 'edad': 25, 'ciudad': 'Bogotá', 'apellido': 'Parra'}

# modificar un valor de un diccionario

datos_personales['edad'] = 26
print(datos_personales) # {'nombre': 'juan', 'edad': 26, 'ciudad': 'Bogotá', 'apellido': 'Parra'}

datos_personales.update({'edad': 27, 'ciudad': 'Medellín'})
print(datos_personales) # {'nombre': 'juan', 'edad': 27, 'ciudad': 'Medellín', 'apellido': 'Parra'}


# eliminar un par clave-valor de un diccionario

del datos_personales['apellido']
print(datos_personales) # {'nombre': 'juan', 'edad': 27, 'ciudad': 'Medellín'}

datos_personales.pop('edad')
print(datos_personales) # {'nombre': 'juan', 'ciudad': 'Medellín'}

# longitud de un diccionario
len(datos_personales) # 2

# obtener las keys de un diccionario

list(datos_personales.keys()) # ['nombre', 'ciudad']

# obtener los valores de un diccionario
list(datos_personales.values()) # ['juan', 'Medellín']

# obetner los items
datos_personales.items() # dict_items([('nombre', 'juan'), ('ciudad', 'Medellín')])