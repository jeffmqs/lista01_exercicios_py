"""11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.

Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em duas vezes, preço normal de etiqueta mais juros de 10% 
"""

def calcular_media_e_conceito():
  
    identificacao = int(input("Digite o número de identificação do aluno: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media_exercicios = float(input("Digite a média dos exercícios: "))

    
    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

   
    if media_aproveitamento >= 90:
        conceito = "A"
    elif media_aproveitamento >= 75:
        conceito = "B"
    elif media_aproveitamento >= 60:
        conceito = "C"
    elif media_aproveitamento >= 40:
        conceito = "D"
    else:
        conceito = "E"

    # Verificação de aprovação/reprovação
    if conceito in ("A", "B", "C"):
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    # Saída de dados
    print("\n--- Resultados ---")
    print(f"Número do aluno: {identificacao}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média dos exercícios: {media_exercicios}")
    print(f"Média de aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
    print(f"Resultado: {resultado}")


calcular_media_e_conceito()