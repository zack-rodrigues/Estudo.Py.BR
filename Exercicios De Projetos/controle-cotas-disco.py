#controles de cota de disco
import os

def bytes_mb(bytes):
    return bytes/(1024*1024)

arquivo_base= os.path.dirname(__file__)
arquivo_entrada= os.path.join(arquivo_base,'usuarios.txt')
arquivo_saida= os.path.join(arquivo_base, 'relatorio.txt')

usuarios=[]

with open(arquivo_entrada) as arquivo:
    for linha in arquivo:
        nome= linha[:15].strip()
        espaco_bytes=int(linha[15:].strip())
        espaco_mb=bytes_mb(espaco_bytes)
        usuarios.append((nome,espaco_mb))


total_espaco= sum(espaco for _, espaco in usuarios )
media_espaco= total_espaco / len(usuarios) 


relatorio=[]
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
