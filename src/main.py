from bottle import default_app, run, template, route
from control.route import *
from control.static import *
from control.static_game import *

def main():
    import bottle
    import os

    view_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'view')
    bottle.TEMPLATE_PATH.insert(0, view_path)

    application = default_app()

    run(host='localhost', port=8080, server='gunicorn', workers=4)

@route('/error403')
def error403():
    return template('error403.tpl')


if __name__ == '__main__':
    main()
