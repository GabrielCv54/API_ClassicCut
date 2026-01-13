from flask_restx import fields,Resource,Namespace
from database.barber_db import (update_barber,get_one_barber,get_all_barbers,delete_barber,delete_all_barbers,create_new_barber)

barber_ns = Namespace('barbeiros',description='Operações de Barbeiro')

barber_model = barber_ns.model('Barbeiro',{
    'id':fields.Integer(required=True,description='Id do barbeiro'),
    "barbeiro": fields.String(required=True,description='Nome do barbeiro'),
    "idade":fields.Integer(description="Idade do barbeiro"),
    "local de trabalho":fields.String(required=True,description="Local onde o barbeiro trabalha"),
    "agendamentos": fields.List(fields.Integer(required=True,description="Agendamento(s) que o barbeiro realizará"))
            })

barber_output_model = barber_ns.model('BarbeiroOutput',{
    "id":fields.Integer(description="Id do barbeiro"),
    'barbeiro':fields.String(description="Nome do barbeiro"),
    "idade":fields.Integer(description="Idade do barbeiro"),
    'local de trabalho':fields.String(description="Local onde o barbeiro trabalha"),
    'agendamentos':fields.List(fields.Integer(description='Agendamento(s) que ele realizará'))
    })

@barber_ns.route('/')
class BarbeiroResource(Resource):
    @barber_ns.marshal_list_with(barber_output_model)
    def get(self):
        return get_all_barbers()
    
    @barber_ns.expect(barber_model)
    def post(self):
        data = barber_ns.payload
        create_new_barber(data)
        return {'Sucesso':'Barbeiro criado'},201
    
@barber_ns.route('/<int:id>')
class BarbeiroIdResource(Resource):
    @barber_ns.marshal_with(barber_output_model)
    def get(self,id):
        return get_one_barber(id)
    
    @barber_ns.expect(barber_model)
    def put(self,id):
        data = barber_ns.payload
        update_barber(id,data)
        return data,201

    def delete(self,id):
      delete_barber(id)
      return {}, 204