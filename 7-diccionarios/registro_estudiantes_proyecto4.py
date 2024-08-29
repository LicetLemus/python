"""
Desarrolla un programa en Python para gestionar un sistema de registro de
estudiantes. El sistema deberá permitir:

- Registro de Estudiantes:
    - Capturar in formación de estudiantes desde la terminal, inluyen nombre,
    edad y curso.
    - Almacenar la información en un diccionario.
- Almacenamiento en una lista:
    - Guardar cada diccionario de estudiantes en una lista central.
- Visualización de registro:
    - Mostrar el registro completo de estudiantes, incluyendo sus detalles como
    nombre, edad y curso
"""

registro = []

def registrar_estudiante():
    while True:
        print("Por favor ingrese la información de los estudiantes")
        estudiante = {
            'nombre': input("Nombre: "),
            'edad' : int(input("Edad: ")),
            'curso': input('Curso: '),
        }
        registro.append(estudiante)
        print("Estudiante registrado con éxito")
    
        confirmación = input("Desea continuar ingresando información (s/n): ").lower()
        if confirmación != 's':
            print("Gracias por registrar los estudiantes")
            break


def entrada():
    print("sistema de registro de estudiantes")
    
    while True:
        print("1. Registro de estudiantes")
        print("2. Mostrar registro de estudiantes")
        print("3. Salir")
        opcion = int(input("Por favor seleccione una opción: "))
    
        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            if len(registro) == 0:
                print("No hay estudiantes registrados, por favor registre un estudiante")
            else:
                print("Registro de estudiantes", registro)
        elif opcion == 3:
            print("Gracias por usar el sistema de registro de estudiantes")
            break

entrada()
