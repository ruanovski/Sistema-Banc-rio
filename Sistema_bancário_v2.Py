import os
import time

class Banco:
    def __init__(self):
        self.usuarios = []
        self.agencia = "0001"
        self.contas = 0
        self.saldo = 0
        self.numero_de_saques = 0
        self.extrato = []
        self.QTD_LIMITE_SAQUES = 3
        self.VALOR_LIMITE_POR_SAQUE = 500

    def menu(self):
        menu_text = """
        Escolha uma operação bancária:
        Depositar = [D]
        Sacar = [S]
        Extrato = [E]
        Criar usuário = [U]
        Listar usuário = [L]
        Sair = [Q]
        """
        return input(menu_text).upper()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor}")
            print(f"\nSeu saldo atual é: {self.saldo}")
            time.sleep(3)
            os.system("clear")
        elif valor <= 0:
            print("\nNão é possível depositar um valor negativo ou nulo")
            time.sleep(3)
            os.system("clear")
        else:
            print("Você digitou um valor inválido")

    def sacar(self, valor):
        limite_valor_atingido = valor > self.VALOR_LIMITE_POR_SAQUE
        limite_saque_atingido = self.numero_de_saques >= self.QTD_LIMITE_SAQUES
        sem_saldo = valor > self.saldo

        if sem_saldo:
            print("\nVocê não tem saldo suficiente.")
        elif limite_valor_atingido:
            print(f"\nVocê atingiu o valor limite! O valor limite é: {self.VALOR_LIMITE_POR_SAQUE}")
        elif limite_saque_atingido:
            print("\nVocê excedeu o limite de saque")
        elif valor > 0:
            self.saldo -= valor
            self.numero_de_saques += 1
            self.QTD_LIMITE_SAQUES -= self.numero_de_saques
            self.extrato.append(f"Saque: -R${valor}")
            print(f"Valor sacado: {valor}")
        else:
            print("Você digitou uma opção inválida")

    def exibir_extrato(self):
        contador = 0
        print(f"Seu saldo atual é: {self.saldo}")
        if not self.extrato:
            print("Não houve nenhuma movimentação")
        else:
            for valores in self.extrato:
                contador += 1
                print(f"{contador}ª {valores}")

    def criar_usuario(self):
        cpf = input("Informe somente os números do CPF:")
        if len(cpf) != 11:
            print("Você digitou um número de CPF incorreto ou incluiu algo além de números.\nDigite apenas 11 números")
            time.sleep(3)
            os.system("clear")
        elif cpf in [user["cpf"] for user in self.usuarios]:
            print("Esse CPF está vinculado a um usuário no sistema!")
            time.sleep(3)
        else:
            self.contas += 1
            print("Criando uma conta e usuário para o cliente")
            nome = input("\nInforme seu nome: ")
            data_nascimento = input("\nInforme sua data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "conta": self.contas})

    def listar_usuario(self):
        cpf = input("Digite o CPF do usuário:")
        for usuario in self.usuarios:
            if cpf == usuario["cpf"]:
                print(f"Nome: {usuario['nome']}, Data de nascimento: {usuario['data_nascimento']}, Conta: {usuario['conta']}")
                time.sleep(3)
                return
        print("Nenhum usuário encontrado")

    def iniciar(self):
        while True:
            os.system("clear")
            opcao = self.menu()

            if opcao == "D":
                os.system("clear")
                print("==========Depositar==========")
                valor = float(input("Digite o valor que deseja depositar:"))
                self.depositar(valor)

            elif opcao == "S":
                os.system("clear")
                print("==========Saque==========")
                print(f"Seu saldo atual é: R${self.saldo} \nSeu limite de saque é: {self.QTD_LIMITE_SAQUES}")
                print(f"\nVocê já fez {self.numero_de_saques} saques")
                valor = float(input("\nDigite o valor que deseja sacar:"))
                self.sacar(valor)

            elif opcao == "E":
                os.system("clear")
                print("==========Extrato==========")
                self.exibir_extrato()

            elif opcao == "U":
                os.system("clear")
                print("==========Cadastrando usuário==========")
                self.criar_usuario()

            elif opcao == "L":
                os.system("clear")
                print("==========Listando usuário==========")
                self.listar_usuario()

            elif opcao == "Q":
                break

if __name__ == "__main__":
    banco = Banco()
    banco.iniciar()
