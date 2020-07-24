from flask_jwt import JWT


def init_app(app, *args):
    JWT(app, *args)
