from flask import jsonify,request,Blueprint
from database.barber_db import (
   create_new_barber,delete_barber,BarbeiroNaoEncontrado,get_all_barbers,get_one_barber,update_barber,
    )
import os 
from datetime import datetime,timedelta
from flask_jwt_extended import create_access_token,jwt_required

barber_blueprint = Blueprint('barbeiros',__name__)

@barber_blueprint.route('/barbearia/barbeiros',methods=['GET'])
def mostrar_barbeiros():
    return jsonify(get_all_barbers()),200


@barber_blueprint.route('/barbearia/barbeiros/<int:id>',methods=['GET'])
def mostrar_barbeiro_por_id(id):
      try:
         return jsonify(get_one_barber(id)),200
      except BarbeiroNaoEncontrado:
           return jsonify({'Erro':'Esse barbeiro não existe ou não foi encontrado'}),404


@barber_blueprint.route('/barbearia/barbeiros',methods=['POST'])
def criar_novo_barbeiro():
   try:
    data = request.get_json()
    create_new_barber(data)
    return jsonify({'Mensagem':'Barbeiro criado!'}),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi cadastrado!!'}),404

@barber_blueprint.route('/barbearia/barbeiros/login',methods=['POST'])   
def barber_login():
   barbers = get_all_barbers()
   user = request.json.get('user',None)
   password = request.json.get('senha',None)

   for b in barbers:
      if user != f'{b.name}' or password != 'QWPjFGGX':
         return jsonify({'A senha ou o nome do cliente está errado!'}),400

@barber_blueprint.route('/barbearia/barbeiros/<int:id>',methods=['PUT'])
def atualizar_barbeiro(id):
   try:
    updated_data = request.json
    update_barber(id,updated_data)
    return jsonify({'Mensagem':'Barbeiro Atualizado!'}),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi encontrado!'}),404

@barber_blueprint.route('/barbearia/barbeiros/<int:id>',methods=['DELETE'])
def deletar_barbeiro(id):
     try:
        delete_barber(id)
        return jsonify({'Mensagem':'Barbeiro Excluido'}),204
     except BarbeiroNaoEncontrado:
      return jsonify({'Erro':'Barbeiro com esse id não foi encontrado'}),404


