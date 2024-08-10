# break en los bucles en python nos permite salir de un bucle antes de que se complete su ejecución.
# continue en los bucles en python nos permite saltar a la siguiente iteración del bucle, sin ejecutar el código que se encuentra después de la palabra clave continue.


#break 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in range(11):
    if numero == 5:
        break
    # print(numero)

#continue

for numero in range(11):
    if numero == 5:
        continue
    print(numero)