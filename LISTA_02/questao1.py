#1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menorque C. 

def verificar_soma():

    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))

    if A + B < C:
        print("A soma de A + B é menor que C.")
    else:
        print("A soma de A + B não é menor que C.")

verificar_soma()