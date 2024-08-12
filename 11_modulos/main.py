import datetime as dt # importamos el modulo datetime de python para trabajar con fechas y horas
from mi_paquete import modulo1

# from datetime import date as d
# from datetime import datetime as dt
# from datetime import *

if __name__ == '__main__': # si el modulo se ejecuta como principal
    print('Este es el modulo principal')
    hoy = dt.date.today()
    ahora = dt.datetime.now()

    print(hoy)
    print(ahora)

    modulo1.saludar()
    # modulo1.imprimir_variable()

    print(__name__) # __name__ es una variable especial que nos dice el nombre del modulo en el que estamos trabajando

