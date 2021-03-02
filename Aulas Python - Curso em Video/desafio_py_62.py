
#====DESAFIO PYTHON 62 CV ====

#Ler um número e mostra a sequencia de Fibonacci os fibo termos
#CURSO EM VIDEO

fibo = int(input("Informe um número: "))

termo1 = 0
termo2 = 1
cont = 3

'''while cont <= fibo:
    termo3 = (termo1 + termo2)
    print("{}".format(termo3), end=" -> ")
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("FIM")'''

print("{} -> {}".format(termo1, termo2), end="")

while cont <= fibo:
    termo3 = (termo1 + termo2)
    print(" -> {}".format(termo3), end="")
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(" -> FIM")