from flask import Blueprint

catalog = Blueprint(
    'catalog',
    __name__,
)


@catalog.route('/api/catalog')
def show_logo():
    return 'Logo!'
