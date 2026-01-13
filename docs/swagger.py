from flask_restx import Api
from app import api

api_s = Api(app=api,
            version='1.0',
            title='API de Barbearia',
            description='Api responsável por gerenciar Barbeiros,Agendamentos e Clientes',
            mask_swagger=False,
            doc='/docs')