import mysql.connector
from datetime import date
from passlib.hash import pbkdf2_sha256 as cryp
import pandas as pd

connection = mysql.connector.connect(host='localhost', user='root', password='21050630', database='SuperJobs', charset='utf8')
print('Conexão feita com Sucesso.')
cursor = connection.cursor(dictionary=True)

def usuario_superjobs(email):
    user = email.split('@')[0]
    print(f'Usuário criando com suesso: {user}')

# Inserindo dados na Tabela User do BD SuperJobs
resposta = ''

while resposta != 'sair':
    print('***Bem Vindo ao Super Jobs***')
    nome = str(input('Digite o Nome:'))
    sobrenome = str(input('Digite o Sobrenome:'))
    email = str(input('Email: '))
    data_nasc = str(input('Data de nascimento [AAAA/MM/DD]: '))
    cpf = str(input('Digite o Cpf: '))
    senha = str(input('Digite a Senha: '))
    senha_encriptada = cryp.hash(senha, rounds=200000, salt_size=16)

    cursor.execute(f'INSERT INTO User (nome, sobrenome, email, data_nasc, cpf, senha, usuario_name) VALUES ("{nome}", "{sobrenome}", '
                   f'"{email}","{data_nasc}", "{cpf}", "{senha_encriptada}","{usuario_superjobs(email)}")')
    connection.commit()
    resposta = input('Digite sair para terminar.')

current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')
print(current_date)

# COMANDO DE SELEÇÃO
select = input('Você deseja visualizar a Tabela User?')
if select == 'Sim' or select == 'sim':
    sql_select = 'SELECT * FROM User;'
    cursor.execute(sql_select)
    data_frame = pd.DataFrame(cursor)
    print(data_frame.head())
else:
    print('Até Logo.')



# UPDATE
update = input('Deseja atualizar o dado de alguma coluna da Tabela User: ')
if update == 'Sim' or update == 'sim':
    columns = ['nome', 'sobrenome', 'email', 'dat_nasc', 'cpf', 'senha', 'usuario_name']
    for column in columns:
        print(column)
    coluna = str(input('Qual das coluna deseja alterar: '))
    valor = str(input('Digite a alteração que deseja fazer nesta coluna: '))
    sql_update = f'UPDATE USER set {coluna} = {valor}'
    cursor.execute(sql_update)
else:
    print('Até Logo.')


# Fecha o curso, atualiza o BD e fecha a conexão
cursor.close()
connection.commit()
connection.close()
