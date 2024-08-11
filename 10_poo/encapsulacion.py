# encapsulacion: es un mecanismo que restringe el acceso a algunos métodos y atributos de un objeto.
# __ atributo: es un atributo privado, es decir, solo puede ser accedido dentro de la clase donde fue declarado.

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
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad}, Nombre: {self.__nombre}"

mascota1 = Mascota('Felino', 5, 'Mishi')
mascota1.set_nombre('firulais')
print(mascota1.get_nombre())