#====DESAFIO PYTHON 5 CV ====

#Imprimindo os dados de determinada variavel

valor = input('Digite algo? ')

print('O tipo primitivo é {}'.format(type(valor)))

print('Só tem espaços? {}'.format(valor.isspace()))

print('Só tem números? {}'.format(valor.isnumeric()))

print('É alfabético? {}'.format(valor.isalpha()))

print('É alfanúmerico? {}'.format(valor.isalnum()))

print('É maiúscula? {}'.format(valor.isupper()))

print('É minúscula? {}'.format(valor.islower()))

print('Está capitalizada? {}'.format(valor.capitalize()))