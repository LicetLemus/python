#poliformismo es la capacidad de un objeto de tomar diferentes formas o comportamientos segun el contexto

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
        
    def hablar(self):
        pass
    
    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad}, Nombre: {self.nombre}"
        
mascota1 = Mascota('Felino', 5, 'Mishi')
print(mascota1.__str__())

class Perro(Mascota):
    def hablar(self):
        return "Woof!"

class Gato(Mascota):
    def hablar(self):
        return "Miau!"
    
p = Perro('Canino', 10, 'Firulais')
g = Gato('Felino', 5, 'Miaugu')

print(p.hablar())
print(g.hablar())