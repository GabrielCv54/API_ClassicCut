## API-ClassicCut
<img src="/logo/logotipo.jpg" alt="imagem" width="80%" height="60%">

API- ClassicCut💈
Esse projeto é um projeto que estou desenvolvendo uma API que gerencia uma barbearia , que possui três entidades : Barbeiro, Cliente e Agendamentos. Nesse projeto,estão ,os endpoints das três entidades, banco de dados para armazenar as informações e os endpoints que funcionam com  4 métodos HTTP(GET,POST,PUT E DELETE)

## Tecnologia utilizadas
- Python🐍
- Flask
- Docker🐋
- Flask SQLAlchemy
- POSTMAN👩‍🚀

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
Exemplos de retorno
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
.O atributo agendamento na entidade barbeiro, mostra os id's dos agendamentos do qual o barbeiro irá realizar. Lembrando que , o atributo agendamentos não é uma coluna no banco , apenas um objeto que faz o relacionamento entre barbeiros e agendamentos.

### Cliente
```
    {
        "age": 19,
        "id": 150,
        "name": "marcelo",
        "service": "corte de cabelo longo",
        "telephone": "1196958787"
    }
```
. Os clientes também tem seus dados armazenados na API para garantir aos barbeiros a integridade dos clientes que eles irão atender.

### Agendamento
```
    {
        "barbeiro": 1,
        "cliente": 100,
        "dia": "2024-01-17",
        "horário": "17:40:00",
        "id": 1
    }
```
Cada agendamento possui também os id's de barbeiro e cliente que fazem parte , para assim o sistema também fazer o relacionamento entre as tabelas.

## Como mexer no projeto
Enquanto o projeto estiver lá rodando, você pode utilizar ferramentas como Postman ou Insomnia, para ver os métodos HTTP em ação, abaixo explicando como

### GET
![alt text](print_get_barbearia.png)