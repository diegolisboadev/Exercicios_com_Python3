#====DESAFIO PYTHON 26 CV ====

#Verificar o primeiro é o último nome de uma pessoa

nome = str(input('Informe seu nome completo: ')).strip()

print('O primeiro nome de {} é {}'.format(nome, nome.split()[0]))

print('O último nome de {} é {}'.format(nome, nome.split()[-1]))
