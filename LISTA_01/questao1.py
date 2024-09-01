""" 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
três e que se encontram no conjunto dos números de 1 até 500.""" 

def main():
    soma = 0


    for numero in range(1, 501):
     
        if numero % 2 != 0 and numero % 3 == 0:
            soma += numero

  
    print(f"A soma de todos os números ímpares que são múltiplos de três de 1 a 500 é: {soma}")

if __name__ == "__main__":
    main()
