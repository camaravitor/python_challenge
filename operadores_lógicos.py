#Operadores lógicos

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite

saldo >= saque or saque <= limite

#Operador de negação

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not ""


#Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print (exp_3)
