import pandas as pd

def cadastrar_item():

    df = pd.read_csv('database.csv', dtype={'id': str})
    new_id = df['id'].astype(int).max() + 1 if not df.empty else 1
    new_item_name = input('Digite o nome do item que deseja adicionar: ')
    new_price = float(input('Digite o preço: '))
    new_qty = int(input('Digite a quantidade: '))
    new_brand = input('Digite a marca do produto: ')

    df = pd.concat([df, pd.DataFrame([{'id': new_id, 'item_name': new_item_name, 'price': new_price, 'quantity': new_qty, 'brand': new_brand}])], ignore_index=True)
    df.to_csv('database.csv', index=False)
    print(f'Item {new_item_name} cadastrado com sucesso!')



def busca_item():
   
    df = pd.read_csv('database.csv', dtype={'id': str})
    palavrachave = input('Digite o item para buscar: ').lower()
    marca = input('Digite a marca do produto: ').lower()
    df_filtrado = df[df['item_name'].str.contains(palavrachave, case=False) & df['brand'].str.contains(marca, case=False)]
    df_filtrado_sorted = df_filtrado.sort_values(by='price', ascending=False)

    for _, item in df_filtrado_sorted.iterrows():
        print(item.to_dict())


def remover_item():

    id_remove = input('Digite o ID que deseja remover: ')
    df = pd.read_csv('database.csv', dtype={'id': str})
    df_filtrado = df[df['id'] != id_remove]
    df_filtrado.to_csv('database.csv', index=False)

    print(f'Item com ID {id_remove} removido com sucesso (se existia).')



def editar_item():
    df = pd.read_csv('database.csv', dtype={'id': str})
    id_editar = input('Digite o ID do item que deseja editar: ')
    item = df[df['id'] == id_editar].iloc[0]

    print(f"Item encontrado: {item['item_name']} - {item['brand']} - {item['price']}")

    new_item_name = input(f'Digite o novo nome do item (ou pressione Enter para manter "{item["item_name"]}"): ')
    new_price = input(f'Digite o novo preço (ou pressione Enter para manter {item["price"]}): ')
    new_qty = input(f'Digite a nova quantidade (ou pressione Enter para manter {item["quantity"]}): ')
    new_brand = input(f'Digite a nova marca (ou pressione Enter para manter "{item["brand"]}"): ')

    if new_item_name: item['item_name'] = new_item_name
    if new_price: item['price'] = float(new_price)
    if new_qty: item['quantity'] = int(new_qty)
    if new_brand: item['brand'] = new_brand

    df.loc[df['id'] == id_editar] = item

    df.to_csv('database.csv', index=False)
    print(f'Item com ID {id_editar} atualizado com sucesso!')


def menu():
    while True:
        print('\nMENU DE OPERAÇÕES')
        print('1. Buscar item')
        print('2. Cadastrar item')
        print('3. Editar item')
        print('4. Remover item')
        print('5. Sair')

        option_selected = input('Selecione uma opção: ')
        
        if option_selected == '1':
            busca_item()
        elif option_selected == '2':
            cadastrar_item()
        elif option_selected == '3':
            editar_item()
        elif option_selected == '4':
            remover_item()
        elif option_selected == '5':
            print('Encerrando o programa. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()
