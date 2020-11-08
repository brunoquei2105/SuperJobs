from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

def login():
    layout = [
            [sg.Text('Usuário', size=(5, 0)), sg.Input(size=(30, 0), key='usuario')],
            [sg.Text('Senha', size=(5, 0)), sg.Input(size=(30, 0), key='senha', password_char='*')],
            [sg.Checkbox('Salvar Dados')],
            [sg.Button('Entrar')]
                ]
#criando a janela
    janela = sg.Window('Super Jobs- Login', layout)
    while True:
        event, values = janela.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Entrar':
            if values['usuario'] == 'Bruno' and values['senha'] == '123456':
                print('Bem-Vindo ao Super Jobs!')
            else:
                print('Usuário ou Senha Inválida.')


login()
