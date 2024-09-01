"""9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
● para homens: (72.7 * h) – 58;
● para mulheres: (62.1 * h) – 44.7. """

def main():
    try:
        
        altura = float(input("Digite a altura da pessoa (em metros): "))
        
       
        sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").strip().upper()

        
        if sexo == "M":
            peso_ideal = (72.7 * altura) - 58
            print(f"O peso ideal para um homem de altura {altura} m é: {peso_ideal:.2f} kg")
        elif sexo == "F":
            peso_ideal = (62.1 * altura) - 44.7
            print(f"O peso ideal para uma mulher de altura {altura} m é: {peso_ideal:.2f} kg")
        else:
            print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
    
    except ValueError:
        print("Por favor, insira valores válidos para altura e sexo.")

if __name__ == "__main__":
    main()
