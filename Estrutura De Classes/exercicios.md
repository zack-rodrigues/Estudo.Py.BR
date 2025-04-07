# 📁 Exercícios com Classes em Python

## 1. **Classe Bola**

Crie uma classe que modele uma bola:
- **Atributos**: Cor, circunferência, material
- **Métodos**: `trocaCor`, `mostraCor`

[Código](./classe_bola.py)



## 2. **Classe Quadrado**

Crie uma classe que modele um quadrado:
- **Atributo**: Tamanho do lado
- **Métodos**: `mudarLado`, `retornarLado`, `calcularArea`

[Código](./classe_quadrado.py)



## 3. **Classe Retângulo**

Crie uma classe que modele um retângulo:
- **Atributos**: ladoA, ladoB
- **Métodos**: `mudarLados`, `retornarLados`, `calcularArea`, `calcularPerimetro`
- **Extra**: Calcular quantidade de pisos e rodapés para medidas fornecidas pelo usuário.

[Código](./classe_retangulo.py)



## 4. **Classe Pessoa**

Crie uma classe que modele uma pessoa:
- **Atributos**: nome, idade, peso, altura
- **Métodos**: `envelhecer`, `engordar`, `emagrecer`, `crescer`

[Código](./classe_pessoa.py)



## 5. **Classe Conta Corrente**

Crie uma classe para implementar uma conta corrente:
- **Atributos**: número da conta, nome do correntista, saldo (default = 0)
- **Métodos**: `alterarNome`, `depositar`, `sacar`

[Código](./classe_conta_corrente.py)



## 6. **Classe TV**

Faça um programa que simule um televisor:
- **Atributos**: canal, volume
- **Métodos**: `mudarCanal`, `aumentarVolume`, `diminuirVolume`
- **Validação**: manter canal e volume dentro de limites válidos.

[Código](./classe_tv.py)



## 7. **Classe Bichinho Virtual (Tamagushi)**

Crie uma classe que modele um Tamagushi:
- **Atributos**: nome, fome, saúde, idade
- **Métodos**: `alterarNome`, `alterarFome`, `alterarSaude`, `alterarIdade`, `retornarHumor`

[Código](./classe_bichinho.py)



## 8. **Classe Macaco**

Crie uma classe Macaco:
- **Atributos**: nome, bucho (lista de alimentos)
- **Métodos**: `comer`, `verBucho`, `digerir`
- **Extra**: Testar macaco canibal (um comer o outro)

[Código](./classe_macaco.py)



## 9. **Classe Ponto e Retângulo**

- Classe `Ponto`: atributos x e y
- Classe `Retangulo`: atributos largura, altura, ponto de origem (classe `Ponto`)
- **Funções**: imprimir ponto, encontrar centro do retângulo
- Criar menu para alterar retângulo e imprimir centro

[Código](./classe_ponto_retangulo.py)



## 10. **Classe Bomba de Combustível**

Crie uma classe chamada `BombaCombustivel`:
- **Atributos**: tipoCombustivel, valorLitro, quantidadeCombustivel
- **Métodos**:
  - `abastecerPorValor`
  - `abastecerPorLitro`
  - `alterarValor`
  - `alterarCombustivel`
  - `alterarQuantidadeCombustivel`

[Código](./classe_bomba.py)



## 11. **Classe Carro**

Crie uma classe Carro:
- **Atributos**: consumo (km/litro), combustível (inicia em 0)
- **Métodos**:
  - `andar(distancia)`
  - `obterGasolina()`
  - `adicionarGasolina(qtde)`

[Código](./classe_carro.py)



## 12. **Classe Conta de Investimento**

Crie uma classe `ContaInvestimento`:
- **Atributos**: saldo, taxaJuros
- **Método**: `adicioneJuros()`
- **Exemplo**: criar conta com R$1000, taxa 10%, aplicar juros 5 vezes

[Código](./classe_investimento.py)



## 13. **Classe Funcionário**

Crie uma classe Funcionário:
- **Atributos**: nome, salário
- **Métodos**: `getNome()`, `getSalario()`, `aumentarSalario(porcentagem)`

[Código](./classe_funcionario.py)



## 14. **Classe Bichinho Virtual++**

Melhore o programa do bichinho virtual:
- Especificar quantidade de comida e tempo de brincadeira
- "Porta escondida" que mostra valores exatos do objeto (`__str__`)
- Criar uma fazenda com vários bichinhos (lista de objetos)
- Controlar todos ao mesmo tempo (alimentar, brincar, ouvir)

[Código](./classe_bichinho_plus.py)

