from models.user import User


class Count():
    codigo = 101

    def __init__(self, user: User):
        self.__cod = Count.codigo
        self.__user = user
        Count.codigo += 1

    def __str__(self):
        return f'Código Conta: {self.__cod}\n Usuário: {User.gera_user} \nSenha: {User.senha}'