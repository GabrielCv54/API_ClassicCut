from ..app import db
import datetime

today = datetime.datetime.now()

class Cliente(db.Model):
    __tablename__ = 'Cliente'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(70),nullable=False)
    age = db.Column(db.Integer)
    appointment_time = db.Column(db.Time,nullable=False)
    appointment_day = db.Column(db.String(35),nullable=False)

    barber_id = db.Column(db.Integer,db.ForeignKey('Barbeiro.id'))
    barber = db.relationship('Barbeiro',back_populates='agendamentos')
   
    def __init__(self,id,name,age,appointment_time,appointment_day,barber):
        self.id = id
        self.name = name
        self.age = age
        self.appointment_time = appointment_time
        self.appointment_day = appointment_day
        self.barber = barber

    def dicionario(self):
        return {'id':self.id,'nome':self.name,'idade':self.age,'hora do agendamento':self.appointment_time,'dia do agendamento':self.appointment_day,'barbeiro':self.barber}
    
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
    new_client = Cliente(id=data['id'],name=data['nome'],age=data['idade'],appointment_time=data['hora do agendamento'],appointment_day=data['dia do agendamento'],barber=data['barbeiro'])
    db.session.add(new_client)
    db.session.commit()
    return new_client

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
    return {'Cliente atualizado com sucesso!!'}

def delete_client(id):
    client = Cliente.query.get(id)
    if not client:
        raise CustomerNotFound
    db.session.delete(client)
    db.session.commit()
    return {'Cliente deletado com sucesso!!'}