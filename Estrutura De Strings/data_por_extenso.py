meses={ 
'1':'janeiro',
'2':'fevereiro',
'3':'março',
'4':'abril',
'5':'maio',
'6':'junho',
'7':'julho',
'8':'agosto',
'9':'setembro',
'10':'outubro',
'11':'novembro',
'12':'dezembro'
}

data=input('Digite sua data de nascimento dd/mm/aaaa : ')

dia, mes, ano=data.split('/')

print(f'Você nasceu em {dia} de {meses[mes]} de {ano}.')