# 📁 Exercícios com Arquivos

## 1. **Validador de Endereços IP**

Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

### 📅 Arquivo de entrada (`ips.txt`)
```
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
```

### 📄 Arquivo de saída (`relatorio_ips.txt`)
```
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
```

[Código](./validador_ips.py)

---

## 2. **Relatório de Espaço em Disco por Usuário**

A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.

O administrador possui um arquivo com o seguinte conteúdo:

### 📅 Arquivo de entrada (`usuarios.txt`)
```
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
```

O nome do usuário possui exatamente 15 caracteres. A partir deste arquivo, você deve criar um relatório com:

- Espaço utilizado em MB
- Porcentagem do uso
- Espaço total ocupado
- Espaço médio ocupado

### 📄 Arquivo de saída (`relatorio.txt`)
```
ACME Inc.               Uso do espaço em disco pelos usuários
--------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
1    alexandre      434,99 MB            16,85%
2    anderson      1187,99 MB            46,02%
3    antonio        117,73 MB             4,56%
4    carlos          87,03 MB             3,37%
5    cesar            0,94 MB             0,04%
6    rosemary       752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
```

[Código](./relatorio_usuarios.py)

