#Operadores de identidade

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

#Operador para identificar se ambos ocupam a mesma região de memória