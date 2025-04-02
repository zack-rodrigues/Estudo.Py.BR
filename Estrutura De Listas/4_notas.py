medias=[]

for aluno_id in range(10):
    print(f'aluno numero {aluno_id+1} !')
    soma=0

    for nota_id in range(4):
        nota=int(input(f"Qual a nota {nota_id+1}: "))
        soma+=nota
    
    media=soma/4
    medias.append(media)

aprovados=sum(1 for media in medias if media >=7)
print(f'numero de aprovados é {aprovados}')