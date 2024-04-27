menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual é o valor do depósito? "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de {deposito} realizado com sucesso\n"
        else:
            print("Não é possível depositar valores negativos!")

    elif opcao == "s":
        saque = float(input("Qual é o valor do saque? "))

        if saque > saldo:
            print("Não será possível realizar a operação. Saldo insuficiente!")
        elif saque > 0:
            if saque < LIMITE and numero_saques < LIMITE_SAQUES:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque de {saque} realizado com sucesso\n"
            elif saque >= LIMITE:
                print(f"Não é possível realizar saque de valor maior que {LIMITE} por operação!")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Não é possível realizar mais do que {LIMITE_SAQUES} por dia!")

        else:
            print("Não é possível realizar saque de valores negativos!")
        

    elif opcao == "e":
        print(extrato)
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")