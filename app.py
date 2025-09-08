from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_jwt_extended  import JWTManager
import os
""" import jwt
 """

api = Flask(__name__)
jwt = JWTManager(api)

api.config['JWT_SECRET_KEY'] = os.environ.get('key_jwt','Key')
api.config['JSON_AS_ASCII'] = False
api.config['PORT'] = 5000
api.config['DEBUG'] = True
api.config['HOST'] = '0.0.0.0'
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(api)

#migrate = Migrate(api,db)
