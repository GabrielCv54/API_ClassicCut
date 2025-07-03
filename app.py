from flask_sqlalchemy import SQLAlchemy
from flask import Flask

""" import jwt
 """
api = Flask(__name__)
db= SQLAlchemy()

api.config['PORT'] = 5000
api.config['DEBUG'] = True
api.config['HOST'] = '0.0.0.0'
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#api['JSON_SORT_KEYS'] = False

db.init_app(api)

with api.app_context():
   db.create_all()

if __name__ == '__main__':
    api.run(debug=True)
