texto = "Python"

print(texto[0]) # P
print(texto[1]) # y
print(texto[2]) # t
print(texto[3]) # h
print(texto[4]) # o
print(texto[5]) # n
print(texto[-1]) # n
print(texto[-2]) # o

# longitud de una cadena de texto

print(len(texto)) # 6


# slicing en cadenas de texto slice [start:stop:step]

print(texto[0:2]) # Py
print(texto[2:6]) # thon
print(texto[:2]) # Py
print(texto[2:]) # thon
print(texto[-3:-1]) # ho
print(texto[::2]) # Ptos
print(texto[::-1]) # nohtyP
print(texto[:3:2]) # Pt

# inmutabilidad de las cadenas de texto: no se pueden modificar

# texto[0] = 'p' # TypeError: 'str' object does not support item assignment

nuevo_texto = 's' + texto[1:]
print(nuevo_texto) # sython 