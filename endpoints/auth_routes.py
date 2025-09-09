from database.cliente_db import Cliente, CustomerNotFound
from  database.barber_db import Barbeiro
from database.scheduling_db import Agendamento
from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth',__name__)

def get_name_client(name):
    client = Cliente.query.get(name)
    if not client:
       raise CustomerNotFound
    return client.info()

@auth_blueprint.route('/login',methods=['POST'])
def login():
    name = request.json.get('name',None)
    password = request.json.get('password',None)

    client = get_name_client(name)

    if client and client.password == password:
        access_token = create_access_token(identity=client.id)
        return jsonify(access_token=access_token),200
    
    return jsonify({'Erro':'nome ou senha incorretos!!'}),401

