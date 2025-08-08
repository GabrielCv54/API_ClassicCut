import pytest 
import requests as r
import datetime

url = 'http://127.0.0.1:5000/barbearia/barbeiros'

today = datetime.date.today()
#Dicionário de exemplo da barbearia
barbershop= {
    'Barbeiros':[
        {"id":1,"barbeiro":"Edgar Rodrigues","idade":36,"agendamentos":[],"local de trabalho":"Their Space"}
        ],
    'Clientes':[
        {"id":100,"nome":"Lucas Moura","idade":29,"telefone":"1194699999","serviço":""},
        {'id':200,'Nome':'Kauan De moraes','Idade':36,'CPF':57812484041,'Horário_Agendamento':datetime.time(10,0).isoformat(),'Dia_agendamento':'Sexta,27 de junho'}
        ],
    "Agendamentos":[
        {"id":1,"dia":"28 de Junho","horário":"17h40","barbeiro":1,"cliente":100},
        {'id':2,'dia':'27 de Junho','horário':'9h','barbeiro':2,"cliente":200}
        ]
    }

barbers = barbershop['Barbeiros']
clients = barbershop['Clientes']
appointments = barbershop['Agendamentos']

def requisition_api():
      requisition = r.get(url)
      assert (requisition.status_code == 200)

def test_id_barbeiro():
       for b in barbers:
            id = b.get('id')
       assert (type(id) == int), 'id adicionado corretamente!!'

def test_verifica_se_o_nome_string():
        for barber in barbers:
           nome = barber.get('Nome')
           assert type(nome) == str,"O nome do barbeiro está ok"
            
def test_maior_de_idade():
      for barber in barbers:
             age_barber = barber['Idade']
             assert isinstance(age_barber<=18), 'A idade do barbeiro cadastrado só pode ser maior de 18 anos!'

def test_verifica_se_o_id_do_cliente_existe(id):
      id_clients = barbers['Cortes Marcados']
      for id in id_clients:
         assert (id in id_clients) ,'Esse cliente não está cadastro ou não existe'

def test_se_idade_maior_que_150():
     for cli in clients:
      assert cli.get('Idade') > 150, 'Esse cliente não existe, pois essa é uma idade muito avançada'
     

def test_verificar_se_o_cpf_e_valido():
    pass      

def test_agendamento_existe():
     pass
'''age_barber = datetime.datetime.now() - datetime.datetime(2022,10,2)
print(age_barber.days)'''

'''for cli in clients:
      print(cli)'''
