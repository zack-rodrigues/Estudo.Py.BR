import re
import os

caminho_arquivo_entrada = os.path.join(os.path.dirname(__file__), 'ips.txt')
caminho_arquivo_saida = os.path.join(os.path.dirname(__file__), 'relatorio_ips1.txt')

def validar_ip(ip):
    padrao = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(padrao, ip):
        return False
    partes = ip.split('.')
    return all(0 <= int(parte) <= 255 for parte in partes)

ips_validos = []
ips_invalidos = []

# Lê o arquivo de entrada
with open(caminho_arquivo_entrada, 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open(caminho_arquivo_saida, 'w') as saida:
    saida.write('[Endereços válidos:]\n')
    for ip in ips_validos:
        saida.write(f'{ip}\n')

    saida.write('\n[Endereços inválidos:]\n')
    for ip in ips_invalidos:
        saida.write(f'{ip}\n')

#ou

import re
import os

base_dir = os.path.dirname(__file__)
path_in = os.path.join(base_dir, 'ips.txt')
path_out = os.path.join(base_dir, 'relatorio_ips2.txt')

def ip_valido(ip):
    if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False

with open(path_in) as f:
    ips = [linha.strip() for linha in f]

validos = [ip for ip in ips if ip_valido(ip)]
invalidos = [ip for ip in ips if not ip_valido(ip)]

with open(path_out, 'w') as f:
    f.write('[Endereços válidos:]\n' + '\n'.join(validos) +
            '\n\n[Endereços inválidos:]\n' + '\n'.join(invalidos))


#pingando ao invez de validar

import os
import platform

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = f"ping {param} 1 {ip}"
    return os.system(comando) == 0

base_dir = os.path.dirname(__file__)
path_in = os.path.join(base_dir, 'ips.txt')
path_out = os.path.join(base_dir, 'relatorio_ips_ping.txt')

with open(path_in) as f:
    ips = [linha.strip() for linha in f if linha.strip()]

validos = [ip for ip in ips if ping(ip)]
invalidos = [ip for ip in ips if ip not in validos]

with open(path_out, 'w') as f:
    f.write('[Endereços válidos:]\n' + '\n'.join(validos) +
            '\n\n[Endereços inválidos:]\n' + '\n'.join(invalidos))
