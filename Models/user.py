from datetime import date
from utils.helper import date_para_str, str_para_date
from passlib.hash import pbkdf2_sha256 as cryp


class User:
    cod = 1001

    def __init__(self, nome: str, sobrenome: str, email: str, data_nasc: str, cpf: str, senha: str):
        self.__cod = User.cod
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__data_nasc = str_para_date(data_nasc)
        self.__cpf = cpf
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.__data_cadastro = date.today()
        User.cod += 1
        print(f'Usuário criado com Sucesso: {self.gera_user}')


    def __str__(self):
        return f'Nome Completo: {self.nome_completo} \nEmail: {self.email} \nData Nascimento: {self.data_nascimento} ' \
               f'\nData de Cadastro: {self.data_cadastro} \nSenha: {self.__senha}'

    @property
    def codigo(self):
        return self.__cod

    @property
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def data_nascimento(self):
        return date_para_str(self.__data_nasc)

    @property
    def data_cadastro(self):
        return date_para_str(self.__data_cadastro)

    @property
    def gera_user(self):
        return self.email.split('@')[0]

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def change_email(self, email):
        self.__email = email
        return email