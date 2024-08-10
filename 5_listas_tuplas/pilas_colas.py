# pila: sigue el principio LIFO (Last In First Out), es decir, el último elemento en entrar es el primero en salir.

# cola: sigue el principio FIFO (First In First Out), es decir, el primer elemento en entrar es el primero en salir.


# crear una pila

pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila) # [1, 2, 3]

elemento = pila.pop() # 3
print(pila) # [1, 2]
print(elemento) # 3


# crear una cola

cola = []
cola.append(1)
cola.append(2)
cola.append(3)

print(cola) # [1, 2, 3]

elemento = cola.pop(0) # 1
print(cola) # [2, 3]
print(elemento) # 1

# from collections import deque

# cola = deque()
# cola.append(1)
# cola.append(2)
# cola.append(3)

# print(cola) # deque([1, 2, 3])

# elemento = cola.popleft() # 1
# print(cola) # deque([2, 