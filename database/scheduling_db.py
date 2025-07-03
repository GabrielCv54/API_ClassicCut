from app import db

class Agendamento(db.Model):
     __tablename__ = 'Agendamento'

     id = db.Column(db.Integer,primary_key=True)
     day =db.Column(db.Datetime,nullable=False)
     barber = db.Column(db.ForeignKey('Barbeiro.id'))
     client = db.Column(db.ForeignKey('Cliente.id'))