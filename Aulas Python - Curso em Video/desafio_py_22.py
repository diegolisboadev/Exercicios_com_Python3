
#====DESAFIO PYTHON 22 CV ====

#Digite um número na tela de 0 a 9999 e mostre na tela seus digitos separados
#Erro se não inserir os 4 digitos

#num = input('Insira um número entre 0 e 9999: ')

#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))

#Validação somente para int

num = int(input('Insira um número entre 0 e 9999: '))

if num > 0 and num < 9999:

    print('Unidade: {}'.format((num // 1) % 10))
    print('Dezena: {}'.format((num // 10) % 10))
    print('Centena: {}'.format((num // 100) % 10))
    print('Milhar: {}'.format((num // 1000) % 10))

else:
    print('Erro!! Você inseriu o valor {} não permitido!!'.format(num))