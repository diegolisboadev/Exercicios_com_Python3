
#====DESAFIO PYTHON 58 CV ====

#ler dois valores e mostrar um menu para o usuário, perguntando se ele ainda
#vai realizar contas ou não se não sair do programa

opcao = None

num1 = int(input("Digite um Número: "))
num2 = int(input("Digite outro número: "))

while opcao != 5:

    print("Escolha umas das Opções abaixo.")
    opcao = int(input("[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior Número\n"
        "[4] Novos Números\n"
        "[5] Sair do Programa\n"
              "Digite uma opção: "))

    if opcao == 1:
        soma = num1 + num2
        #Saída Soma
        print("Os valores informados foram {} e {} e o Resultado da soma é {}".format(num1, num2, soma))
    elif opcao == 2:
        multi = num1 * num2
        #Saída Multiplicação
        print("Os valores informados foram {} e {} e o Resultado da multiplicação é {}".format(num1, num2, multi))
    elif opcao == 3:
        #Saída Maior Valor
        if num1 > num2:
            resultado = num1
            print("O Maior número é {}".format(resultado))
        else:
            resultado = num2
            print("O Maior número é {}".format(resultado))
    elif opcao == 4:
        num1 = int(input("Digite um Número: "))
        num2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print("Obrigado Por Utilizar!!!")
        exit(-1)


