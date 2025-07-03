from ..app import db
from sqlalchemy.types import ARRAY

class Barbeiro(db.Model):
    __tablename__ = 'Barbeiro'

    id = db.Column(db.Integer,primary_key= True,autoincrement=True)
    name = db.Column(db.String(70),nullable=True)
    age = db.Column(db.Integer)
    workplace = db.Column(db.String(70),nullable=False)
    appointments = db.Column(db.ForeignKey(ARRAY('Cliente.id')))

    def __init__(self,id,name,age,workplace,appointments):
       self.id = id
       self.name = name
       self.age = age
       self.workplace = workplace
       self.appointments = appointments

    def dicionario(self):
     return {'Id':self.id,'Barbeiro':self.name,'Idade':self.age,'Local de trabalho': self.workplace,'Agendamentos':self.appointments}
    
    def informations(self):
     return self.dicionario()

class BarbeiroNaoEncontrado(Exception):
   pass


def get_all_barbers():
     barbers = Barbeiro.query.all()
     return barbers

def get_one_barber(id):
   barber = Barbeiro.query.get(id)
   if not barber:
         return {'Erro':'Esse barbeiro não está cadastrado,verifique se o id e tente novamente!!'},404
   return barber.dicionario()

def create_new_barber(data):
   new_barber = Barbeiro(id=data['id'],name=data['nome'],age=data['Idade'],workplace=data['Local de Trabalho'],appointments=data['Agendamentos'])
   db.session.add(new_barber)
   db.session.commit()

def update_barber(id,data):
    barber = Barbeiro.query.get(id)
    if not barber :
       raise BarbeiroNaoEncontrado
    data.id = barber['id']
    data.name = barber['nome']
    data.age = barber['idade']
    data.workplace = barber['Local de Trabalho']
    data.appointments = barber['Agendamentos']
    db.session.add(data)
    db.session.commit()

def delete_barber(id):
   barber_delete = Barbeiro.query.get(id)
   if not barber_delete:
      raise BarbeiroNaoEncontrado
   else:
      db.session.delete(barber_delete)
      db.session.commit()


