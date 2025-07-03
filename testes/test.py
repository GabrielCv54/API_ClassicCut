import pytest
import requests as r

url = 'http://127.0.0.1:5000/barbearia/barbeiros'

@pytest.fixture()
def requisition_api():
      requisition = r.get(url)
      assert (requisition.status_code == 200)

@pytest.fixture()
def id_barbeiro(self):
       barber = {'id':4,'Nome':'Joao','idade':27}
       assert (type(barber['id']) == int)

def test_verifica_se_o_id_e_inteiro(barber):
     for b in barber:
          if type(b['id'] )!= int:
               raise ValueError('O id só pode ser do tipo inteiro!')
          else:
               return {'Tudo certo!!!'}

if  __name__ == '__main__':
   pytest.main()