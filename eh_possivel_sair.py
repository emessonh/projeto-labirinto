from Pilhas import *

# vai caminhando
def passo(labirinto, caminho, co_inicio, co_fim, co_visitadas):
    pos_atual = caminho.top()
    
    # verifica se chegou no fim
    if pos_atual == co_fim:
        return True
    
    #verifica se há uma parede e se a casa já foi visitada
    elif labirinto[pos_atual[0]][pos_atual[1]+1] != "#" and (pos_atual[0],pos_atual[1]+1) not in            co_visitadas:
            # anda pra direita
            # coloca na pilha o caminho que ele está fazendo
            caminho.push((pos_atual[0],pos_atual[1]+1))
            # registra a casa visitada
            co_visitadas.append((pos_atual[0],pos_atual[1]+1))
    else:
        
        #verifica se há uma parede e se a casa já foi visitada
        if labirinto[pos_atual[0]+1][pos_atual[1]] != "#" and (pos_atual[0]+1,pos_atual[1]) not in      co_visitadas:
            # anda pra baixo
            # coloca na pilha o caminho que ele está fazendo
            caminho.push((pos_atual[0]+1,pos_atual[1]))
            # registra a casa visitada
            co_visitadas.append((pos_atual[0]+1,pos_atual[1]))
        else:
            #verifica se há uma parede e se a casa já foi visitada
            if labirinto[pos_atual[0]-1][pos_atual[1]] != "#" and (pos_atual[0]-1,pos_atual[1]) not     in co_visitadas:
                # anda pra cima
                # coloca na pilha o caminho que ele está fazendo
                caminho.push((pos_atual[0]-1,pos_atual[1]))
                # registra a casa visitada
                co_visitadas.append((pos_atual[0]-1,pos_atual[1])) 
            else:
                # volta uma casa
                caminho.pop()
                # retorna false caso volte para o ponto inicial
                if pos_atual == (1,0):
                    return False
    # chama a funcao recursivamente          
    return passo(labirinto, caminho, co_inicio, co_fim, co_visitadas)
                
    
                
def eh_possivel_sair(labirinto, caminho, co_inicio, co_fim, co_visitadas):
    saida_barrada = passo(labirinto, caminho, co_inicio, co_fim, co_visitadas)
    return saida_barrada