# 📁 Exercícios com Projetos

### 1. Controle de cotas de disco ([código](./controle-cotas-disco.py))

A **ACME Inc.**, uma organização com mais de 1500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado.

Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado `usuarios.txt`:

```
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
```

Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado `relatório.txt`, no seguinte formato:

```
ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB            16,85%
2    anderson       1187,99 MB            46,02%
3    antonio         117,73 MB             4,56%
4    carlos           87,03 MB             3,37%
5    cesar             0,94 MB             0,04%
6    rosemary        752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
```

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes, deverá ser feita através de uma **função separada**, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma **função separada**.

**Recursos adicionais (opcional):**
- Ordenar os usuários pelo percentual de espaço ocupado;
- Mostrar apenas os *n* primeiros em uso, definido pelo usuário;
- Gerar a saída numa página **HTML**;
- Criar o programa que **lê as pastas e gera o arquivo inicial**.

---

### 2. Analisador de logs do Apache ([código](./analisador-logs-apache.py))

Desenvolva um analisador de log do Apache que mostre quais as **strings de pesquisa do Google** que mais levam internautas para o site da sua organização.

---

### 3. Analisador de logs do Squid: sites bloqueados ([código](./analisador-logs-squid.py))

Desenvolva um analisador de log do Squid que mostre **quais os sites mais bloqueados** em uma organização.

