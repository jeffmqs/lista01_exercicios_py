""""4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
terminar quando for lido um número negativo."""

def main():
    
    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0
    
    print("Digite números para contagem nos intervalos (digite um número negativo para sair):")
    
    while True:
        try:
          
            numero = float(input())
            
           
            if numero < 0:
                break
            
       
            if 0 <= numero <= 25:
                intervalo_0_25 += 1
            elif 26 <= numero <= 50:
                intervalo_26_50 += 1
            elif 51 <= numero <= 75:
                intervalo_51_75 += 1
            elif 76 <= numero <= 100:
                intervalo_76_100 += 1
        except ValueError:
            print("Por favor, insira um número válido ou um número negativo para sair.")
            continue
    
  
    print("\nContagem de números em cada intervalo:")
    print(f"[0-25]: {intervalo_0_25}")
    print(f"[26-50]: {intervalo_26_50}")
    print(f"[51-75]: {intervalo_51_75}")
    print(f"[76-100]: {intervalo_76_100}")

if __name__ == "__main__":
    main()
