# modulos -> saludos.py son funciones que se pueden reutilizar en otros archivos
# se pueden importar en otros archivos con la palabra reservada import seguido del nombre del archivo sin la extensión .py

import random # modulo que viene dentro del lenguaje.
from typing import List, Dict # modulo que viene dentro del lenguaje.

def formato_aleatorio() -> str:
    formatos = [
        'Hola {}!',
        'Hola {}! Cómo estás?',
        'Hola {}! Qué tal tu día?',
        'Hola {}! Qué tal tu día?'
    ]
    return random.choice(formatos)


def hola(nombre:str) -> str:
    if nombre == '':
        return "Error: Nombre vacio"
    saludo = formato_aleatorio().format(nombre)
    return saludo


def holas(nombres:List) -> Dict:
    saludos = {}
    
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
        
    return saludos


nombres = ['Lucia', 'Pedro', 'Juan', 'Maria']
