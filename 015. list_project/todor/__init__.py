from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from todor.config import Config


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    # registro de blueprint
    from . import todo

    app.register_blueprint(todo.bp)

    from . import auth

    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    with app.app_context():
        db.create_all()

    return app
