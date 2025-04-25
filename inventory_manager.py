import csv

def cadastrar_item():
    with open('database.csv', 'r') as database:
        lista = csv.DictReader(database)
        ids = [int(linha['id']) for linha in lista]  # puxa todos id
        new_id = max(ids) + 1 if ids else 1  # Calcula o novo ID e verifica se existem ids na lista, caso não cria o primeiro

    with open('database.csv', 'a') as database:  #tem que abrir como append pra dar certo
        new_item_name = str(input('Digite o nome do item que deseja adicionar: '))
        new_price = float(input('Digite o preço: '))
        new_qty = int(input('Digite a quantidade: '))
        new_brand= str(input('Digite a marca do produto: '))
        database.write(f'{new_id},{new_item_name},{new_price},{new_qty},{new_brand}\n')


def busca_item():
    with open('database.csv','r') as database:
      
      lista=csv.DictReader(database)
      palavrachave=input('Digite o item para buscar: ').lower()
      marca=input('Digite a marca do produto: ').lower()
     
      resultados = []                #essa parte, gera uma lista de resultados apartir desses filros. ordenados por preço.)
      for item in lista:
        if palavrachave in item['item_name'].lower() and marca in item['brand'].lower():
           resultados.append(item)
      
      resultados_sorted=sorted(resultados, key=lambda x:float(x['price']),reverse=True)
      for item in resultados_sorted:
         print(item)


             



busca_item()


    

