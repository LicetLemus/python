import saludos #importamos el archivo saludos.py

# from saludos import hola, holas

print(saludos.hola('carla'))

nombres_user= ['Carlo', 'Maca', 'Marco', 'Marta']
saludos = saludos.holas(nombres_user)

for saludo in saludos.items():
    print(saludo)