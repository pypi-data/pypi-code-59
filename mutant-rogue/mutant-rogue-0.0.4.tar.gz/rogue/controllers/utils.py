from  termcolor import colored

def auth_error(app):
    token = app.config.get('rogue','token')
    if token:
        msg = colored('Session expired please execute login again','red')
    else:
        msg = colored('You need execute login first','red')

    app.render({'msg': msg } ,'msg.jinja2')
    return False