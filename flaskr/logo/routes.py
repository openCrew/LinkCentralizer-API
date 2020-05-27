from flask import Blueprint

logo = Blueprint(
    'logo',
    __name__,
)

@logo.route('/api/logo')
def show_logo():

    return 'Logo!'
