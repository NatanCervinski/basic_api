import os
from flask import Flask
from flask_restful import Api
from resources.item_resource import Item, ItemList
from security import authenticate, identity
from ext import auth
from ext.db import db
from resources.user_resource import UserRegister
from resources.store_resource import Store, StoreList

# from flask_jwt import JWT



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', "sqlite:///data.db")
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

if __name__ == '__main__':
    app.run()

# api.add_resource(Item, '/item/<string:name>')
