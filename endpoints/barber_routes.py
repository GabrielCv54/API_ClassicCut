from flask import jsonify,request,Flask,make_response
from database.barber_db import (
    Barbeiro,create_new_barber,delete_barber,BarbeiroNaoEncontrado,get_all_barbers,get_one_barber,update_barber
    )

class Error(Exception):
    pass


api = Flask(__name__)

barbershop= {
    'Barbeiros':[
        {'id':1,'Nome':'Edgar Rodrigues','Idade':44,'Cortes Marcados':[100,200,300,400,500],'Local de Trabalho':'Their Space'}
        ],
    'Clientes':[
        {'id':100,'Nome':'Lucas Moura','Idade':21,'CPF':459896614,'Horário_agendamento':'15h30','Dia_agendamento':'Sábado,28 de junho'},{}
        ],
    "Agendamentos":[
        {'id':1,'Dia':'28 de Junho','Cabeleireiro':1,'Cliente':100}
        ]
    }


@api.route('/barbearia/barbeiros',methods=['GET'])
def mostrar_barbeiros():
    return jsonify(get_all_barbers()),200

@api.route('/barbearia/barbeiro/<int:id>',methods=['GET'])
def mostrar_barbeiro_por_id(id):
    '''
    Essa é a parte que valida se os clientes em que o barbeiro vai atender existem ou não
    clients = barbershop['Clientes']
    for c in clients:
        c.get('id')'''
    for barb in barbershop['Barbeiros']:
        if barb.get('id') == id:
            return jsonify(barb),200
    '''Faz parte da mesma parte
          if barb.get('Cortes Marcados') not in c:
            return jsonify({'Erro':'Não é possível continuar, pois esse cliente não existe ou não marcou agendamento ainda!'}),403'''
    return jsonify({'Erro':'Esse barbeiro não foi encontrado ,tente verificar o id dele novamente!'}), 404

@api.route('/barbearia/barbeiro',methods=['POST'])
def criar_novo_barbeiro():
   data = request.json
   barbershop['Barbeiros'].append(data)
   return jsonify(barbershop['Barbeiros']),201

@api.route('/barbearia/barbeiro/<int:id>',methods=['PUT'])
def atualizar_barbeiro(id):
   updated_data = request.json
   for b in barbershop['Barbeiros']:
       if b.get('id') == id:
           b.update(updated_data)
           return jsonify(barbershop['Barbeiros']),201
   return jsonify({'Erro':'O id do barbeiro não existe, tente novamente'}),404

@api.route('/barbearia/barbeiro/<int:id>',methods=['DELETE'])
def deletar_barbeiro(id):
    for barber in barbershop['Barbeiros']:
        if barber.get('id') == id:
            barbershop['Barbeiros'].remove(barber)
            return jsonify({'Mensagem':'Barbeiro excluído com sucesso!!'}),200
    return jsonify({'Erro':'Barbeiro com esse id não foi encontrado'}),404

