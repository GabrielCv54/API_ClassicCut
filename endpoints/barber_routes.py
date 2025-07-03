from flask import jsonify,request,make_response
from app import api
from ..database.barber_db import (
   create_new_barber,delete_barber,BarbeiroNaoEncontrado,get_all_barbers,get_one_barber,update_barber,
    )
import os 

#Usar isso daqui para autenticação da API
# secret_key = os.getenv('chave secreta','Key')


'''barbershop= {
    'Barbeiros':[
        {'id':1,'Nome':'Edgar Rodrigues','Idade':44,'Cortes Marcados':[100,200,300,400,500],'Local de Trabalho':'Their Space'}
        ],
    'Clientes':[
        {'id':100,'Nome':'Lucas Moura','Idade':21,'CPF':459896614,'Horário_agendamento':'15h30','Dia_agendamento':'Sábado,28 de junho'},{}
        ],
    "Agendamentos":[
        {'id':1,'Dia':'28 de Junho','Cabeleireiro':1,'Cliente':100}
        ]
    }'''


@api.route('/barbearia/barbeiros',methods=['GET'])
def mostrar_barbeiros():
    return jsonify(get_all_barbers()),200

@api.route('/barbearia/barbeiro/<int:id>',methods=['GET'])
def mostrar_barbeiro_por_id(id):
        return jsonify(get_one_barber(id)),200

@api.route('/barbearia/barbeiro',methods=['POST'])
def criar_novo_barbeiro():
   try:
    data = request.json
    return jsonify(create_new_barber(data)),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi cadastrado!!'}),404
   
@api.route('/barbearia/barbeiro/<int:id>',methods=['PUT'])
def atualizar_barbeiro(id):
   try:
    updated_data = request.json
    return jsonify(update_barber(id,updated_data)),201
   except BarbeiroNaoEncontrado:
       return jsonify({'Erro':'Esse barbeiro não existe ou não foi encontrado!'}),404

@api.route('/barbearia/barbeiro/<int:id>',methods=['DELETE'])
def deletar_barbeiro(id):
     try:
            return jsonify({'Mensagem':'Barbeiro excluído com sucesso!!'}),200
     except BarbeiroNaoEncontrado:
      return jsonify({'Erro':'Barbeiro com esse id não foi encontrado'}),404


