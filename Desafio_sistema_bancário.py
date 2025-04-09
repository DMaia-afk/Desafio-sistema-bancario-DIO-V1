## Importando bibliotecas para o projeto
from datetime import date, datetime
import pytz


## Menu principal
menu = f'''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>'''
# Básico
total_de_saques = 0 # Contagem de saque no total
total_de_transacoes = 0 # Contagem de transações no total
saldo = 0 # Saldo inicial
extrato = "" # String que recebe todas movimentações
LIMITE_POR_SAQUE = 500 # Limite por saque
LIMITE_DE_SAQUE = 3 # Limite de saques
LIMITE_DE_TRANSACOES_POR_DIA = 10 # Limite de transações

# Data/hora
data = None 
data_formatada = None

def get_hours():
    hours = pytz.timezone("America/Sao_Paulo")
    return datetime.now(hours).strftime("%d/%m/%Y %H:%M")



## Função de depósito
def depositando_valor():
    global total_de_transacoes, saldo, extrato
    
    valor_depositado = input("""Insira o valor você deseja depositar: """)
    extrato += f"|    Depósito: {float(valor_depositado):.2f}\n"
    print("\n---Parabéns, seu depósito foi realizado com sucesso!---")
    saldo += float(valor_depositado)
    total_de_transacoes += 1

## Função de saque
def sacando_valor():
    global total_de_transacoes, extrato, total_de_saques, saldo, LIMITE_POR_SAQUE

    valor_sacado = input("""Insira o valor você deseja sacar: """)
    
    
    if float(valor_sacado) > saldo:
        print("""\n---SAQUE NÃO EFETUADO, VERIFIQUE SEU SALDO---""")

    elif float(valor_sacado) > LIMITE_POR_SAQUE:
        print("""\n---VOCÊ ULTRAPASSOU O LIMITE DISPONÍVEL PARA O SAQUE ATUAL---""")

    else:
        print("\n---Parabéns, seu saque foi realizado com sucesso!---")
        total_de_saques += 1
        saldo -= float(valor_sacado)
        extrato += f"|    Saque: {float(valor_sacado):.2f}\n"
        total_de_transacoes += 1


## Laço do menu
while True:

    escolha = input(menu)

    if escolha == "d":
        if LIMITE_DE_TRANSACOES_POR_DIA <= total_de_transacoes:
            print("\n---LIMITE DE TRANSAÇÕES ATINGIDO, RETORNE NO PRÓXIMO DIA---")
        else:
            data = datetime.now()
            data_formatada = datetime.strftime(data, "%d/%m/%Y %H:%M")
            extrato += f"|    Data/Hora: {data_formatada}\n"
            depositando_valor()
        
    elif escolha == "s":
        
        if total_de_saques >= LIMITE_DE_SAQUE:
            print("""\n---VOCÊ JÁ ATINGIU O LIMITE DE SAQUES POSSÍVEIS POR HOJE---""")

        elif LIMITE_DE_TRANSACOES_POR_DIA <= total_de_transacoes:
            print("\n---LIMITE DE TRANSAÇÕES ATINGIDO, RETORNE NO PRÓXIMO DIA---")

        else:
            data = datetime.now()
            data_formatada = datetime.strftime(data, "%d/%m/%Y %H:%M")
            extrato += f"|    Data/Hora: {data_formatada}\n"
            sacando_valor()
        
    elif escolha == "e":
        if saldo <= 0:
            print("\n---Por favor, nenhum valor identificado no saldo. Caso o erro se repita, contate nossa gerencia pelo suporte!---")

        else:
            print("-_-_-_-_-_-_- EXTRATO -_-_-_-_-_-")
            print(extrato)
        

    elif escolha == "q":
        break

    else:
        print("\n---Por favor, escolha uma das opções acima para que possamos prosseguir com o serviço. O Banco D.M agradece sua compreensão.---")

