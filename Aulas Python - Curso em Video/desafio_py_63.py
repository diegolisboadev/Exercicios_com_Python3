
#====DESAFIO PYTHON 63 CV ====

#Ler varios numeros inteiros, mostrando a soma deles no final desconsiderando
#o flag 999 que é a condição de parada

num = 0
cont = 1
soma = 0

while num != 999:
    num = int(input("{} Informe um número: ".format(cont)))

    if num == 999:
        break
    cont += 1
    soma += num

if num == 999:
    print("Fim! 999 Condição de Parada!")
    #print("Foram digitados {} números e a soma entre eles é {}".format(cont, soma))
    print(f"Foram digitados {cont - 1} números e a soma entre eles é {soma}") # usando (f strings)
    exit(-1)


