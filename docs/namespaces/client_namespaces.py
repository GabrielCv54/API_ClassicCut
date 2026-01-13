from flask_restx import Namespace,Resource,fields
from endpoints.cliente_routes import update_client,create_cliente,delete_client,get_all_clients,get_one_client,CustomerNotFound
from app import api

client_ns = Namespace('Cliente',description='Operações relacionadas aos clientes')

client_model = client_ns.model("Cliente",{
    "name":fields.String(required=True, description="Nome do cliente"),
    "age": fields.Integer(description="Idade do cliente"),
    "telephone": fields.String(required=True, description='Telefone do cliente'),
    "service": fields.String(required=True,description='Serviço que o cliente pediu para ser realizado')
})

cliente_output_model = client_ns.model('ClienteOutput',{
    'id': fields.Integer(description='Id do cliente'),
    'name': fields.String(description='Nome do cliente'),
    'age': fields.Integer(description='Idade do cliente'),
    'telephone': fields.String(description="Telefone do cliente"),
    "service": fields.String(description="Serviço que o cliente pedi ")
})

@client_ns.route('/')
class ClientResource(Resource):
    @client_ns.marshal_list_with(cliente_output_model)
    def get(self):
        return get_all_clients()
    
    @client_ns.expect(client_model)
    def post(self):
        data = client_ns.payload
        create_cliente(data=data)
        return {'Sucesso':'Cliente criado com sucesso'},201

@client_ns.route('/<int:id>')
class ClienteIdResource(Resource):
    @client_ns.marshal_with(cliente_output_model)
    def get(self,id):
        return get_one_client(id)
    
    @client_ns.expect(client_model)
    def put(self,id):
        data = client_ns.payload
        update_client(id,data)
        return data,201
    
    def delete(self,id):
        delete_client(id)
        return {},204
