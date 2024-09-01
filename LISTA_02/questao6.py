"""6) Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são
VERDADEIROS ou FALSOS. """

def main():
    try:
      
        valor1 = input("Digite o primeiro valor booleano (True/False): ").strip().capitalize()
        valor1 = valor1 == "True"

       
        valor2 = input("Digite o segundo valor booleano (True/False): ").strip().capitalize()
        valor2 = valor2 == "True"

    
        if valor1 and valor2:
            print("Ambos os valores são VERDADEIROS.")
        elif not valor1 and not valor2:
            print("Ambos os valores são FALSOS.")
        else:
            print("Os valores são diferentes.")
    
    except ValueError:
        print("Por favor, insira valores booleanos válidos (True/False).")

if __name__ == "__main__":
    main()
