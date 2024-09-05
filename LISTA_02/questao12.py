"""12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas
3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
aproveitamento, usando a fórmula:
MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno,
suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a
mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.
Média de aproveitamento Conceito
>= 90 A
>= 75 e < 90 B
>= 60 e < 75 C
>= 40 e < 60 D
< 40 E """

def calcular_conceito(ma):
   
    if ma >= 90:
        return 'A', 'Aprovado'
    elif ma >= 75:
        return 'B', 'Aprovado'
    elif ma >= 60:
        return 'C', 'Aprovado'
    elif ma >= 40:
        return 'D', 'Reprovado'
    else:
        return 'E', 'Reprovado'

def calcular_media_aproveitamento(nota1, nota2, nota3, me):
    
    ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7
    return ma


num_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media_exercicios = float(input("Digite a média dos exercícios: "))


ma = calcular_media_aproveitamento(nota1, nota2, nota3, media_exercicios)


conceito, status = calcular_conceito(ma)


print(f"Número do Aluno: {num_identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos Exercícios: {media_exercicios}")
print(f"Média de Aproveitamento: {ma:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")
