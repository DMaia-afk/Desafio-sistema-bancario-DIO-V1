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
total_de_transacoes = 0



## Função de depósito
def depositando_valor():
    global saldo
    global extrato
    valor_depositado = input("""Insira o valor você deseja depositar: """)
    extrato += f"Depósito: {float(valor_depositado):.2f} \n"
    print("Parabéns, seu depósito foi realizado com sucesso!")
    saldo += float(valor_depositado)

## Função de saque
def sacando_valor():
    global extrato
    global total_de_saques
    global saldo
    global limite_por_saque
    valor_sacado = input("""Insira o valor você deseja sacar: """)
    
    
    if float(valor_sacado) > saldo:
        print("""###SAQUE NÃO EFETUADO, VERIFIQUE SEU SALDO###""")

    elif float(valor_sacado) > limite_por_saque:
        print("""###VOCÊ ULTRAPASSOU O LIMITE DISPONÍVEL PARA O SAQUE ATUAL###""")

    else:
        print("Parabéns, seu saque foi realizado com sucesso!")
        total_de_saques += 1
        saldo -= float(valor_sacado)
        extrato += f"Saque: {float(valor_sacado):.2f} \n"


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
        print(extrato)
        
    elif escolha == "q":
        break

    else:
        print("Por favor, escolha uma das opções acima para que possamos prosseguir com o serviço. O Banco D.M agradece sua compreensão.")

