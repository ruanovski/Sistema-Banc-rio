import os
import time


def menu():
    menu = """
Escolhe uma operação bancária:

Depositar = [D]

Sacar = [S]

Extrato = [E]

Criar usuário = [U]

Listar usuário = [L]

Sair = [Q]

"""
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: +R${valor}")
        print(f"\nSeu saldo atual é: {saldo}")
        time.sleep(3)
        os.system("clear")
    elif valor <= 0:
        print("\nNão é possivel depositar um valor negativou ou nulo")
        time.sleep(3)
        os.system("clear")
    else:
        print("Você digitou um valor inválido")

    return saldo, extrato


def saque(*, saldo, valor, extrato, numero_de_saques, QTD_LIMITE_SAQUES, VALOR_LIMITE_POR_SAQUE):
    limite_valor_atingido = valor > VALOR_LIMITE_POR_SAQUE
    limite_saque_atingido = numero_de_saques >= QTD_LIMITE_SAQUES
    sem_saldo = valor > saldo

    if sem_saldo:
        print("\nVocê não tem saldo suficiente.")
        time.sleep(3)
        os.system("clear")
    elif limite_valor_atingido:
        print(
            f"\nVocê atingiu o valor limite! O valor limite é: {VALOR_LIMITE_POR_SAQUE}")
        time.sleep(3)
        os.system("clear")
    elif limite_saque_atingido:
        print("\nVocê exceddeu o limite de saque")
        time.sleep(3)
        os.system("clear")
    elif valor > 0:
        saldo -= valor
        numero_de_saques += 1
        QTD_LIMITE_SAQUES -= numero_de_saques
        extrato.append(f"Saque: -R${valor}")
        print(f"Valor sacado: {valor}")
        time.sleep(3)
        os.system("clear")
    else:
        print("Você digitou uma opção inválida")
        time.sleep(3)
        os.system("clear")

    return saldo, extrato, numero_de_saques


def exibir_extrato(saldo, /, *, extrato):
    contador = 0
    print(f"Seu saldo atual é: {saldo}")
    if not extrato:
        print("Não houve nenhuma moviemntação")
        time.sleep(3)
        os.system("clear")
    else:
        for valores in extrato:
            contador += 1
            print(f"{contador}ª {valores}")
        time.sleep(3)
        os.system("clear")
    return saldo, extrato


def criar_usuario(usuarios, agencia, contas):
    cpf = input("Informe somente os números do cpf:")
    if len(cpf) != 11:
        print("Você digitou um número de cpf errado ou colocou algo além de números.\n Digite apenas 11 números")
        time.sleep(3)
        os.system("clear")
    elif cpf in usuarios:
        print("Esse cpf está vinculado a um usuário no sistema!")
        time.sleep(3)
    else:
        contas += 1
        print("Criando uma conta e usuário para o cliente")
        nome = input("\nInforme seu nome: ")
        data_nascimento = input(
            "\nInforme sua data de nascimento (dd-mm-aaaa): ")
        endereco = input(
            "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "conta": contas})
    return usuarios


def listar_usuario(usuarios):
    cpf = input("Digite o cpf do usuário:")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print(f"Nome: {usuario['nome']}, Data de nascimento: {usuario['data_nascimento']}, conta: {usuario['conta']}")
            time.sleep(3)
        else:
            print("Nenhum usuário encontrado")


def inciar():
    usuarios = []
    agencia = "0001"
    contas = 0
    saldo = 0
    numero_de_saques = 0
    extrato = []
    QTD_LIMITE_SAQUES = 3
    VALOR_LIMITE_POR_SAQUE = 500

    while True:
        os.system("clear")
        opcao = menu().upper()

        if opcao == "D":
            os.system("clear")
            print("==========Depositar==========")
            valor = float(input("Digite o valor que deseja depositar:"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            os.system("clear")
            print("==========Saque==========")
            print(
                f"Seu saldo atual é: R${saldo} \nSeu limite de saque é: {QTD_LIMITE_SAQUES}")
            print(f"\n Você já fez {numero_de_saques} saques")
            valor = float(input("\nDigite o valor que deseja sacar:"))
            saldo, extrato, numero_de_saques = saque(saldo=saldo, valor=valor, extrato=extrato,
                                                     numero_de_saques=numero_de_saques,
                                                     QTD_LIMITE_SAQUES=QTD_LIMITE_SAQUES,
                                                     VALOR_LIMITE_POR_SAQUE=VALOR_LIMITE_POR_SAQUE,
                                                     )

        elif opcao == "E":
            os.system("clear")
            print("==========Extrato==========")
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "U":
            os.system("clear")
            print("==========Cadastrando usuário==========")
            usuarios = criar_usuario(usuarios, agencia, contas)
      
        elif opcao == "L":
            os.system("clear")
            print("==========Listando usuário==========")
            listar_usuario(usuarios)

        elif opcao == "Q":
            break


inciar()
