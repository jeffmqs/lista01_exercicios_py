"""10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120"""

def main():
    try:
     
        A = int(input("Digite um número para calcular o fatorial: "))
        
        if A < 0:
            print("O fatorial não é definido para números negativos.")
            return
        
        
        fatorial = 1
        sequencia = ""
        
       
        for i in range(A, 0, -1):
            fatorial *= i
            sequencia += str(i) + " X " if i > 1 else str(i)
        
       
        print(f"\n{A}! = {sequencia} = {fatorial}")
    
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
