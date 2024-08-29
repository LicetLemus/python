# condicioneales anidados

# Ingreso de datos

entrada_usuario = int(input("ingresa un numero: "))

if entrada_usuario > 0:
    print("es par positivo" if entrada_usuario % 2 == 0 else "es impar positivo")
elif entrada_usuario < 0: #elif es una abreviacion de else if 
    print("es par negativo" if entrada_usuario % 2 == 0 else "es impar negativo") 
else:
    print("el numero es 0") 
