import os

def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

base_dir = os.path.dirname(__file__)
arquivo_entrada = os.path.join(base_dir, 'usuarios.txt')
arquivo_saida = os.path.join(base_dir, 'relatorio_users.txt')

usuarios = []

with open(arquivo_entrada) as f:
    for linha in f:
        nome = linha[:15].strip()
        espaco_bytes = int(linha[15:].strip())
        espaco_mb = bytes_para_mb(espaco_bytes)
        usuarios.append((nome, espaco_mb))

total_espaco = sum(espaco for _, espaco in usuarios)
media_espaco = total_espaco / len(usuarios)

relatorio = []
relatorio.append("ACME Inc.               Uso do espaço em disco pelos usuários")
relatorio.append("--------------------------------------------------------------")
relatorio.append("Nr.  Usuário        Espaço utilizado     % do uso")

for i, (nome, espaco) in enumerate(usuarios, 1):
    percentual = (espaco / total_espaco) * 100
    relatorio.append(f"{i:<4} {nome:<15} {espaco:>10.2f} MB {percentual:>14.2f}%")

relatorio.append(f"\nEspaço total ocupado: {total_espaco:.2f} MB")
relatorio.append(f"Espaço médio ocupado: {media_espaco:.2f} MB")

with open(arquivo_saida, 'w') as f:
    f.write('\n'.join(relatorio))


#sem função

import os

base_dir = os.path.dirname(__file__)
arquivo_entrada = os.path.join(base_dir, 'usuarios.txt')
arquivo_saida = os.path.join(base_dir, 'relatorio_users2.txt')

usuarios = []

# Lê os dados do arquivo
with open(arquivo_entrada) as f:
    for linha in f:
        nome = linha[:15].strip()
        espaco_bytes = int(linha[15:].strip())
        espaco_mb = espaco_bytes / (1024 * 1024)
        usuarios.append((nome, espaco_mb))

total_espaco = 0
for _, espaco in usuarios:
    total_espaco += espaco

media_espaco = total_espaco / len(usuarios)

# Monta o relatório
relatorio = []
relatorio.append("ACME Inc.               Uso do espaço em disco pelos usuários")
relatorio.append("--------------------------------------------------------------")
relatorio.append("Nr.  Usuário        Espaço utilizado     % do uso")

i = 1
for nome, espaco in usuarios:
    percentual = (espaco / total_espaco) * 100
    relatorio.append(f"{i:<4} {nome:<15} {espaco:>10.2f} MB {percentual:>14.2f}%")
    i += 1

relatorio.append(f"\nEspaço total ocupado: {total_espaco:.2f} MB")
relatorio.append(f"Espaço médio ocupado: {media_espaco:.2f} MB")

# Escreve o arquivo de saída
with open(arquivo_saida, 'w') as f:
    f.write('\n'.join(relatorio))
