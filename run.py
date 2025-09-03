from app import db,api
from endpoints.barber_routes import barber_blueprint
from endpoints.cliente_routes import client_blueprint
from endpoints.scheduling_routes import agendamento_blueprint


api.register_blueprint(barber_blueprint)
api.register_blueprint(client_blueprint)
api.register_blueprint(agendamento_blueprint)

#db.create_all(api)

with api.app_context():
    db.create_all()


if __name__ == '__main__':
    api.run(debug=api.config['DEBUG'],port=api.config['PORT'],host=api.config['HOST'])