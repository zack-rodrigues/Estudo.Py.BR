senha=None
username=None
while senha==username:

    username=input('Defina um nome de usuario:')
    senha=input('Defina uma senha:')

    if senha!=username:
        print(f'User: {username} e senha: {senha} , cadastrados com sucesso')
        break
    else:
        print('A senha deve ser diferente do nome de Usuario',username)
