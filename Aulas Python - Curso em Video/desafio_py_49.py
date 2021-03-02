
#====DESAFIO PYTHON 47 CV ====

#Ler seis números inteiros e mostre a soma somente dos números pares

soma = 0
cont = 0
text = None

for n in range(6):
    num = int(input('Informe um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

if cont > 1:
    text = 'numeros pares'
else:
    text = 'numero par'

print('Foi localizado {} {}, é a soma é: {}'.format(cont, text, soma))
