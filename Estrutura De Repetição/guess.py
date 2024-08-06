import random

while True:
 num=random.randint(1, 10)
 print(f'para motivos de teste, a resposta é: {num}')
 chute=int(input('Advinhe o número que estou pensando de 1 a 10: '))
 if chute == num:
    print('Acertou!!!')
    break
 else:
    print('Errou tente novamente...')
