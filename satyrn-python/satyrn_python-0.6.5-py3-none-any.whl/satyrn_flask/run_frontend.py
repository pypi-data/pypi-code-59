import platform
import os


def run():
    try:
        import flask
    except ImportError as e:
        os.system("python3 -m pip install --upgrade flask")

    try:
        import networkx
    except ImportError as e:
        os.system("python3 -m pip install --upgrade networkx")

    try:
        import matplotlib
    except ImportError as e:
        os.system("python3 -m pip install --upgrade matplotlib")

    system = platform.system()

    if system == "Linux" or system == "Darwin":
        os.system("export FLASK_APP=satyrn_flask")
        os.system("export FLASK_ENV=development")

    elif system == "Windows":
        os.system("set FLASK_APP=satyrn_flask")
        os.system("set FLASK_ENV=development")

    os.system("flask run")
