from flask import Blueprint

background = Blueprint(
    'background',
    __name__,
)

@background.route('/api/background')
def show_background():

    return 'Background!'