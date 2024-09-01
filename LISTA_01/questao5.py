"""5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero."""


quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_total = 0
quantidade_total = 0


while True:
    numero = int(input("Digite um número positivo (0 para encerrar): "))

   
    if numero == 0:
        break

    if numero > 0:
        soma_total += numero
        quantidade_total += 1

        
        if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1


media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_geral = soma_total / quantidade_total


print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")