from flask import Flask, render_template



app = Flask(__name__) # __name__ is a special variable in Python that is the name of the module, app of the Flask. Module name is __main__ when it is run from the command line.

# for execute of the server you need to run the next command: flask --app hello run
# debug mode: The server will reload itself each time you make a change in the code.
# for execute of debug mode you need to run the next command: flask --app hello --debug run
# ruotes and view functions


@app.route('/index')
@app.route('/')
def index():
    # return '<h1>Página de Inicio</h1>'
    name = ''
    return render_template('index.html', name=name)

#string <string:name>
#int <int:id>
#float <float:price>
#path <path:file>
#uuid <uuid:id>
@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
def hello(name = None, age = None):
    if name == None and age == None:
        return '<h1>Hola, Mundo!</h1>'
    elif name != None and age == None:
        return f'<h1>Hola, {name}!</h1>'
    else:
        return f'<h1>Hola, {name}! tienes {age} años y el doble de tu edad es: {age * 2}</h1>'


# we can obtain values from the URL <name>
# Escape of the HTML: 


from markupsafe import escape # escape function to avoid XSS attacks
@app.route('/code/<path:code>')
def code(code):
    return f'''
            <p>Hola, ¿como estas?</p>
            <code>El código es: {escape(code)}</code>'''
