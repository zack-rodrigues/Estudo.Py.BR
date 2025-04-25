import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd

ARQUIVO = 'database.csv'

def cadastrar_item():
    try:
        df = pd.read_csv(ARQUIVO, dtype={'id': str})
    except FileNotFoundError:
        df = pd.DataFrame(columns=['id', 'item_name', 'price', 'quantity', 'brand'])

    new_id = df['id'].astype(int).max() + 1 if not df.empty else 1
    item_name = simpledialog.askstring("Cadastrar", "Digite o nome do item:")
    price = simpledialog.askfloat("Cadastrar", "Digite o preço:")
    quantity = simpledialog.askinteger("Cadastrar", "Digite a quantidade:")
    brand = simpledialog.askstring("Cadastrar", "Digite a marca do produto:")

    if None in (item_name, price, quantity, brand):
        return

    df = pd.concat([df, pd.DataFrame([{
        'id': new_id,
        'item_name': item_name,
        'price': price,
        'quantity': quantity,
        'brand': brand
    }])], ignore_index=True)

    df.to_csv(ARQUIVO, index=False)
    messagebox.showinfo("Sucesso", f'Item "{item_name}" cadastrado com sucesso!')

def busca_item():
    try:
        df = pd.read_csv(ARQUIVO, dtype={'id': str})
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Arquivo não encontrado.")
        return

    palavra = simpledialog.askstring("Buscar", "Digite o item para buscar:")
    marca = simpledialog.askstring("Buscar", "Digite a marca do produto:")

    if not palavra or not marca:
        return

    filtrado = df[df['item_name'].str.contains(palavra, case=False) & df['brand'].str.contains(marca, case=False)]
    filtrado = filtrado.sort_values(by='price', ascending=False)

    if filtrado.empty:
        messagebox.showinfo("Busca", "Nenhum item encontrado.")
        return

    # Janela com rolagem
    result_window = tk.Toplevel(root)
    result_window.title("Resultados da Busca")
    result_window.geometry("600x400")

    scrollbar = tk.Scrollbar(result_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(result_window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_area.pack(expand=True, fill=tk.BOTH)

    for _, row in filtrado.iterrows():
        texto = (
            f"ID: {row['id']}\n"
            f"Nome: {row['item_name']}\n"
            f"Marca: {row['brand']}\n"
            f"Preço: R${row['price']}\n"
            f"Quantidade: {row['quantity']}\n"
            + "-"*50 + "\n"
        )
        text_area.insert(tk.END, texto)

    scrollbar.config(command=text_area.yview)

def remover_item():
    try:
        df = pd.read_csv(ARQUIVO, dtype={'id': str})
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Arquivo não encontrado.")
        return

    id_remove = simpledialog.askstring("Remover", "Digite o ID do item a remover:")
    if not id_remove:
        return

    df_novo = df[df['id'] != id_remove]
    df_novo.to_csv(ARQUIVO, index=False)

    messagebox.showinfo("Remover", f'Item com ID {id_remove} removido (se existia).')

def editar_item():
    try:
        df = pd.read_csv(ARQUIVO, dtype={'id': str})
    except FileNotFoundError:
        messagebox.showwarning("Erro", "Arquivo não encontrado.")
        return

    id_editar = simpledialog.askstring("Editar", "Digite o ID do item a editar:")
    if not id_editar:
        return

    if id_editar not in df['id'].values:
        messagebox.showerror("Erro", "ID não encontrado.")
        return

    item = df[df['id'] == id_editar].iloc[0]
    nome = simpledialog.askstring("Editar", f'Nome atual: {item["item_name"]}\nNovo nome:')
    preco = simpledialog.askstring("Editar", f'Preço atual: {item["price"]}\nNovo preço:')
    qtd = simpledialog.askstring("Editar", f'Quantidade atual: {item["quantity"]}\nNova quantidade:')
    marca = simpledialog.askstring("Editar", f'Marca atual: {item["brand"]}\nNova marca:')

    if nome: item['item_name'] = nome
    if preco: item['price'] = float(preco)
    if qtd: item['quantity'] = int(qtd)
    if marca: item['brand'] = marca

    df.loc[df['id'] == id_editar] = item
    df.to_csv(ARQUIVO, index=False)

    messagebox.showinfo("Editar", f"Item com ID {id_editar} atualizado com sucesso.")

# UI principal
root = tk.Tk()
root.title("Gerenciador de Itens")
root.geometry("320x350")

tk.Label(root, text="Menu de Operações", font=("Helvetica", 14, "bold")).pack(pady=10)

tk.Button(root, text="1. Buscar item", width=30, command=busca_item).pack(pady=5)
tk.Button(root, text="2. Cadastrar item", width=30, command=cadastrar_item).pack(pady=5)
tk.Button(root, text="3. Editar item", width=30, command=editar_item).pack(pady=5)
tk.Button(root, text="4. Remover item", width=30, command=remover_item).pack(pady=5)
tk.Button(root, text="5. Sair", width=30, command=root.quit, fg="red").pack(pady=20)

root.mainloop()
