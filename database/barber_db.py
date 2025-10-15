from app import db


class Barbeiro(db.Model):
    __tablename__ = 'Barbeiro'

    id = db.Column(db.Integer,primary_key= True,autoincrement=True)
    barbeiro = db.Column(db.String(100),nullable=False)
    idade = db.Column(db.Integer)
    local_de_trabalho = db.Column(db.String(70),nullable=False)
    appointments = db.relationship('Agendamento',back_populates='barber')

    def __init__(self,id,name,age,workplace,appointments):
       self.id = id
       self.barbeiro = name
       self.idade = age
       self.local_de_trabalho = workplace
       self.appointments = appointments

    def dicionario(self):
     return {'id':self.id,'barbeiro':self.barbeiro,'idade':self.idade,'local de trabalho': self.local_de_trabalho,'agendamentos':[agendamento.id for agendamento in self.appointments]}
    
    def informations(self):
     return self.dicionario()

class BarbeiroNaoEncontrado(Exception):
   pass


def get_all_barbers():
     barbers = Barbeiro.query.all()
     return [barber.informations() for barber in barbers]

def get_one_barber(id):
   barber = Barbeiro.query.get(id)
   if not barber:
      raise BarbeiroNaoEncontrado
   return barber.dicionario()

def create_new_barber(data):
   new_barber = Barbeiro(id=data['id'],name=data['barbeiro'],age=data['idade'],workplace=data['local de trabalho'],appointments=data.get('agendamentos',[]))
   db.session.add(new_barber)
   db.session.commit()

def update_barber(id,data):
    barber = Barbeiro.query.get(id)
    if not barber:
       raise BarbeiroNaoEncontrado
    barber.id = data['id']
    barber.name = data['barbeiro']
    barber.age = data['idade']
    barber.workplace = data['local de trabalho']
    barber.agendamentos = data['agendamentos']
    db.session.commit()

def delete_barber(id):
   barber_delete = Barbeiro.query.get(id)
   db.session.delete(barber_delete)
   db.session.commit()

def delete_all_barbers():
   barbers = Barbeiro.query.all()
   db.session.delete(barbers)
   db.session.commit()
