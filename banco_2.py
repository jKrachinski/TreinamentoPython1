import datetime as dt

# Esse código utilizando classes seria muito mais eficiente, mas buscando utilizar o aprendizado, vamos utilizar dicionários

menu = '''
    [c] Cadastrar Cliente
    [b] Cadastrar Conta bancária
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> '''
# Criar uma série de menus? Cadastro de cliente ou entrar na conta -> conta bancária -> operações dentro da conta // Desvantagem: Infinitos While? (se estivesse usando um sistema de widgets[qt] não seria um problema) Vantagem: Mais fácil para o usuário não ter que se repetir

# aqui vou optar pelo mais simples

saldo_atual = 0
extrato = ""
limite = 500
LIMITE_SAQUES = 3
saques_realizados = 0

clientes = {}

# cliente = {"data_nascimento":, "banco1" :, "banco2" :, ...}
# banco = {"extrato" :, "saldo" :, "saques_utilizados" :}


def criar_cliente(nome: str, data_nascimento, clientes: dict):
    clientes[nome] = {}
    clientes[nome]['data_nascimento'] = data_nascimento
    return clientes


def criar_conta_bancaria(banco, saldo_inicial, clientes: dict, nome):
    if nome not in clientes.keys():
        print("Usuário não cadastrado")
        return clientes

    clientes[nome][banco] = {}
    clientes[nome][banco]['saldo'] = float(saldo_inicial)
    clientes[nome][banco]['extrato'] = '[' + dt.datetime.now().strftime(
        "%d/%m/%Y - %H:%M:%S") + ']' + ' Saldo Inicial: R$' + float(saldo_inicial)
    clientes[nome][banco]['saques_utilizados'] = 0

    return clientes


def realizar_deposito(saldo_atual, extrato, deposito):
    saldo_atual += float(deposito)
    extrato += '[' + dt.datetime.now().strftime("%d/%m/%Y - %H:%M:%S") + \
        "] Depósito: +R$" + str("%.2f" % float(deposito)) + '\n'
    return saldo_atual, extrato


def realizar_saque(saldo_atual, extrato, saque: float, saques_realizados):
    if (saldo_atual < float(saque)):
        print('Você não tem saldo o suficiente para realizar essa operação.')
        return saldo_atual, extrato, saques_realizados

    if (float(saque) > limite):
        print('Esse saque excede o seu limite')
        return saldo_atual, extrato, saques_realizados

    saldo_atual -= float(saque)
    extrato += '[' + dt.datetime.now().strftime("%d/%m/%Y - %H:%M:%S") + \
        "] Saque: -R$" + str("%.2f" % float(saque)) + '\n'
    saques_realizados += 1
    return saldo_atual, extrato, saques_realizados


while True:
    i = input(menu)

    if (i == 'd'):
        print(clientes)
        nome = input('Nome da conta: ')
        if (nome not in clientes.keys()):
            print('Usuário não identificado')
            continue

        banco = input('Banco utilizado: ')
        if (banco not in clientes[nome].keys()):
            print('Banco não identificado')
            continue

        deposito = input("Quanto gostaria de depositar? ")
        clientes[nome][banco]['saldo'], clientes[nome][banco]['extrato'] = realizar_deposito(
            saldo_atual=clientes[nome][banco]['saldo'], extrato=clientes[nome][banco]['extrato'], deposito=deposito)

    elif (i == "s"):
        nome = input('Nome da conta: ')
        if (nome not in clientes.keys()):
            print('Usuário não identificado')
            continue

        banco = input('Banco utilizado: ')
        if (banco not in clientes[nome].keys()):
            print('Banco não identificado')
            continue

        # em todos esses casos, da pra implementar um verificador de float, mas cansou
        if (clientes[nome][banco]['saques_utilizados'] < LIMITE_SAQUES):
            saque = input('Quanto deseja sacar? ')
            clientes[nome][banco]['saldo'], clientes[nome][banco]['extrato'], clientes[nome][banco]['saques_utilizados'] = realizar_saque(
                clientes[nome][banco]['saldo'], clientes[nome][banco]['extrato'], saque, clientes[nome][banco]['saques_utilizados'])
        else:
            print("Você já atingiu o limite de saques de hoje")

    elif (i == 'e'):
        nome = input('Nome da conta: ')
        if (nome not in clientes.keys()):
            print('Usuário não identificado')
            continue

        banco = input('Banco utilizado: ')
        if (banco not in clientes[nome].keys()):
            print('Banco não identificado')
            continue

        print(clientes[nome][banco]['extrato'])
        print('Saldo Atual: R$' + str("%.2f" %
              clientes[nome][banco]['saldo']))

    elif (i == 'b'):
        nome = input('Usuário da conta: ')
        banco = input('Nome do banco: ')
        saldo_inicial = input('Saldo inicial: ')
        clientes = criar_conta_bancaria(banco, saldo_inicial, clientes, nome)

    elif (i == 'c'):
        nome = input('Nome do cliente: ')
        data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
        clientes = criar_cliente(nome, data_nascimento, clientes)
        print(clientes.keys())

    else:
        print('Essa opção não se encontra disponível')
