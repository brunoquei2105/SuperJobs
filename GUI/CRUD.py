import mysql.connector
from datetime import date
from passlib.hash import pbkdf2_sha256 as cryp




connection = mysql.connector.connect(host='localhost', user='root', password='21050630', database='SuperJobs', charset='utf8')
print('Conexão feita com Sucesso.')
cursor = connection.cursor(dictionary=True)

'''Teste'''
#cursor.execute(f'INSERT INTO User (nome, sobrenome, email, data_nasc, cpf, senha) '
               #f'VALUES ("jose", "joffre", "jj@gmail.com", "1991/03/24", "55599977700", "12345")')
#connection.commit()

resposta = ''
while resposta != 'sair':
    print('***Bem Vindo ao Super Jobs***')
    nome = str(input('Digite o Nome:'))
    sobrenome = str(input('Digite o Sobrenome:'))
    email = str(input('Email: '))
    data_nasc = str(input('Data de nascimento [AAAA/MM/DD]: '))
    cpf = str(input('Digite o Cpf: '))
    senha = str(input('Digite a Senha: '))
    senha_encriptada = cryp.__hash__(senha, rounds=200000, salt_size=16)
    cursor.execute(f'INSERT INTO User (nome, sobrenome, email, data_nasc, cpf, senha) VALUES ("{nome}", "{sobrenome}", "{email}",'
                   f' "{data_nasc}", "{cpf}", "{senha_encriptada}")')
    connection.commit()
    resposta = input('Digite sair para terminar.')

current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')

# COMANDO DE SELEÇÃO
sql_select = 'SELECT * FROM User;'
cursor.execute(sql_select)
for values in cursor:
    print(values)


cursor.close()
connection.commit()
connection.close()