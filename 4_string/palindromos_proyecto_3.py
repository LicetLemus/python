palabra_usuario = input("Introduce una palabra: ")

palabra_usuario = palabra_usuario.replace(' ', '').lower()

palindromo = palabra_usuario[::-1]

if palabra_usuario == palindromo:
    print("La palabra es un palíndromo.")
else: 
    print("La palabra no es un palíndromo.")