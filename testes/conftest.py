import pytest
import requests as r
from test_app import barbers,clients,url


@pytest.fixture()
def requisition_api():
      requisition = r.get(url)
      assert (requisition.status_code == 200)

@pytest.fixture()
def test_id_barbeiro():
       for b in barbers:
            id = b.get('id')
       assert (type(id) == int)

@pytest.fixture()
def test_verifica_se_o_nome_string():
        for barber in barbers:
           nome = barber.get('Nome')
        if type(nome)!= str:
           raise ValueError('O id só pode ser do tipo inteiro!')
        else:
            return {'Sucesso':'Tudo certo, barbeiro com nome ok!!!'}
