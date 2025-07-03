import unittest
import requests as r
from ..app import api

route = 'http://127.0.0.1:5000/barbearia/barbeiros'

class TesteApi(unittest.TestCase):
    def test_se_api_funciona(self):
      requisition = r.get(route)
      self.assertEqual()