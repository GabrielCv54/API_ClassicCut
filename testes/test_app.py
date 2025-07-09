import pytest 
import requests as r
import datetime

url = 'http://127.0.0.1:5000/barbearia/barbeiros'

#Dicionário de exemplo da barbearia
barbershop= {
    'Barbeiros':[
        {'id':1,'Nome':'Edgar Rodrigues','Idade':datetime.datetime(1985,1,22),'Cortes Marcados':[100,200,300,400,500],'Local de Trabalho':'Their Space'}
        ],
    'Clientes':[
        {'id':100,'Nome':'Lucas Moura','Idade':datetime.datetime(1995,10,20),'CPF':459896614,'Horário_agendamento':'15h30','Dia_agendamento':'Sábado,28 de junho'},
        {'id':200,'Nome':'Kauan De moraes','Idade':datetime.datetime(2000,4,19),'Cortes Marcados':}
        ],
    "Agendamentos":[
        {'id':1,'Dia':'28 de Junho','Cabeleireiro':1,'Cliente':100}
        ]
    }

barbers = barbershop['Barbeiros']
clients = barbershop['Clientes']


def requisition_api():
      requisition = r.get(url)
      assert (requisition.status_code == 200)

def test_id_barbeiro():
       for b in barbers:
            id = b.get('id')
       assert (type(id) == int)

def test_verifica_se_o_nome_string():
        for barber in barbers:
           nome = barber.get('Nome')
           assert type(nome) == str,"O nome do barbeiro está ok"
            
def test_maior_de_idade():
      for barber in barbers:
             age_barber =( datetime.datetime.now() - barber.get('idade'))
             assert isinstance(age_barber,age_barber<=18), 'A idade do barbeiro cadastrado só pode ser maior de 18 anos!'

def test_verifica_se_o_id_do_cliente_existe():
      id_clients = barbers['Cortes Marcados']
      all_clients = clients
      for id_cli in id_clients:
        assert id_cli == 
                
'''age_barber = datetime.datetime.now() - datetime.datetime(2022,10,2)
print(age_barber.days)'''