import random

def lancar_dados():
    """Simula o lançamento de dois dados e retorna a soma."""
    return random.randint(1, 6) + random.randint(1, 6)


def jogar_craps():
    """Implementa o jogo de Craps."""
    print("\n==== JOGO DE CRAPS ====\n")
    primeiro_lancamento = lancar_dados()
    print(f"Você lançou {primeiro_lancamento}")
    
    if primeiro_lancamento in [7, 11]:
        print("Natural! Você ganhou! 🏆")
    elif primeiro_lancamento in [2, 3, 12]:
        print("Craps! Você perdeu! 😢")
    else:
        ponto = primeiro_lancamento
        print(f"Seu Ponto é {ponto}. Continue jogando até tirar {ponto} novamente ou um 7 para perder.")
        
        while True:
            entrada = input("Pressione Enter para lançar os dados...")
            novo_lancamento = lancar_dados()
            print(f"Você lançou {novo_lancamento}")
            
            if novo_lancamento == ponto:
                print("Parabéns! Você tirou seu Ponto e ganhou! 🏆")
                break
            elif novo_lancamento == 7:
                print("Você tirou 7 antes do Ponto. Você perdeu! 😢")
                break


jogar_craps()
