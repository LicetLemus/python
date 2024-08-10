# metodos de string

# upper() convierte una cadena de texto a mayúsculas
saludo = "Hola, ¿cómo estás?"
print(saludo.upper()) # HOLA, ¿CÓMO ESTÁS?

# lower() convierte una cadena de texto a minúsculas
print(saludo.lower()) # hola, ¿cómo estás?

# capitalize() convierte la primera letra de una cadena de texto a mayúscula
print(saludo.capitalize()) # Hola, ¿cómo estás?

# title() convierte la primera letra de cada palabra de una cadena de texto a mayúscula
print(saludo.title()) # Hola, ¿Cómo Estás?

# count() cuenta cuantas veces aparece una subcadena en una cadena de texto
print(saludo.count('o')) # 3

# find() devuelve el índice de la primera aparición de una subcadena en una cadena de texto
print(saludo.find('o')) # 1

# rfind() devuelve el índice de la última aparición de una subcadena en una cadena de texto
print(saludo.rfind('o')) # 14

# index() devuelve el índice de la primera aparición de una subcadena en una cadena de texto
print(saludo.index('o')) # 1

# rindex() devuelve el índice de la última aparición de una subcadena en una cadena de texto
print(saludo.rindex('o')) # 14

# startswith() devuelve True si una cadena de texto comienza con una subcadena
print(saludo.startswith('Hola')) # True

# endswith() devuelve True si una cadena de texto termina con una subcadena
print(saludo.endswith('¿cómo estás?)')) # True

# replace() reemplaza una subcadena por otra en una cadena de texto
print(saludo.replace('o', '0')) # H0la, ¿c0m0 estás?

# split() divide una cadena de texto en una lista de subcadenas
print(saludo.split()) # ['Hola,', '¿cómo', 'estás?']

# strip() elimina los espacios en blanco al principio y al final de una cadena de texto
print(saludo.strip()) # Hola, ¿cómo estás?

# lstrip() elimina los espacios en blanco al principio de una cadena de texto
print(saludo.lstrip()) # Hola, ¿cómo estás?

# rstrip() elimina los espacios en blanco al final de una cadena de texto
print(saludo.rstrip()) # Hola, ¿cómo estás?

# join() une una lista de subcadenas en una cadena de texto
print(' '.join(['Hola,', '¿cómo', 'estás?'])) # Hola, ¿cómo estás?

# in operador de pertenencia
print('Hola' in saludo) # True

# not in operador de no pertenencia
print('Hola' not in saludo) # False