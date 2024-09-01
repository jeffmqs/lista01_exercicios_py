"""8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
decrescente. """

def ordenar_decrescente():

    numeros = []

    
    for i in range(3):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º valor inteiro: "))
                if num in numeros:
                    print("Os valores devem ser distintos. Tente novamente.")
                else:
                    numeros.append(num)
                    break
            except ValueError:
                print("Entrada inválida. Digite um valor inteiro.")

   
    numeros.sort(reverse=True)


    print("Números em ordem decrescente:", numeros)


ordenar_decrescente()