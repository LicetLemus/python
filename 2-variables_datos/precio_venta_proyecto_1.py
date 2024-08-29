"""

 calcula el precio de venta de un producto

 Enunciado: Dado el precio de venta de un producto, se debe calcular el 
 impuesto general a las ventas (IVG) que es del 18%, y a partir de eso, 
 determinar el precio de venta final.

 mejora: En esta practica, vamos a crear un prograa en python que permita 
 al usuario ingresar el valor de venta del producto. Luego, el sistema 
 realizará los calculos necesarios para hallar el IVG y el precio de venta final.

"""

# Definir las variables

precio_venta = input("Ingrese el precio de venta del producto: ")

IVG = 0.18
impuesto_IVG = float(precio_venta) * IVG
precio_venta_final = float(precio_venta) + impuesto_IVG

print("El precio de venta final es: ", precio_venta_final)