# globales, locales y no locales
# globales: variables que se declaran fuera de una función
# locales: variables que se declaran dentro de una función
# no locales: variables que se declaran en una función anidada y se utilizan en la función padre

variable_global = 'Soy una variable global'

def variable_entornos():
    variable_local = 'Soy una variable local'
    print(variable_local) # Acceso a variable local
    print(variable_global) # Acceso a variable global

# print(variable_local) NameError: name 'variable_local' is not defined
# las variables globales nno pueden ser modificadas dentro de una función a menos que se utilice la palabra reservada global 
# y solo se modifica en el ámbito de la función por fuera de la función sigue siendo la misma variable.

def modificar_variable_global():
    global variable_global
    variable_global = 'Soy una variable global modificada'
    print(variable_global) # imprime 'Soy una variable global modificada'

print(variable_global) # imprime 'Soy una variable global'

variable_entornos()

print('variables globales:-----------------------', globals()) # imprime un diccionario con todas las variables globales
print('Variables locales:------------------------', locals()) # imprime un diccionario con todas las variables locales


# varibles no locales

def funcion_anidada():
    variable_no_local = 'Soy una variable no local'
    def funcion2():
        nonlocal variable_no_local
        variable_no_local = 'Soy una variable no local modificada'
        print(variable_no_local)
    funcion2()
    print(variable_no_local) # imprime 'Soy una variable no local modificada'