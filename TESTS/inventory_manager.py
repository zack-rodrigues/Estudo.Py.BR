import csv

def cadastrar_item():
    with open('database.csv', 'r') as database:
        lista = csv.DictReader(database)
        ids = [int(linha['id']) for linha in lista]  # Coleta todos os IDs
        new_id = max(ids) + 1 if ids else 1  # Calcula o novo ID e verifica se existem ids na lista, caso não cria o primeiro

    with open('database.csv', 'a') as database:  # Reabre o arquivo em modo de append
        new_item_name = str(input('Qual nome do item que deseja adicionar? '))
        new_price = float(input('Qual o preço? '))
        new_qty = int(input('Qual a quantidade? '))
        database.write(f'{new_id},{new_item_name},{new_price},{new_qty}\n')


def busca_item():
   with open('database.csv','r') as database:
      lista=csv.DictReader(database)
      palavrachave=input('Digite algo para buscar: ').lower()
      for item in lista:
         if palavrachave in item['item_name'].lower():
            print(item)


cadastrar_item()
busca_item()



    

