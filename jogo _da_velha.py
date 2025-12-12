import numpy as np

def colocar_peca(tabuleiro , linha , coluna , peca):
    """"Coloca a peça do jogador na posição escolhida"""
    
    tabuleiro[linha][coluna] = peca

def verificar_vitoria(tabuleiro , peca):
    """Verifica se o jogador ganhou o jogo"""
    linhas = np.any(np.all(tabuleiro == peca , axis=1))
    colunas = np.any(np.all(tabuleiro == peca , axis=0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    """Imprimir o tabuleiro de forma legivel para o jogador """
    for linha in tabuleiro:
        print(" | ".join(str(x) if x !=0 else " " for x in linha))
        print( "-"*8)

def jogo ():
    """ Função principal para rodar jogo da velha"""
    tabuleiro = np.zeros((3,3), dtype=int)

    peca_atual = 1
    vencedor = False
    empate = False
    
    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)

        while True:
            try:
                linha = int(input(f"jogador {peca_atual}, escolha a linha (0,1,2):"))
                coluna = int(input(f"jogador {peca_atual}, escolha a coluna(0,1,2):"))
                
                #verifica se alinha e a coluna são validas 
                
                if linha not in [0,1,2] or coluna not in [0,1,2]:
                    print("\n Escolha linhas e colunas válidas ! de 0 a 2. \n")
                    continue
                #verifica se a linha já está ocupada 
                if tabuleiro[linha][coluna] !=0:
                    print("\nPosição ocupada ! Tente novamente. \n")
                    continue

                colocar_peca(tabuleiro,linha,coluna,peca_atual)
                vencedor = verificar_vitoria(tabuleiro, peca_atual)

                # se ouve empate 
                if np.all(tabuleiro !=0):
                    empate = True
                    
                break
            except ValueError:
                print("\nEntrada invalida! por favor insira numros inteiros de 0 a 2. \n")
        
        #troca de jogador 
        if not vencedor and not empate:
            peca_atual =2 if peca_atual == 1 else 1
    imprimir_tabuleiro(tabuleiro)
    if vencedor:
        print(f"\n\n\tParabéns jogador {peca_atual} venceu ! ")
    else:
        print("\n\n\tEmpate")
        
jogo()
