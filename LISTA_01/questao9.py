"""9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.G. contendo 10 valores."""


A = 2
R = 3


sequencia_pg = []


for i in range(10):
  termo = A * R**i  
  sequencia_pg.append(termo) 


print("Sequência em P.G.:", sequencia_pg)