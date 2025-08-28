menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> '''

saldo_atual = 0
extrato = ""
limite = 500
LIMITE_SAQUES = 3
saques_realizados = 0


def realizar_deposito(saldo_atual, extrato, deposito):
    saldo_atual += float(deposito)
    extrato += "Depósito: +R$" + str("%.2f" % float(deposito)) + '\n'
    return saldo_atual, extrato


def realizar_saque(saldo_atual, extrato, saque: float, saques_realizados):
    if (saldo_atual < float(saque)):
        print('Você não tem saldo o suficiente para realizar essa operação.')
        return saldo_atual, extrato, saques_realizados

    if (float(saque) > limite):
        print('Esse saque excede o seu limite')
        return saldo_atual, extrato, saques_realizados

    saldo_atual -= float(saque)
    extrato += "Saque: -R$" + str("%.2f" % float(saque)) + '\n'
    saques_realizados += 1
    return saldo_atual, extrato, saques_realizados


while True:
    i = input(menu)
    if (i == 'd'):
        deposito = input("Quanto gostaria de depositar? ")
        saldo_atual, extrato = realizar_deposito(
            saldo_atual=saldo_atual, extrato=extrato, deposito=deposito)

    elif (i == "s"):
        # em todos esses casos, da pra implementar um verificador de float, mas cansou
        if (saques_realizados < LIMITE_SAQUES):
            saque = input('Quanto deseja sacar? ')
            saldo_atual, extrato, saques_realizados = realizar_saque(
                saldo_atual, extrato, saque, saques_realizados)
        else:
            print("Você já atingiu o limite de saques de hoje")

    elif (i == 'e'):
        print(extrato)
        print('Saldo Atual: R$' + str("%.2f" % saldo_atual))

    elif (i == 'q'):
        break
