
#====DESAFIO PYTHON 56 CV ====

#Ler o sexo de uma pessoa, porém só aceitar M ou F

sexo = ''

while sexo.upper() != 'M' and sexo.upper() != 'F':
    sexo = input("Informe seu sexo: ")
print("O seu sexo é {} ".format(sexo))