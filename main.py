from gera_lab_map2 import *
from Pilhas import Pilha
from eh_possivel_sair import *

lab = gera_lab(7,15)

print_lab(lab)
caminho = Pilha()
INICIO = (1,0)
caminho.push(INICIO)
FIM = (len(lab)-2, len(lab[0])-1)
coordenadas_visitadas = []
print(eh_possivel_sair(lab, caminho, INICIO, FIM, coordenadas_visitadas))