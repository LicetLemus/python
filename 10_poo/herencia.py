# herencia en python: es la capacidad de una clase de heredar atributos y metodos de otra clase padre.
# las subclases heredan todos los metodos y atributos de la clase padre.

class Animal:
    def __init__(self, especie, edad) -> None: # constructor de la clase Animal con atributos
        self.especie = especie
        self.edad = edad
        
    def str (self): # metodo especial que retorna una cadena
        return f"Especie: {self.especie}, Edad: {self.edad}"
        
# subclase de la clase Animal

class Mascota(Animal):
    def __init__(self, especie, edad, nombre) -> None:
        Animal.__init__(self, especie, edad)
        self.nombre = nombre
        
    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad}, Nombre: {self.nombre}"
        
mascota1 = Mascota('Felino', 5, 'Mishi')
print(mascota1.info())