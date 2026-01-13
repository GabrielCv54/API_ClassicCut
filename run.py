from app import db,api
from endpoints.barber_routes import barber_blueprint
from endpoints.cliente_routes import client_blueprint
from endpoints.scheduling_routes import agendamento_blueprint
from endpoints.auth_routes import auth_blueprint
from docs.swagger import api_s
from docs.namespaces.barber_namespace import barber_ns
from docs.namespaces.client_namespaces import client_ns

#Registro dos blueprints
api.register_blueprint(barber_blueprint)
api.register_blueprint(client_blueprint)
api.register_blueprint(auth_blueprint)
api.register_blueprint(agendamento_blueprint)

#Registro dos namespaces
api_s.add_namespace(barber_ns)
api_s.add_namespace(client_ns)

with api.app_context():
    db.create_all()


if __name__ == '__main__':
    api.run(debug=api.config['DEBUG'],port=api.config['PORT'],host=api.config['HOST'])