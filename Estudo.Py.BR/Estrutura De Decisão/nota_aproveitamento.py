grade1=float(input('Insert your first grade:'))
grade2=float(input('Insert your second grade:'))

avarange=(grade1+grade2)/2
conceito='nada'
approval='nada'

if avarange > 0.0 and avarange < 4.0:
    conceito='E'
    approval='REPROVADO'

elif avarange > 4.0 and avarange < 6:
     conceito='D'
     approval='REPROVADO'

elif avarange > 6.0 and avarange < 7.5:
     conceito='C'
     approval='APROVADO'

elif avarange > 7.5 and avarange < 9.0:
     conceito='B'
     approval='APROVADO'

elif avarange > 9.0 and avarange <= 10.0:
     conceito='A'
     approval='APROVADO'

print(f'Sua média é de {avarange:.2f}, seu conceito é {conceito}, logo você foi.. {approval}!')   
    
