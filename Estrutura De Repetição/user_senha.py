while True:
   
    user=str(input('Qual nome de usuário você deseja ?\n'))
    senha=input('Qual senha vai cadastrar para seu user ?\n')

    if senha == user:
        print()
        print('A senha deve ser diferente do usuário..\n')
    else:
        print('Cadastro Concluído')
        break