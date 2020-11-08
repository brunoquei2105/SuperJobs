from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Nome', size=(5, 0)), sg.Input(size=(30, 0), key='nome')],
    [sg.Text('Email', size=(5, 0)), sg.Input(size=(30, 0), key='email')],
    [sg.Text('Data Nascimento', size=(15, 0)), sg.Input(size=(20, 0), key='data_nascimento')],
    [sg.Text('Cpf', size=(5, 0)), sg.Input(size=(30, 0), key='cpf')],
    [sg.Text('Senha', size=(5, 0)), sg.Input(size=(20, 0), key='senha', password_char='*')],
    [[sg.Text('Repita Senha', size=(13, 0)), sg.Input(size=(20, 0), key='repita_senha', password_char='*')]],
    [sg.Checkbox('Salvar Dados')],
    [sg.Button('Cadastrar')]
]
janela = sg.Window('Super Jobs - Cadastro', layout)
while True:
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cadastrar':
        if values['senha'] == values['repita_senha']:
            print('Usuário Cadastrado com Sucesso')
        else:
            print('Senhas Não Confere. Tente Novamente.')
            