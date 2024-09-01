"""8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.A. contendo 10 valores. """


A = 3 
R = 5


sequencia_pa = []


for i in range(10):
  termo = A + i * R  
  sequencia_pa.append(termo)  


print("Sequência em P.A.:", sequencia_pa)