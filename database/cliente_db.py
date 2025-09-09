from app import db
import datetime
from .barber_db import Barbeiro
from werkzeug.security import check_password_hash,generate_password_hash
import hashlib


class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(70),nullable=False)
    age = db.Column(db.Integer)
    telephone = db.Column(db.String(12),nullable=False)
    service = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(128),nullable=False,default="")

   
    def __init__(self,id,name,age,telephone,service,password):
        self.id = id
        self.name = name
        self.age = age
        self.telephone = telephone
        self.service = service
        self.password = password
        

    def dicionario(self):
        return {'id':self.id,'nome':self.name,'idade':self.age,'telefone':self.telephone,'serviço':self.service,'senha':self.password}
    
    def info(self):
        return self.dicionario()
    
class CustomerNotFound(Exception):
    pass

def get_all_clients():
     clientes = Cliente.query.all()
     return [cliente.info() for cliente in clientes]

def get_one_client(id):
    client = Cliente.query.get(id)
    if not client :
        raise CustomerNotFound 
    return client.info()

def create_cliente(data):
    new_client = Cliente(id=data['id'],name=data['nome'],age=data['idade'],telephone=data['telefone'],service=data['serviço'])
    db.session.add(new_client)
    db.session.commit()
    

def update_client(id,updated):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    client.id = updated['id']
    client.name = updated['nome']
    client.age = updated['idade']
    client.telephone = updated['telefone']
    client.service = updated['serviço']
    db.session.commit()


def delete_client(id):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    db.session.delete(client)
    db.session.commit()