#bucle for 

datos = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

for valor in datos:
    print(valor) # devuelve las claves del diccionario
    
for clave, valor in datos.items():
    print(clave, valor) # devuelve las claves y valores
    
for clave in datos.keys():
    print(clave) # devuelve las claves