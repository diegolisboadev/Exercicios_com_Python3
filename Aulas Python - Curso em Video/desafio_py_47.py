
#====DESAFIO PYTHON 47 CV ====

#A soma dos números impares multiplos de 3 entre 1 e 500

soma = []

for n in range(1,500, 2):
    #if n % 2 == 1 and n % 3 == 0:
    if n % 3 == 0:
        soma.append(n)

adicao = sum(soma)
print('A soma entre os {} valores é: {}'.format(len(soma), adicao))