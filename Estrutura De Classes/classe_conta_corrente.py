class Conta_Corrente:
    def __init__(self,conta,correntista,saldo):
        self.conta=conta
        self.correntista=correntista
        self.saldo=saldo
    
    def alterar_nome(self,novo_nome):
        self.correntista=novo_nome
        print(f'O novo nome da conta é {self.correntista}')
    
    def depositar(self,valor_deposito):
        self.saldo=self.saldo+valor_deposito
        print(f'O novo saldo é {self.saldo}')

    def saque (self,valor_saque):
        self.saldo=self.saldo-valor_saque
        print(f'O valor do saldo agora é {self.saldo}')
    
conta1=Conta_Corrente(2131,'Zack Rodrigues',100000)

conta1.alterar_nome('Eduardo Manches')
conta1.depositar(100)
conta1.saque(50)


