# anotaciones de tipo
# capacidad de especificar el tipo de dato que se espera en los argumentos de una función

a: int = 400 # variable a espera un tipo entero

def suma(a: int, b: int) -> int: # la función suma espera dos argumentos de tipo entero y retorna un entero
    return a + b

suma(40, 85)

def saludo(nombre:str, veces:int=1) -> str:
    return f"Hola {nombre}! " * veces

print(saludo('lucia'))
print(saludo('lucia', 3))