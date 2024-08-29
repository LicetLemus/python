"""
    crea un juego que le pida al usuario adivinar un número entre 1 y 100.

    - Genera un número aleatorio entre 1 y 100.
    - El usuario debe ingresar un número con un limite de 10 intentos.
    - Debe ayudar al usuario en cada intento si el número ingresado es mayor o menor al número generado.
    - Muestra el resultado si ganaste o perdite 

"""

import random

print("Bienvenido al juego de adivina el número, ¡empecemos!")

numero_aleatorio = random.randint(1, 100) # Genera un número aleatorio entre 1 y 100
intentos = 10
intentos_realizados = 0


while intentos_realizados < intentos:
    numero_usuario = int(input("Ingresa un número: "))
    intentos_realizados += 1

    if numero_usuario == numero_aleatorio:
        print("¡Felicidades! ¡Adivinaste el número!")
        break
    elif numero_usuario < numero_aleatorio:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")


if intentos_realizados == intentos:
    print("¡Perdiste! El número era: ", numero_aleatorio)

print("¡Gracias por jugar!")
