import pytest
import requests as r
from test_app import barbershop,clients,url_barber


@pytest.fixture()
def requisition_api():
      requisition = r.get(url_barber)
      return requisition.status_code

@pytest.fixture()
def test_id_barbeiro(id):
       for b in barbershop['Barbeiros']:
           if  b.get('id') == id:
            return (b)

@pytest.fixture()
def test_verifica_se_o_nome_string():
        for barber in barbershop['Barbeiros']:
           nome = barber.get('Nome')
           return {'Mensagem':f'Nome do seu barbeiro: {nome}'}
