from app import db

class Agendamento(db.Model):
     __tablename__ = 'Agendamento'

     id = db.Column(db.Integer,primary_key=True)
     day = db.Column(db.Datetime,nullable=False)
     hour = db.Column(db.Time,nullable=False)
     barber = db.Column(db.ForeignKey('Barbeiro.id'))
     client = db.Column(db.ForeignKey('Cliente.id'))

     def __init__(self,id,day,hour,barber,client):
          self.id = id
          self.day = day
          self.hour = hour
          self.barber = barber
          self.client = client
          

     def dici(self):
          return {'id':self.id,'dia':self.day,'horário':self.hour,'barbeiro':self.barber,'cliente':self.client}
  
     def info(self):
          return self.dici()
     
class SchedulingNotFound(Exception):
     pass

def get_all_schedulings():
     scheduling = Agendamento.query.all()
     return [sch.info() for sch in scheduling]

def get_one_scheduling(id):
     scheduling = Agendamento.query.get(id)
     if not scheduling:
          raise SchedulingNotFound
     return scheduling.info()

def create_new_scheduling(data):
     new = Agendamento(id=data['id'],day=data['dia'],hour=data['hora'],barber=data['barbeiro'],client=data['cliente'])
     db.session.add(new)
     db.session.commit()

def update_scheduling(id,data):
     scheduling = Agendamento.query.get(id)
     if not scheduling:
          raise SchedulingNotFound
     scheduling.id = data['id']
     scheduling.day = data['dia']
     scheduling.hour = data['hora']
     scheduling.barber = data['barbeiro']
     scheduling.client = data['cliente']
     db.session.commit()

def delete_scheduling(id):
     deleted = Agendamento.query.get(id)
     if not deleted:
          raise SchedulingNotFound
     db.session.delete(id)
     db.session.commit()