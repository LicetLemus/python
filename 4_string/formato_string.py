nombre = "Juan"
edad = 25
altura = 1.75

# formato de cadena de texto
print("Hola, mi nombre es " + nombre + ", tengo " + str(edad) + " años y mido " + str(altura) + " metros.")

mensaje = "Hola, mi nombre es %s, tengo %d años y mido %.2f metros." % (nombre, edad, altura)
print(mensaje)

mensaje_2 = "Hola, mi nombre es {}, tengo {} años y mido {:.2f} metros.".format(nombre, edad, altura)
print(mensaje_2)

# f-string

mensaje_3 = f"Hola, me llamo {nombre}, tengo {edad} años y mi altura es {altura:.2f} metros."
print(mensaje_3)