#ESTRUTURA FOR INTERÁVEL

#texto = input("Informe um texto: ")
#texto = ""
#VOGAIS = "AEIOU"

#for letra in texto:
#    if letra.upper() in VOGAIS:
#        print(letra, end="")
#else:
#    print("\nExecuta ao final do laço")



#ESTRUTURA FOR - BUILT IN RANGE
#
#for numero in range(0, 11):
#    print(numero, end=" ")
#
#for numero in range(0, 51, 5): #star, finish, step
#    print(numero, end=" ")

#ESTRUTURA WHILE

#opcao = -1
#
#while opcao != 0:
#    opcao = int(input("[1] Sacar \n[2] Extrato\n[0] Sair \n: "))
#
#if opcao == 1:
#    print("Sacando...")
#elif opcao ==2:
#    print("Exibindo o extrato...")
#else:
#    print("Obrigado por usar nosso sistema bancário. Até logo!")
  
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue
    
    print(numero)
    
#for numero in range(100):
#
#
#    if numero == 12:
#       break    #continue: serve para pular o número escolhido
#
#
#    print(numero, end=" ")
