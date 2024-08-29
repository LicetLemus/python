# entonrno virtual en python es una herramienta que nos permite crear entornos de desarrollo aislados para cada proyect

"""
Cuando se usa por ejemplo pip3 install flask, se instala en el entorno global de python - en el ordenador y usarlo
en todos los proyectos, si se quiere instalar en un entorno virtual se debe hacer lo siguiente:

1. Crear un entorno virtual: python3 -m venv nombre_entorno
2. se crea una carpeta con el nombre_entorno y dentro de ella se crea una carpeta llamada bin, lib, include
3. Activar el entorno virtual: source nombre_entorno/bin/activate
4. Desactivar el entorno virtual: deactivate

5. para eliminar el entorno virtual se debe eliminar la carpeta creada con el nombre_entorno

"""