import os

# Mapeamento dos nomes de arquivos antigos para novos nomes
file_mapping = {
    "circle measures.py": "area_circulo.py",
    "avarange grade.py": "media_notas.py",
    "celcius to fh.py": "celsius_para_fahrenheit.py",
    "dobro.py": "calculando_numeros.py",
    "double square area.py": "dobro_area_quadrado.py",
    "fh to celsius.py": "fahrenheit_para_celsius.py",
    "folha de pagamento.py": "folha_pagamento.py",
    "hello.py": "alo_mundo.py",
    "m to cm.py": "metros_para_centimetros.py",
    "num input.py": "numero_informado.py",
    "pescador e multa.py": "pescador_multa.py",
    "peso ideal.py": "peso_ideal.py",
    "peso idela h ou m.py": "peso_ideal_h_m.py",
    "sum test.py": "soma_numeros.py",
    "tinta m2.py": "loja_tintas.py",
    "tintas seletivas.py": "loja_tintas_avancado.py",
    "velocidade internet.py": "velocidade_download.py",
    "worked hours calculator.py": "calculadora_horas_trabalhadas.py"
}

# Renomeia os arquivos
for old_name, new_name in file_mapping.items():
    try:
        os.rename(old_name, new_name)
        print(f"Renomeado {old_name} para {new_name}")
    except FileNotFoundError:
        print(f"Arquivo {old_name} não encontrado.")
    except Exception as e:
        print(f"Erro ao renomear {old_name}: {e}")
