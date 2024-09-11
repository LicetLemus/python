from flask import Blueprint


bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def list():
    return 'List task'

@bp.route('/create')
def create():
    return 'Create task'