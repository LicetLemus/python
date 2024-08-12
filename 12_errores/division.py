# control de excepciones: es una forma de controlar los errores de excepcion

"""
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero diferente a cero: "))

resultado = a / b

print(f"el resultado entre {a}/{b} es {resultado}")
"""


# si el usuario ingresa un cero, se produce un error de excepcion - ZeroDivisionError por lo tanto 
# se pueden usar las clausulas try y except para controlar el error y capturar el mensaje de error

try: 
    
    a = int(input("Ingrese un numero entero: "))
    b = int(input("Ingrese otro numero entero diferente a cero: "))
        
    resultado = a / b

except ValueError:
    print("Error: Debe ingresar un numero entero")
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
    
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"el resultado entre {a}/{b} es {resultado}")
    
print("Fin del programa")

# si no se usan las clausulas try y except, el programa se detiene y se muestra un mensaje de error
# al usar las clausulas try y except, se controla el error y se muestra un mensaje personalizado ademas
# de que el programa no se detiene y se sigue ejecutando