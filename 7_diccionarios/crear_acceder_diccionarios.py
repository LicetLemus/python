# diccionarios en python son una estructura de datos que permite almacenar pares de clave-valor (key-value) 

mi_diccionario = {}

print(type(mi_diccionario)) # <class 'dict'>

datos_personales = {
    'nombre': 'Juan',
    'edad': 25,
    'ciudad': 'Bogotá'
}

# Acceder a un valor de un diccionario

datos_personales["nombre"] # 'Juan'

# para saber si una clave existe en un diccionario se puede usar el operador in

'apellido' in datos_personales # False

# metodo get para acceder a un valor de un diccionario

datos_personales.get('nombre') # 'Juan'
datos_personales.get('apellido', 'no especificado') # 'no especificado'