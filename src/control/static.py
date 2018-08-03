from bottle import route, static_file

@route('/static/<filename>')
def css(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/css')

@route('/static/fontes/<filename>')
def fontes(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/fontes')

@route('/static/js/<filename>')
def js(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/js')

@route('/static/img/<filename>')
def img(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img')

@route('/GLOBAL/<path:path>')
def global_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/GLOBAL')

@route('/GLOBAL/player')
def global_player():
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(root='././jogo/GLOBAL/player')

@route('/ASSETS/<path:path>')
def assets_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/ASSETS')

@route('/UV1/<path:path>')
def uv1_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/UV1')