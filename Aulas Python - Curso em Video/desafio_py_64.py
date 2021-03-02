
#====DESAFIO PYTHON 64 CV ====

#Ler varios numeros inteiros, mostrando a media deles no final e
#o maior e menor valores

num = 0
cont = 0
escolha = None
soma = 0
maior_menor = []

while escolha != 'N':
    num = int(input("{} Informe um número: ".format(cont)))
    cont += 1
    escolha = input("Quer continuar a digitar números? [S][N]").upper()
    soma += num
    maior_menor.append(num)

#Media entre todos os valores
print("A média entre os {} números digitados é {:.2f}".format(cont, (soma / cont)))

#O maior e menor valores
print("O maior valor é {} é o menor valor é {}".format(max(maior_menor), min(maior_menor)))

