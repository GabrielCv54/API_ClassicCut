from app import db
import datetime
from .barber_db import Barbeiro
from werkzeug.security import check_password_hash,generate_password_hash
import hashlib
from werkzeug.exceptions import HTTPException


class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(70),nullable=False)
    age = db.Column(db.Integer)
    telephone = db.Column(db.String(12),nullable=False)
    service = db.Column(db.String(50),nullable=False)

   
    def __init__(self,name,age,telephone,service):
        self.name = name
        self.age = age
        self.telephone = telephone
        self.service = service
        

    def dicionario(self):
        return {'id':self.id,'name':self.name,'age':self.age,'telephone':self.telephone,'service':self.service}
    
    def info(self):
        return self.dicionario()
    
class CustomerNotFound(HTTPException):
    code = 404
    description = 'O cliente não foi encontrado .'

class DataInvalid(HTTPException):
    code = 400
    description = 'Dados enviados incorretamente, tente de novo.'

class ServerError(HTTPException):
    code = 500
    description = f'Erro no servidor'

def get_all_clients():
     clientes = Cliente.query.all()
     return [cliente.info() for cliente in clientes]

def get_one_client(id):
    client = Cliente.query.get(id)
    if not client :
        raise CustomerNotFound 
    return client.dicionario()

def create_cliente(data):
    new_client = Cliente(name=data['name'],age=data['age'],telephone=data['telephone'],service=data['service'])
    db.session.add(new_client)
    db.session.commit()
    

def update_client(id,updated):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    client.name = updated['name']
    client.age = updated['age']
    client.telephone = updated['telephone']
    client.service = updated['service']
    db.session.commit()


def delete_client(id):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    db.session.delete(client)
    db.session.commit()

def delete_all_clients():
    clients = Cliente.query.all()
    db.session.delete(clients)
    db.session.commit()