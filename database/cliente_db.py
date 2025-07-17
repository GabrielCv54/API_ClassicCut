from app import db
import datetime
from .barber_db import Barbeiro

today = datetime.datetime.now()

class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(70),nullable=False)
    age = db.Column(db.Integer)
    telephone = db.Column(db.String(12),nullable=False)
    service = db.Column(db.String(50),nullable=False)

    barber_id = db.Column(db.Integer,db.ForeignKey('Barbeiro.id'))
    barber = db.relationship('Barbeiro',back_populates='agendamentos')
   
    def __init__(self,id,name,age,telephone,service):
        self.id = id
        self.name = name
        self.age = age
        self.telephone = telephone
        self.service = service

    def dicionario(self):
        return {'id':self.id,'nome':self.name,'idade':self.age,'telefone':self.telephone,'serviço':self.service,'barber_id':self.barber_id}
    
class CustomerNotFound(Exception):
    pass

def get_all_clients():
     clientes = Cliente.query.all()
     return [cliente.dicionario() for cliente in clientes]

def get_one_client(id):
    client = Cliente.query.get(id)
    if not client :
        raise CustomerNotFound
    return client

def create_cliente(data):
    barbeiro_id = data.get('barber_id')
    barbeiro_objeto = Barbeiro.query.get(barbeiro_id)
    if not barbeiro_objeto:
        raise CustomerNotFound
    new_client = Cliente(id=data['id'],name=data['nome'],age=data['idade'],telephone=data['telefone'],service=data['serviço'],barber_id=data['barbeiro_responsável'])
    db.session.add(new_client)
    db.session.commit()
    

def update_client(id,updated):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    updated.id = client['id']
    updated.name = client['nome']
    updated.age = client['idade']
    updated.telephone = client['telefone']
    updated.service = client['serviço']
    db.session.add(updated)
    db.session.commit()


def delete_client(id):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    db.session.delete(client)
    db.session.commit()