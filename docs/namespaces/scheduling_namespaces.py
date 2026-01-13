from flask_restx import Namespace,Resource,fields
from endpoints.scheduling_routes import update_scheduling,create_new_scheduling, delete_scheduling,get_all_schedulings,get_one_scheduling

scheduling_ns = Namespace('Agendamento',description='Operações relacionadas a agendamentos')

class Time(fields.Raw):
    def format(self, value):
        if value is None:
            return None
        elif isinstance(value, str):
         return value
        value.strftime('%H:%M:%S')
    
scheduling_model = scheduling_ns.model('Agendamento',{
    'dia': fields.Date(required=True,description="Dia do agendamento(YYYY-MM-DD)",example='2025-01-11'),
    'horário': fields.String(required=True,description='Hora do agendamento(HH:MM:SS)',example='17:30:00'),
    'barbeiro': fields.Integer(required=True,description='Id do barbeiro que realizará o agendamento'),
    'cliente':fields.Integer(required=True, description='Cliente que solicitou o agendamento')
})

scheduling_output_model = scheduling_ns.model('AgendamentoOutput',{
    'id':fields.Integer(description='Id do agendamento'),
    'dia': fields.Date(description="Dia do agendamento"),
    'horário': Time(description='Hora do agendamento'),
    'barbeiro': fields.Integer(description='Id do barbeiro que realizará o agendamento'),
    'cliente':fields.Integer(description='Id do cliente que solicitou o agendamento')

})

@scheduling_ns.route('/')
class SchedulingResource(Resource):
    @scheduling_ns.marshal_list_with(scheduling_output_model)
    def get(self):
        return get_all_schedulings()
    
    @scheduling_ns.expect(scheduling_model)
    def post(self):
        data = scheduling_ns.payload
        create_new_scheduling(data)
        return {'Sucesso':'Agendamento criado com sucesso'},201
    
@scheduling_ns.route('/<int:id>')
class SchedulingIdResource(Resource):
    @scheduling_ns.marshal_list_with(scheduling_output_model)
    def get(self,id):
        scheduling = get_one_scheduling(id)
        return scheduling,200
    
    @scheduling_ns.expect(scheduling_model)
    def put(self,id):
        scheduling = scheduling_ns.payload
        update_scheduling(id,scheduling)
        return {'Sucesso':'Agendamento atualizado com sucesso'},201
    
    def delete(self,id):
       delete_scheduling(id)
       return {'Sucesso':'Agendamento deletado com sucesso'},204