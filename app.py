from flask import Flask
from flask_restful import Api
from second_api.resources.item_resource import Item, ItemList
from second_api.security import authenticate, identity
from second_api.ext import auth
from second_api.ext.db import db
from second_api.resources.user_resource import UserRegister
from second_api.resources.store_resource import Store, StoreList

# from flask_jwt import JWT


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "asdasdsadasdsadasdsadasdsadasdsadasd"
    api = Api(app)

    @app.before_first_request
    def create_table():
        db.create_all()

    db.init_app(app)
    auth.init_app(app, *[authenticate, identity])
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(UserRegister, "/register")
    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    return app


# api.add_resource(Item, '/item/<string:name>')
