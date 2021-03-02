#====DESAFIO PYTHON 40 CV ====

#Confederação nacional de natação
#Ler o ano de nascimento de atleta e mostra a categoria conforme a idade

from datetime import date

ano_nasc = int(input('Informe seu ano de nascimento: '))

idade = (ano_nasc - date.today().year) * -1

categoria = 0

if idade <= 9:
    categoria = 'MIRIM'

elif idade <= 14:
    categoria = 'INFANTIL'

elif idade <= 19:
    categoria = 'JUNIOR'

elif idade <= 20:
    categoria = 'SÊNIOR'

else:
    categoria = 'MASTER'

print('A sua idade é {} anos, portanto sua categoria é {}'.format(idade, categoria))
