## API-ClassicCut
<img src="/logo/logotipo.jpg" alt="imagem" width="80%" height="60%">

API- ClassicCut💈
Esse projeto é um projeto que estou desenvolvendo uma API que gerencia uma barbearia , que possui três entidades : Barbeiro, Cliente e Agendamentos. Nesse projeto,estão ,os endpoints das três entidades, banco de dados para armazenar as informações e os endpoints que funcionam com  4 métodos HTTP(GET,POST,PUT E DELETE)

## Tecnologia utilizadas
- Python🐍
- Flask
- Docker🐋
- Flask SQLAlchemy
- POSTMAN

### Como baixar
` git clone https://github.com/GabrielCv54/API_ClassicCut.git `

### Venv
Nunca se esquecer de ,quando clonar o projeto em sua máquina, também criar e ativar o ambiente virtual(venv)

` python -m venv nome do ambiente(normalmente venv ) `

## Como funciona
O projeto foi feito na minha intenção de estudar mais sobre a construção de uma API com Flask, e fiz ele justamente  com esse tema de barbearia para explorar também os relacionamentos entre entidades do banco de dados. Para rodar o projeto, primeiro deve se executar o comando `python run.py`

Logo após , será gerado o link `127.0.0.1` , e esse link deve ser colado no navegador e adicionar uma barra com o nome das entidades.
Exemplo: '127.0.0.1/barbearia/barbeiros' | '127.0.0.1/barbearia/clientes' | 

### Barbeiro
Exemplo de retorno 
```
 {
        "agendamentos": [
            1,
            4
        ],
        "barbeiro": "Edgar Rodrigues",
        "id": 1,
        "idade": 36,
        "local de trabalho": "Their Space"
    } 
    ```
.O atributo agendamento na entidade barbeiro, mostra os id's dos agendamentos do qual o barbeiro irá realizar.

### Cliente
. Os clientes também tem seus dados armazenados na API para garantir aos barbeiros a integridade dos clientes que eles irão atender.

### Agendamento
Cada agendamento