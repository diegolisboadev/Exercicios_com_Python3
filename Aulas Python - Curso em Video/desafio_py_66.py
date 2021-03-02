# ====DESAFIO PYTHON 66 CV ====

# Tabuada de vários numeros 1 de cada vez
# para valores digitados pelo usuário

while True:

    num = int(input("Qual valor da tabuada você quer ver? "))

    # caso negativo interromper laço
    if num < 0:
        print("Valor negativo não permitido!")
        break

    opcao = input("Informe a Tabuada [ + | - | X | / ]: ").upper().strip()[0]

    print("--"*20)

    #Mostra Tabuada
    for n in range(0,10):
        if opcao == "+":
            calc = num + n
        elif opcao == "-":
            calc = num - n
        elif opcao == "X":
            calc = num * n
        elif opcao == "/":
            if n == 0:
                continue
            calc = num / n
        else:
            print("Tabuada incorreta! Tente Novamente!")
            continue

        print(f"{num} {opcao} {n} = {calc}")

    print("--"*20)



