"""
Manejo de archivos: abrir (open), leer (r), escribir (w) y cerrar (close)
la estrucutra de open es open("nombre del archivo", "modo de apertura")
"""

# Manejo de archivos: abrir, leer, escribir y cerrar

try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError as e:
    print(f"El archivo no existe: {e}")
    print("Se creara un archivo nuevo")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola, este es un archivo de texto")
else:
    print("El archivo se ha leido correctamente")
    print(contenido)
