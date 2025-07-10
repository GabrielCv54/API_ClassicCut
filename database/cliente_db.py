from ..app import db
import datetime

today = datetime.datetime.now()

class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(70),nullable=False)
    age = db.Column(db.Integer)
    appointment_time = db.Column(db.DateTime,nullable=False)
    appointment_day = db.Column(db.String(35),nullable=False)

    def __init__(self,id,name,age,appointment_time,appointment_day):
        self.id = id
        self.name = name
        self.age = age
        self.appointment_time = appointment_time
        self.appointment_day = appointment_day

    def dicionario(self):
        return {'id':self.id,'Nome':self.name,'Idade':self.age,'Horário de Agendamento':self.appointment_time,'Dia do agendamento':self.appointment_day}
    
class CustomerNotFound(Exception):
    pass

def get_all_clients():
    clientes = Cliente.query.all()
    return clientes

def get_one_client(id):
    client = Cliente.query.get(id)
    if not client :
        raise CustomerNotFound
    return client

def create_cliente(data):
    new_client = Cliente(id=data['id'],name=data['nome'],age=data['idade'],appointment_time=data['Horário de Agendamento'],appointment_day=data['Dia do agendamento'])
    db.session.add(new_client)
    db.session.commit()

def update_client(id,updated):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    updated.id = client['id']
    updated.name = client['name']
    updated.age = client['idade']
    updated.appointment_time = client['Horário de Agendamento']
    updated.appointment_day = client['Dia do agendamento']
    db.session.add(updated)
    db.session.commit()

def delete_client(id):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    db.session.delete(client)
    db.session.commit()