# En python se define una función con la palabra reservada def

def saludar(name):
    print(f'Hola {name}!')
    
saludar('Licet')

def mensaje(name, mensaje):
    return f'Hola {name}! {mensaje}'

print(mensaje('Licet', 'Bienvenida a Python'))

def suma(a, b):
    return a + b

print(suma(10, 30))