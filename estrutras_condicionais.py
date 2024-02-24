##saldo = 2000.0
#saque = float(input("Informe o valor do saque: "))
#
#if saldo >= saque:
#    print("Realizando saque!")
#
#if saldo < saque:
#    print("Saldo insuficiente!")
#
#opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
#
#if opcao == 1:
#    valor = float(input("Informe a quantia para o saque: "))
#
#elif opcao ==2:
#    print("Exibindo o extrato...")
#else:
#    sys.exit("Opção inválida")

#MAIOR_IDADE = 18
#idade_especial = 17
#
#idade = int(input("Informe sua idade: "))
#
#if idade >= MAIOR_IDADE:
#    print("Maior de idade, pode tirar a CNH.")
#
#if idade < MAIOR_IDADE:
#    print("Ainda não pode tirar a CNH.")
#
#
#if idade >= MAIOR_IDADE:
#    print("Maior de idade, pode tirar a CNH.")
#else:
#    print("Ainda não pode tirar a CNH.")
#
#if idade >= MAIOR_IDADE:
#    print("Maior de idade, pode tirar a CNH.")
#elif idade == idade_especial:
#    print("Pode fazer SOMENTE aulas teóricas.")
#else:
#    print("Ainda não pode tirar a CNH.")

#conta_normal = False
#conta_universitaria = False
#
saldo = 2000
saque = 1500
#cheque_especial = 450
#
#if conta_normal:
#    if saldo >= saque:
#        print("Saque realizado com sucesso!")
#    elif saque <= (saldo + cheque_especial):
#        print("Saque realizado com uso do cheque especial!")
#    else:
#        print("Não foi possível realizar o saque. Saldo insuficiente.")
#elif conta_universitaria:
#    if saldo <= saque:
#        print("Saque realizado com sucesso!")
#    else:
#        print("Saldo insuficiente!")
#else:
#    print("Sistema não reconheceu seu tipo de contas. Entre em contato com o gerente.")


# ESTRUTURA CONDICIONAL TERNÁRIA
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")





