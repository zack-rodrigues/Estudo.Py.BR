# Lista de Exercícios de Strings em Python

Aqui estão os exercícios para praticar manipulação de strings em Python. Clique nos links para acessar os códigos correspondentes.

## Exercícios

1. **Tamanho de Strings**

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e se são iguais ou diferentes no conteúdo.

Exemplo:
```
String 1: Brasil Hexa 2006  
String 2: Brasil! Hexa 2006!  
Tamanho de "Brasil Hexa 2006": 16 caracteres  
Tamanho de "Brasil! Hexa 2006!": 18 caracteres  
As duas strings são de tamanhos diferentes.  
As duas strings possuem conteúdo diferente.
```

[Código](./tamanho_strings.py)

2. **Nome ao Contrário em Maiúsculas**

Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.

[Código](./nome_ao_contrario.py)

3. **Nome na Vertical**

Faça um programa que solicite o nome do usuário e imprima-o na vertical.

Exemplo:
```
F  
U  
L  
A  
N  
O
```

[Código](./nome_vertical.py)

4. **Nome na Vertical em Escada**

Modifique o programa anterior de forma a mostrar o nome em formato de escada.

Exemplo:
```
F  
FU  
FUL  
FULA  
FULAN  
FULANO
```

[Código](./nome_escada.py)

5. **Nome na Vertical em Escada Invertida**

Altere o programa anterior de modo que a escada seja invertida.

Exemplo:
```
FULANO  
FULAN  
FULA  
FUL  
FU  
F
```

[Código](./nome_escada_invertida.py)

6. **Data por Extenso**

Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Exemplo:
```
Data de Nascimento: 29/10/1973  
Você nasceu em 29 de Outubro de 1973.
```

[Código](./data_por_extenso.py)

7. **Conta Espaços e Vogais**

Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

- Quantos espaços em branco existem na frase.  
- Quantas vezes aparecem as vogais a, e, i, o, u.

[Código](./conta_espacos_vogais.py)

8. **Palíndromo**

Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa. Em textos mais complexos os espaços e pontuação são ignorados.

Exemplo:
```
SUBI NO ONIBUS
```

Faça um programa que leia uma sequência de caracteres, mostre-a e diga se é um palíndromo ou não.

[Código](./palindromo.py)

9. **Verificação de CPF**

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

[Código](./verifica_cpf.py)

10. **Número por Extenso**

Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

[Código](./numero_por_extenso.py)

11. **Jogo da Forca**

Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Exemplo:
```
Digite uma letra: A  
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O  
A palavra é: _ _ _ _ O

Digite uma letra: E  
A palavra é: _ E _ _ O

Digite uma letra: S  
-> Você errou pela 2ª vez. Tente de novo!
```

[Código](./jogo_forca.py)

12. **Valida e Corrige Número de Telefone**

Faça um programa que leia um número de telefone e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Exemplo:
```
Telefone: 461-0133  
Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.  
Telefone corrigido sem formatação: 34610133  
Telefone corrigido com formatação: 3461-0133
```

[Código](./corrige_telefone.py)

13. **Jogo da Palavra Embaralhada**

Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final, a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

[Código](./jogo_palavra_embaralhada.py)

14. **Leet Speak Generator**

Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça um texto e transforme-o para a grafia leet speak.

[Código](./leet_speak.py)
