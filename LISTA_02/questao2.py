"""2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
estado civil seja “CASADA”, solicitar o tempo de casada (anos). 
"""

def obter_informacoes_pessoa():
    nome = input("Digite o seu nome: ")
    sexo = input("Digite o seu sexo (M/F): ").upper()  
    estado_civil = input("Digite o seu estado civil: ").upper()

    if sexo == "F" and estado_civil == "CASADA":
        tempo_casada = int(input("Digite o tempo de casada (em anos): "))
        print(f"{nome}, sexo {sexo}, estado civil {estado_civil}, casada há {tempo_casada} anos.")
    else:
        print(f"{nome}, sexo {sexo}, estado civil {estado_civil}.")

obter_informacoes_pessoa()