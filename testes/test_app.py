import pytest 
import requests as r

url_barber = 'http://127.0.0.1:5000/barbearia/barbeiros'


#Dicionário de exemplo da barbearia
barbershop = {
    'Barbeiros':[
        {"barbeiro":"Edgar Rodrigues","idade":36,"agendamentos":[1],"local de trabalho":"Their Space"},
         {"id":2,"barbeiro":"Roman rodriguez","idade":32,"agendamentos":[2],"local de trabalho":"El muchacho"}
        ],
    'Clientes':[
        {"name":"Lucas Moura","age":29,"telephone":"1194699999","service":""},
        {'id':200,'nome':'Kauan De moraes','idade':36,'telefone':'11965489996','serviço':'corte e barba'},
        {'id':300,'nome':'Elias de nobrega','idade':23,'telefone':'8589644322','serviço':'Corte longo'}
        ],
    "Agendamentos":[
        {"id":1,"dia":"2025-06-28","horário":"17:40:00","barbeiro":1,"cliente":1},
        {'id':2,'dia':'2025-07-25','horário':'9:00:00','barbeiro':2,"cliente":200},
         {'id':3,'dia':'2025-10-08','horário':'09:00:00','barbeiro':2,"cliente":200}
        ]
    }

barbers = barbershop['Barbeiros']
clients = barbershop['Clientes']
appointments = barbershop['Agendamentos']

def requisition_api():
      requisition = r.get(url_barber)
      assert (requisition.status_code == 200)

def test_id_barbeiro(barber,id):
       for b in barbers:
            id = b.get('id')
       assert (barber == int)

def test_verifica_se_o_nome_string():
        for barber in barbers:
           nome = barber.get('Nome')
           assert type(nome) != str,"O nome do barbeiro está errado, deve ser uma string"
            
def test_maior_de_idade():
      for barber in barbers:
             age_barber = barber['idade']
             assert isinstance(age_barber<=18), 'A idade do barbeiro cadastrado só pode ser maior de 18 anos!'

def test_verifica_se_o_id_do_cliente_existe(id):
      id_clients = barbers['Cortes Marcados']
      for id in id_clients:
         assert (id in id_clients) ,'Esse cliente não está cadastro ou não existe'

def test_se_idade_maior_que_150():
     for cli in clients:
      assert cli.get('Idade') > 150, 'Esse cliente não existe, pois essa é uma idade muito avançada'
         

def test_agendamento_existe():
    schedu_in_barber = barbers['Barbeiro']
    schedu_id = appointments['id']
    for barber in barbers:
        dici = dict()
        dici['barbeiro'] = schedu_id
        assert barber.get('id') not in '' ,'Agendamento não feito' 

def test_client_hour():
     for sch in barbershop['Agendamentos']:
      assert sch.get('horário') > '23:59:59' , "esse horário não é valido, pois está acima das 24 horas diárias"
           
