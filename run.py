from app import db,api
from endpoints.barber_routes import barber_blueprint
from endpoints.cliente_routes import client_blueprint


api.register_blueprint(barber_blueprint)
api.register_blueprint(client_blueprint)

#db.create_all(api)

with api.app_context():
    db.create_all()


if __name__ == '__main__':
    api.run(debug=True)