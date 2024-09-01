#3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. 

def verificar_par_impar(numero):
 
  if numero % 2 == 0:
    print(f"O número {numero} é par.")
  else:
    print(f"O número {numero} é ímpar.")


verificar_par_impar(7)