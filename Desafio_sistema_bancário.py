## Variáveis básicas
menu = f'''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>'''

saldo = 0
extrato = ""
limite_por_saque = 500
LIMITE_DE_SAQUE = 3
total_de_saques = 0
depositos = []
saques = []

## Função de depósito
def depositando_valor():
    global saldo
    global depositos
    valor_depositado = input("""Insira o valor você deseja depositar: """)
    depositos += [valor_depositado]
    print("Parabéns, seu depósito foi realizado com sucesso!")
    saldo += float(valor_depositado)

## Função de saque
def sacando_valor():
    global saques
    global total_de_saques
    global saldo
    global limite_por_saque
    valor_sacado = input("""Insira o valor você deseja sacar: """)
    total_de_saques += 1
    
    if float(valor_sacado) > saldo:
        print("""###SAQUE NÃO EFETUADO, VERIFIQUE SEU SALDO###""")

    elif float(valor_sacado) > limite_por_saque:
        print("""###VOCÊ ULTRAPASSOU O LIMITE DISPONÍVEL PARA O SAQUE ATUAL###""")

    else:
        print("Parabéns, seu saque foi realizado com sucesso!")
        saldo -= float(valor_sacado)
        saques += [valor_sacado]


## Laço do menu
while True:

    escolha = input(menu)

    if escolha == "d":
        depositando_valor()
        
    elif escolha == "s":
        
        if total_de_saques >= LIMITE_DE_SAQUE:
            print("""###VOCÊ JÁ ATINGIU O LIMITE DE SAQUES POSSÍVEIS POR HOJE###""")
        else:
            sacando_valor()
        
    elif escolha == "e":
        print(f"Seus depósitos: {depositos}")
        print(f"Seus saques: {saques}")
        print(f"Seu saldo: {saldo}")
        
    elif escolha == "q":
        break

    else:
        print("Por favor, escolha uma das opções acima para que possamos prosseguir com o serviço. O Banco D.M agradece sua compreensão.")

