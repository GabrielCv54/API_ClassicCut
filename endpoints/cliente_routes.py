from flask import request,jsonify,Blueprint
from database.cliente_db import( create_cliente,get_all_clients,get_one_client,delete_client,update_client,CustomerNotFound )


client_blueprint = Blueprint('clientes',__name__)

@client_blueprint.route('/barbearia/clientes',methods=['GET'])
def get_clients():
    return jsonify(get_all_clients()),200

@client_blueprint.route('/barbearia/cliente/<int:id>',methods=['GET'])
def get_client(id):
    try:
        return jsonify(get_one_client(id)),200
    except CustomerNotFound:
        return jsonify({'O cliente não existe ou não foi encontrado!!'}),404

@client_blueprint.route('/barbearia/cliente',methods=['POST'])
def criar_novo_cliente():
    try:
        new_client = request.get_json()
        create_cliente(data=new_client)
        return jsonify({'Cliente cadastrado com sucesso!'}),201
    except CustomerNotFound:
        return jsonify({'Erro':'Algum erro ocorreu (digitação incorreta,atributo inexistente ou algo do tipo. Por favor tente novamente fazer a requisição!)'}),404
    
@client_blueprint.route('/barbearia/cliente/<int:id>',methods=['PUT'])
def atualizar_cliente(id):
    try:
        updated = request.json
        update_client(id,updated)
        return jsonify({'Cliente atualizado com sucesso'}),201
    except CustomerNotFound:
        return jsonify({'Erro':'Verifique novamente o id do cliente'}),404
    
@client_blueprint.route('/barbearia/cliente/<int:id>',methods=['DELETE'])
def deletar_cliente(id):
    try:
        return jsonify(delete_client(id)),204
    except CustomerNotFound:
        return jsonify({'Erro':'Verifique novamente o id do cliente'}),404