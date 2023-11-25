import os
import time
menu = """
Escolhe uma operação bancária:

Depositar = [D]

Sacar = [S]

Extrato = [E]

Sair = [Q]


"""


saldo = 0
numero_de_saques = 0
extrato = []
QTD_LIMITE_SAQUES = 3
VALOR_LIMITE_POR_SAQUE = 500

while True:
    os.system('clear')
    alternativa_escolhida = input(menu).upper()

    if alternativa_escolhida == "D":
        os.system('clear')
        print("Depósito")
        valor_depositado = float(
            input("Informe o valor que deseja depositar: "))
        if valor_depositado > 0:
            os.system('clear')
            saldo += valor_depositado
            extrato.append(f"Depósito --> + R$:{str(valor_depositado)}")
            print(f"O valor R${valor_depositado} foi depositado")
            print(f"Seu saldo é: {saldo}")
            time.sleep(3)
            continue
        elif valor_depositado < 0:
            os.system('clear')
            print("O valor de depósito não pode ser negativo")
            time.sleep(3)
            continue
        else:
            os.system('clear')
            print("Você digitou uma opção inválida")
            time.sleep(3)
            continue
    elif alternativa_escolhida == "S":
        os.system('clear')
        print("Saque")
        print(f"Seu saldo atual é: {saldo}")
        print(f"Quantidade de saques ainda disponíveis: {QTD_LIMITE_SAQUES}")
        if saldo > 0 and QTD_LIMITE_SAQUES > 0:
            valor_sacar = float(input("Informa quanto você deseja sacar: "))
            if valor_sacar > 0 and valor_sacar <= saldo and \
                    valor_sacar <= VALOR_LIMITE_POR_SAQUE:
                os.system('clear')
                saldo -= valor_sacar
                QTD_LIMITE_SAQUES -= 1
                extrato.append(f"Saque -> - R$: {str(valor_sacar)}")
                print(f"R$ {valor_sacar} sacado!")
                time.sleep(3)
                continue
            elif valor_sacar < 0 or valor_sacar > saldo:
                os.system('clear')
                print("Valor inválido ou valor maior que o saldo!")
                print(f"seu saldo atual é: {saldo}")
                time.sleep(3)
                continue
            elif valor_sacar > VALOR_LIMITE_POR_SAQUE:
                os.system('clear')
                print("Você excedeu o valor limite por saque!")
                print(f"O valor limite por saque é: {VALOR_LIMITE_POR_SAQUE}")
                time.sleep(3)
                continue
            else:
                os.system('clear')
                print("Digite um valor válido")
                time.sleep(3)
                continue
        elif saldo > 0 and QTD_LIMITE_SAQUES <= 0:
            os.system('clear')
            print("Você atingiu o valor limite de saque")
            time.sleep(3)
            continue
        else:
            os.system('clear')
            print(f"Saldo insuficiente! Seu saldo atual é: {saldo}")
            time.sleep(3)
            continue
    elif alternativa_escolhida == "E":
        os.system('clear')
        print("Extrato")
        contador_sequencia = 0
        if len(extrato) == 0:
            print("Não foram realizadas movimentações!")
            time.sleep(3)
        else:
            for transações in extrato:
                contador_sequencia += 1
                print(f"{contador_sequencia}ª: {transações}")
            time.sleep(4)
            continue  
    elif alternativa_escolhida == "Q":
        print("Saindo do sistema, até logo!")
        time.sleep(3)
        os.system('clear')
        break
