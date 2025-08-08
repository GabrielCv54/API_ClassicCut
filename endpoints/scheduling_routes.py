from database.scheduling_db import (get_all_schedulings,get_one_scheduling,create_new_scheduling,update_scheduling,delete_scheduling,SchedulingNotFound)
from flask import jsonify,Blueprint,request

agendamento_blueprint = Blueprint('agendamentos',__name__)

@agendamento_blueprint.route('/barbearia/agendamentos',methods=['GET'])
def mostrar_agendamentos():
    return jsonify(get_all_schedulings()),200

@agendamento_blueprint.route('/barbearia/agendamentos/<int:id>',methods=['GET'])
def mostrar_um_agendamento(id):
    try:
        return jsonify(get_one_scheduling(id)),200
    except SchedulingNotFound:
        return jsonify({'Erro':'O agendamento não foi encontrado!!'}),404
    
@agendamento_blueprint.route('/barbearia/agendamentos',methods=['POST'])
def criar_novo_agendamento():
        new_scheduling = request.get_json()
        create_new_scheduling(new_scheduling)
        return jsonify({'Sucesso':'Agendamento confirmado!!'}),201

@agendamento_blueprint.route('/barbearia/agendamentos/<int:id>',methods=['PUT'])
def atualizar_agendamento(id):
    try:
        data_updated = request.json
        update_scheduling(id,data_updated)
        return jsonify({'Sucesso':'Agendamento atualizado!!'}),201
    except SchedulingNotFound: 
        return jsonify({'Erro':'Agendamento não encontrado!'}),404
    
@agendamento_blueprint.route('/barbearia/agendamentos/<int:id>')
def deletar_agendamento(id):
    try:
        delete_scheduling(id)
        return jsonify({'Sucesso':'Agendamento excluído!!'}),204
    except SchedulingNotFound:
        return jsonify({'Erro':'Agendamento não encontrado!!!'}),404