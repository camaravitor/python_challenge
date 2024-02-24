#OLD STYLE
nome = "Vitor"
idade = 29
profissao = "Programador"
linguagem = "Python"
#
#print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))  #"%d" é utilizado para valores inteiro e "%s" para valores de ponto flutuante.
#
##MÉTODO FORMAT
#print("Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
#print("Olá, me chamo {0}. Tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))
#print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
#print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

#F-STRING
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:3.4f}")






