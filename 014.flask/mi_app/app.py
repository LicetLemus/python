from flask import Flask, render_template, url_for, request

app = Flask(__name__) # __name__ is a special variable in Python that is the name of the module, app of the Flask. Module name is __main__ when it is run from the command line.
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
# for execute of the server you need to run the next command: flask --app hello run
# debug mode: The server will reload itself each time you make a change in the code.
# for execute of debug mode you need to run the next command: flask --app hello --debug run
# ruotes and views functions

# filter 
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%y')

#functions personalize

from datetime import datetime

def repeat(s, n):
    return s * n

@app.route('/')
def index():
    # return '<h1>Página de Inicio</h1>'
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('code', code = 'print("hola")')) 
    name = 'Licet'
    friends = ['Alejandra', 'Luis', 'Pedro', 'Juan']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        date = date,
        repeat = repeat
        )

#string <string:name>
#int <int:id>
#float <float:price>
#path <path:file>
#uuid <uuid:id>
@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    my_date = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data = my_date)


# we can obtain values from the URL <name>
# Escape of the HTML: 


from markupsafe import escape # escape function to avoid XSS attacks
@app.route('/code/<path:code>')
def code(code):
    return f'''
            <p>Hola, ¿como estas?</p>
            <code>El código es: {escape(code)}</code>'''


#crear formulario con wtform : se debe installar pip install flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class Register_user(FlaskForm):
    username = StringField("Nombre de usuario: ", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Contraseña: ", validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField("Registrar ")


#registrar usuarios
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = Register_user()
    print(request.form)
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f'Nombre de usuario: {username}, contraseña: {password}'
    
    
        
    
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
        
    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f'Nombre de usuario: {username}, contraseña: {password}'
    #     else:
    #         error = """ Nombre usuario debe tener entre 4 y 25 caracteres
    #         y la constraseña debe tener entre 6 y 40 caracteres
    #         """
    #     return render_template('auth/register.html', form = form, error = error)
    
    return render_template('auth/register.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)