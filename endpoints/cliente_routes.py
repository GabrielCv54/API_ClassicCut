from flask import request,jsonify,Blueprint
from database.cliente_db import( create_cliente,get_all_clients,get_one_client,delete_client,update_client,CustomerNotFound )
import os

client_blueprint = Blueprint('clientes',__name__)

#key = os.getenv('my_key','s01454')

@client_blueprint.route('/barbearia/clientes',methods=['GET'])
def get_clients():
    return jsonify(get_all_clients()),200

@client_blueprint.route('/barbearia/clientes/<int:id>',methods=['GET'])
def get_client(id):
    try:
        return jsonify(get_one_client(id)),200
    except CustomerNotFound:
        return jsonify({'Erro':'O cliente não foi encontrado!!'}),404

@client_blueprint.route('/barbearia/clientes',methods=['POST'])
def criar_novo_cliente():
        new_client = request.get_json()
        create_cliente(new_client)
        return jsonify({'Sucesso':'Cliente cadastrado com sucesso!'}),201
   
@client_blueprint.route('/barbearia/clientes/<int:id>',methods=['PUT'])
def atualizar_cliente(id):
    try:
        updated = request.json
        update_client(id,updated)
        return jsonify({'Sucesso':'Cliente atualizado com sucesso'}),201
    except CustomerNotFound:
        return jsonify({'Erro':'Verifique novamente o id do cliente'}),404
    
@client_blueprint.route('/barbearia/clientes/<int:id>',methods=['DELETE'])
def deletar_cliente(id):
    try:
        delete_client(id)
        return jsonify({'Mensagem':'Cliente Deletado!!'}),204
    except CustomerNotFound:
        return jsonify({'Erro':'Verifique novamente o id do cliente'}),404