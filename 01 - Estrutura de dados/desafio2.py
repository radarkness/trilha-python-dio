from datetime import date

class Usuario:
    def __init__(self, nome_completo, cpf, endereco):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, titular, agencia, conta, saldo=950):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extratos = []
        self.saques_diarios = 0
        self.ultimo_saque_data = None
        self.limite_saques = 3
        self.limite_valor_saque = 500

    def atualizar_limite_saques(self):
        if self.ultimo_saque_data != date.today():
            self.saques_diarios = 0
            self.ultimo_saque_data = date.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extratos.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, *, valor):
        self.atualizar_limite_saques()
        if self.saques_diarios >= self.limite_saques:
            print("Limite de saques diários atingido!")
        elif valor > self.limite_valor_saque:
            print(f"Valor do saque excede o limite de R${self.limite_valor_saque:.2f} por saque!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor <= 0:
            print("Valor de saque inválido!")
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extratos.append(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def ver_extratos(self):
        print(f"Extratos da conta de {self.titular.nome_completo} (Agência: {self.agencia}, Conta: {self.conta}):")
        if not self.extratos:
            print("Não há movimentações na conta.")
        else:
            for extrato in self.extratos:
                print(extrato)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_diarios}/{self.limite_saques}")

def criar_usuario():
    nome_completo = input("Digite o nome completo do usuário: ")
    while True:
        cpf = input("Digite o CPF (somente números): ")
        if cpf.isdigit():
            break
        else:
            print("CPF inválido! Digite apenas números.")
    endereco = input("Digite o endereço (Logradouro, número, bairro, município, estado): ")
    
    return Usuario(nome_completo, cpf, endereco)

def criar_conta_bancaria(usuarios):
    cpf = input("Digite o CPF do usuário para criar a conta bancária: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if usuario:
        agencia = input("Digite o número da agência: ")
        conta = input("Digite o número da conta: ")
        nova_conta = ContaBancaria(titular=usuario, agencia=agencia, conta=conta)
        print(f"Conta bancária criada para {usuario.nome_completo} na agência {agencia}, conta {conta} com sucesso!")
        return nova_conta
    else:
        print("Usuário não encontrado!")
        return None

def ver_usuarios_cadastrados(usuarios):
    print("Usuários cadastrados:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(usuario.nome_completo)

def menu():
    usuarios = []
    contas = []

    while True:
        print("\nMenu Principal:")
        print("1. Criar novo usuário")
        print("2. Criar nova conta bancária")
        print("3. Realizar operação em uma conta bancária")
        print("4. Ver usuários cadastrados")
        print("5. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            usuario = criar_usuario()
            if any(u.cpf == usuario.cpf for u in usuarios):
                print("Usuário com este CPF já existe!")
            else:
                usuarios.append(usuario)
                print(f"Usuário {usuario.nome_completo} criado com sucesso!")
        elif opcao == '2':
            nova_conta = criar_conta_bancaria(usuarios)
            if nova_conta:
                contas.append(nova_conta)
        elif opcao == '3':
            cpf = input("Digite o CPF do titular da conta bancária: ")
            conta = next((c for c in contas if c.titular.cpf == cpf), None)
            if conta:
                while True:
                    print(f"\nBem-vindo, {conta.titular.nome_completo}! Escolha uma operação:")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Ver extratos")
                    print("4. Voltar ao menu principal")
                    operacao = input("Digite o número da operação desejada: ")

                    if operacao == '1':
                        valor = float(input("Digite o valor a ser depositado: "))
                        conta.depositar(valor)
                    elif operacao == '2':
                        valor = float(input("Digite o valor a ser sacado: "))
                        conta.sacar(valor=valor)
                    elif operacao == '3':
                        conta.ver_extratos()
                    elif operacao == '4':
                        break
                    else:
                        print("Opção inválida! Por favor, escolha uma operação válida.")
            else:
                print("Usuário não encontrado ou Cadastrado! Cliente deve estar cadastrado primeiro, para saber acesse a opção 4. Se foi feito o cadastro, verifique os numeros e tente novamente.")
        elif opcao == '4':
            ver_usuarios_cadastrados(usuarios)
        elif opcao == '5':
            print("Encerrando o sistema bancário. Obrigado por usar nossos serviços!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
