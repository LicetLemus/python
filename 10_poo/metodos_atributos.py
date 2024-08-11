# metodo de instancia: es un metodo que pertenece a un objeto, es decir, se puede acceder a el a traves
# de un objeto de la clase.


class Animal:
    def __init__(self, especie, edad) -> None: # constructor de la clase Animal con atributos
        self.especie = especie
        self.edad = edad
        
    def info(self):
        print(f"Especie: {self.especie}, Edad: {self.edad}")
        
animal1 = Animal('Canino', 10) # objeto de la clase Animal
animal2 = Animal('Felino', 5) # objeto de la clase Animal

print(animal1.info())
print(animal2.especie)