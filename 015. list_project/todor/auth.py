from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    session,
    g,
)

from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from todor import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User(username, generate_password_hash(password, method="pbkdf2:sha256"))

        error = None

        user_name = User.query.filter_by(username=username).first()

        if user_name == None:
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("auth.login"))
        else:
            error = f"El usuario {username}, ya está registrado"

        flash(error)
    return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None

        # validate the dates of the user

        user = User.query.filter_by(username=username).first()

        if user == None:
            error = "Nombre de usuario incorrecto"
        elif not check_password_hash(user.password, password):
            error = "Contraseña incorrecta"

        if error == None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("todo.index"))

        flash(error)
    return render_template("auth/login.html")


@bp.before_app_request  # verifica si se ha iniciado una session
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


@bp.route('/logout')  # verifica si se ha iniciado una session
def logout():
    session.clear()
    return redirect(url_for('index'))


import functools

def login_required(view):
    @functools.wraps(view)
    def wrapper_wraps(**kwargs): # **kwargs multiple args
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapper_wraps
    





# @bp.route("/delete/<id>", methods=["DELETE"])
# def delete(id):

#     user = User.query.filter_by(id=id).first()  # Usa el 'id' de la URL
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return "User deleted successfully", 200
#     else:
#         return "User not found", 404
