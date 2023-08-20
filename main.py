from gera_lab_map2 import gera_lab
from Pilhas import Pilha

lab_1 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
          [' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'], 
          ['#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '], 
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

lab_2 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#'], 
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '#'], 
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'], 
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], 
          ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' '], 
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

lab_3 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
          ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'], 
          ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' '], 
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

def possiveis_passos(trajeto, pos_atual, meu_lab):

    direcoes = [( pos_atual[0], pos_atual[-1]+1 ),
                ( pos_atual[0]+1, pos_atual[-1] ),
                ( pos_atual[0], pos_atual[-1]-1 ),
                ( pos_atual[0]-1, pos_atual[-1] )]
    
    possiveis_passos = list()
    
    for direcao in direcoes:
        if meu_lab[direcao[0]][direcao[-1]] != "#":
            if direcao != trajeto.top():
                possiveis_passos.append(direcao)

    possiveis_passos.append(trajeto.top())

    return possiveis_passos

def proximo_passo(trajeto, pos_atual, meu_lab, ):
    """direita, baixo, esquerda, cima"""
    #1º passo sempre p/ direita
    ultima_pos = trajeto.top()

    if pos_atual == (1,0):
        if meu_lab[1][1] == '#':
            return False
        else:
            return (1,1)
    else:
        #direita
        #baixo
        #esquerda
        #cima
        '''
        if meu_lab[pos_atual[0], pos_atual[-1]+1] == " ":
            return (pos_atual[0], pos_atual[-1]+1)
        '''
        pass

trajetoria = Pilha()
trajetoria.push((1,0))
coordenada = (1,1)

print(possiveis_passos(trajetoria, coordenada, lab_2))