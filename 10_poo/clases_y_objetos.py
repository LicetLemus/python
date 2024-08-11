# clase: modelar un objeto del mundo real, de alli se crean los objetos.

class Animal:
    especie = ''
    edad= 0
    

perro = Animal() # perro es un objeto de la clase Animal
perro.especie = 'canino'
perro.edad = 5

print(perro)
print(perro.especie)