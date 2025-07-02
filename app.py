from endpoints.barber_routes import api
from flask_sqlalchemy import SQLAlchemy
from .database.barber_db import db

api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#api['JSON_SORT_KEYS'] = False

with api.app_context():
   db.create_all()

if __name__ == '__main__':
    api.run(debug=True)
