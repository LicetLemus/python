# condicional if else

if 4 == 4:
    print("4 es igual a 4")

if 4 != 5:
    print("4 es diferente de 5")

if 4 == 6:
    print("4 es igual a 6") # no se imprime porque la condicion es falsa


if 5 == 7:
    print("5 es igual a 7") 
else: 
    print("5 no es igual a 7") 


# ejemplo de uso-----------------------------------------------------

entrada_usuario = int(input("ingresa un numero: "))
numero_secreto = 7

if entrada_usuario % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")