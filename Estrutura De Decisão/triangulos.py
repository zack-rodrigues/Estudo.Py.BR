lado1=float(input('Digite as medidas do primeiro lado do triângulo: '))
lado2=float(input('Digite as medidas do segundo lado do triângulo: '))
lado3=float(input('Digite as medidas do terceiro lado do triângulo: '))

lados={lado1,lado2,lado3}  # usar {} é tipo uma lista [], maaas , ele só retorna 1x o valor    #
                           # caso esteja duplicado, dai foi só fazer os elifs sem muito código,#
                           # caso não queria usar esse estilo, vai ter que fazer uns 9..       #                    #
                           # elif...x-x então assim é mais inteligente                         #
                           
tipo=''  #var com string vazia, não era necessario... mas to testando

if len(lados)==1:       # o pulo do gato é, len() conta a quantidade de elementos dentro de ()     #
    tipo='Equilatero'   # Ou seja se retornou apenas o valor 1 do conjunto de elementos unicos {}, #
                        #  significa que todos os lados são iguais logo é equilatero e é isso      #

elif len(lados)==2:
    tipo='Isoceles'
                          
else:
    tipo='Escaleno'


print(f'Seu triangulo é... {tipo} !!!')

   










