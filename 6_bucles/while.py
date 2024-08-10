
# while - bucle
# quiero imprimir 10 veces la palabra hola

contador = 1

while contador <= 10:
    print(contador)
    contador += 1


# registro de productos - ejemplo de uso de while

lista_productos = []
producto = ''

while producto.lower() != 'finalizar':
    producto = input('Ingresa un producto: (escriba finalizar al terminar de ingresar los productos) ')
    lista_productos.append(producto)

lista_productos.remove('finalizar')
# print('Los productos ingresados son: ', lista_productos)

print('\nLista de productos:', lista_productos)

contador = 1
indice = 0

while indice < len(lista_productos):
    print(f"{contador}. {lista_productos[indice]}")
    indice += 1
    contador += 1