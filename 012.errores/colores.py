# gestionar excepciones - crear las excepciones y controlarlas
# raise - se usa para lanzar una excepcion y se puede personalizar el mensaje de error

# crear una classe de excepcion hereda de Exception

class ColorNoValido(Exception):
    def __init__(self, color):
        super().__init__(f"Error: el color {color} no esta en la lista de colores")
        

def colores(color):
    colores = ["rojo", "verde", "azul", "amarillo", "naranja", "blanco",]
    
    for item in colores:
        if color == item:
            print(f"El color {color} esta en la lista de colores")
        if color not in colores:
            # raise Exception(f"Error: el color {color} no esta en la lista de colores")
            raise ColorNoValido(color)
        
try:
    colores("violeta")
except ColorNoValido as e:
    print(f"Error: {e}")
        
# colores("violeta") # raise EOFError(f"Error: el color {color} no esta en la lista de colores")
# colores("violeta") # return f"El color {color} esta en la lista de colores"


