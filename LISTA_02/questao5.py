"""5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
imprimindo o resultado. """

def main():
    try:
 
        numero = float(input("Digite um número: "))
        
        
        if numero > 0:
            resultado = numero * 2
            print(f"O dobro de {numero} é {resultado}.")
        elif numero < 0:
            resultado = numero * 3
            print(f"O triplo de {numero} é {resultado}.")
        else:
            print("O número é zero, portanto, não tem dobro ou triplo.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
