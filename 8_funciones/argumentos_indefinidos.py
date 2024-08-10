# argumentos indefinidos en funciones en python son aquellos que no tienen un número fijo de argumentos
# se utiliza el operador * para indicar que los argumentos son indefinidos

def args_indefinidos(*args):
    for arg in args:
        print(arg)
        
args_indefinidos('Hola', 24, True, {'nombre': 'Licet', 'edad':28})

# argumentos por nombre debo utilizar kw arguments y el operador **

def args_por_nombre(**kwarguments):
    print(kwarguments)
    
args_por_nombre(nombre='Licet', edad=28, ciudad='Bogotá')

# combinar tipos de argumentos

def combinar_args(a, *args, **kwarguments):
        print(a)
        print(args)
        print(kwarguments)
        
combinar_args('Hola', 24, True, 'mundo', nombre='luis', edad=28)
