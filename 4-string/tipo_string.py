
simple_string = 'Hola Licet!'
doble_string = "Hola Licet!"

# textos grandes 

texto_grande = """ Hola Licet! espero estes muy bien """
texto_grande2 = ''' Hola Licet! espero estes muy bien '''


# concatenar cadenas de texto

nombre = 'Licet'
apellido = 'Lemus'

nuevo_nombre = nombre + ' ' + apellido
print(nuevo_nombre)

print('Hola ' + nombre + ' ' + apellido)
print("Hola " * 3)
print('"Python", es un lenguaje de programación')

# interpolación de cadenas de texto: f-strings es una forma de interpolar cadenas de texto, interpolación es la acción de insertar algo en otra cosa

print(f'Hola {nombre} {apellido}')
print(f'Hola {nombre} {apellido.upper()}')
print(f'Hola {nombre} {apellido.lower()}')
print(f'Hola {nombre} {apellido.capitalize()}')
print(f'Hola {nombre} {apellido.title()}')

# salto de línea en cadenas de texto \n

print('Hola Licet!\nEspero estes muy bien')


# tabulación en cadenas de texto \t

print('Hola Licet!\tEspero estes muy bien')

# longitud de una cadena de texto

print(len('Hola Licet!'))