"""10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2

Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
com a tabela abaixo.
IMC em adultos Condição
Abaixo de 18,5 Abaixo do peso
Entre 18,5 e 25 Peso normal
Entre 25 e 30 Acima do peso
Acima de 30 obeso """

def calcular_imc(peso, altura):

  imc = peso / (altura ** 2)
  return imc

def mostrar_condicao(imc):

  if imc < 18.5:
    print("Abaixo do peso")
  elif 18.5 <= imc < 25:
    print("Peso normal")
  elif 25 <= imc < 30:
    print("Acima do peso")
  else:
    print("Obeso")


peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))


imc = calcular_imc(peso, altura)


print(f"Seu IMC é: {imc:.2f}") 
mostrar_condicao(imc)