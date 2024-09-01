"""""3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos. 
"""
def main():
    valores = []
    positivos = 0
    negativos = 0
    
    print("Digite os valores (digite 'q' para sair):")
    
    while True:
        entrada = input()
        
        if entrada.lower() == 'q':
            break
            
        try:
            valor = float(entrada)
            valores.append(valor)
            
            if valor > 0:
                positivos += 1
            elif valor < 0:
                negativos += 1
        except ValueError:
            print("Por favor, insira um número válido ou 'q' para sair.")
            continue
    
    if valores:
        media = sum(valores) / len(valores)
        total = len(valores)
        percentual_positivos = (positivos / total) * 100
        percentual_negativos = (negativos / total) * 100
        
        print(f"\nMédia aritmética: {media:.2f}")
        print(f"Quantidade de valores positivos: {positivos}")
        print(f"Quantidade de valores negativos: {negativos}")
        print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
        print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
    else:
        print("\nNenhum valor foi inserido.")
        
if __name__ == "__main__":
    main()
