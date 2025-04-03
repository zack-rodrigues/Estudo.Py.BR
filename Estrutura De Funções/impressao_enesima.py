def triangulo():
    n=int(input('Digite um número inteiro: '))
    for i in range(1,n+1):
        print((str(i)+' ')* i)

triangulo()

#ou

def triangulo(n):
    for i in range(1,n+1):
        print((str(i)+' ')*i)

n=int(input('Digite um número inteiro: '))
triangulo(n)  # Passamos 'n' como argumento
