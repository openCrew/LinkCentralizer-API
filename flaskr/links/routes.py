from flask import Blueprint

links = Blueprint(
    'links',
    __name__,
)

@links.route('/api/links')
def show_links():

    return 'Links!'