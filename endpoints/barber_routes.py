from flask import jsonify,request,Blueprint
from database.barber_db import (
   create_new_barber,delete_barber,BarbeiroNaoEncontrado,get_all_barbers,get_one_barber,update_barber,
    )
import os 

#Usar isso daqui para autenticação da API
# secret_key = os.getenv('chave secreta','Key')

barber_blueprint = Blueprint('barbeiros',__name__)

@barber_blueprint.route('/barbearia/barbeiros',methods=['GET'])
def mostrar_barbeiros():
    return jsonify(get_all_barbers()),200

@barber_blueprint.route('/barbearia/barbeiro/<int:id>',methods=['GET'])
def mostrar_barbeiro_por_id(id):
      try:
         return jsonify(get_one_barber(id)),200
      except BarbeiroNaoEncontrado:
           return jsonify({'Erro':'Esse barbeiro não existe ou não foi encontrado'}),404


@barber_blueprint.route('/barbearia/barbeiro',methods=['POST'])
def criar_novo_barbeiro():
   try:
    data = request.get_json()
    post = create_new_barber(data)
    return jsonify({'Mensagem':'Barbeiro criado!'}),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi cadastrado!!'}),404
   
@barber_blueprint.route('/barbearia/barbeiro/<int:id>',methods=['PUT'])
def atualizar_barbeiro(id):
   try:
    updated_data = request.json
    put = update_barber(id,updated_data)
    return jsonify({'Mensagem':'Barbeiro Atualizado!'}),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi encontrado!'}),404

@barber_blueprint.route('/barbearia/barbeiro/<int:id>',methods=['DELETE'])
def deletar_barbeiro(id):
     try:
        deleted_barber = delete_barber(id)
        return jsonify({'Mensagem':'Barbeiro Excluido'}),200
     except BarbeiroNaoEncontrado:
      return jsonify({'Erro':'Barbeiro com esse id não foi encontrado'}),404


