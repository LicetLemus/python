import datetime as dt # importamos el modulo datetime de python para trabajar con fechas y horas
from mi_paquete import modulo1

# from datetime import date as d
# from datetime import datetime as dt
# from datetime import *

hoy = dt.date.today()
ahora = dt.datetime.now()

print(hoy)
print(ahora)

modulo1.saludar()