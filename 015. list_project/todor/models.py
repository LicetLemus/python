from todor import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    # crear usuarios
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # obtener usuarios
    def __repr__(self):
        return f"<User: {self.username}>"


class Todo(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    created_by = db.Column(
        db.Integer,
        db.ForeignKey('user.id'), nullable = False
    )
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default = False)
    

    # crear usuarios
    def __init__(self, created_by, title, desc, state = False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.state = state
        

    # obtener usuarios
    def __repr__(self):
        return f"<Todo: {self.title}>"
