"""
    crea un programa en Python que simule un sistema de descuentos en un
    restaurante segun el monto de consumo. El programa debe seguir las 
    siguientes instrucciones:

    - Solicita al usuario que ingrese el monto de consumo en el restaurante
    - Aplica descuentos segun las siguientes reglas:
        - Si el monto de consumo es mayor a $50 pero igual o menor a 100$, aplica
        un descuento del 10%
        - Si el monto de consumo es mayor a $100 pero igual o menor a $200, aplica
        un descuento del 20%
        - Si el monto de consumo es mayor a $200, aplica un descuento del 30%
        - Si el monto de consumo es igual o menor a $50, no aplica descuento

    Muestra al usuario un resumen de la cuenta con el monto de consumo, el descuento
    aplicado y el monto final con el descuento.

"""

# Definir las variables
consumo_usuario = float(input("Por favor, ingresa el monto de consumo en el restaurante: "))

# Definir las reglas de descuento

# if consumo_usuario > 50 and consumo_usuario <= 100:
#     descuento = 0.10 * consumo_usuario
#     monto_descuento = consumo_usuario - (consumo_usuario * descuento) 
#     print("El descuento aplicado es: ", descuento)
#     print("El monto final con descuento es: ", monto_descuento)
# elif consumo_usuario > 100 and consumo_usuario <= 200:
#     descuento = 0.20 * consumo_usuario
#     monto_descuento = (consumo_usuario * descuento) + consumo_usuario
#     print("El descuento aplicado es: ", descuento)
#     print("El monto final con descuento es: ", monto_descuento)
# elif consumo_usuario > 200:
#     descuento = 0.30 * consumo_usuario
#     monto_descuento = (consumo_usuario * descuento) + consumo_usuario
#     print("El descuento aplicado es: ", descuento)
#     print("El monto final con descuento es: ", monto_descuento)
# else:
#     print("No aplica descuento")
#     print("El monto final es: ", consumo_usuario)

if consumo_usuario > 50 and consumo_usuario <= 100:
    descuento = 0.10
elif consumo_usuario > 100 and consumo_usuario <= 200:
    descuento = 0.20
elif consumo_usuario > 200:
    descuento = 0.30
else:
    descuento = 0

monto_descuento = consumo_usuario * descuento
total_pagar = consumo_usuario - monto_descuento

print("\nResumen de la cuenta") # \n es un salto de linea
print("El monto de consumo es: ", consumo_usuario)
print("El descuento aplicado es: ", descuento * 100, "%")
print("El monto final con descuento es: ", total_pagar)