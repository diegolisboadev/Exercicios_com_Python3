#====DESAFIO PYTHON 31 CV ====

#Calcular se uma ano é bissexto

from time import sleep
from datetime import date

ano = int(input('Informe o ano ou coloque (0) para analisar o ano atual: '))

print('Verificando se o ano é ou não Bissexto...')
sleep(5)

if ano == 0:
    ano = date.today().year #Pegar o ano atual datado em sua máquina

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('Ano {} é Bissexto!!'.format(ano))
else:
    print('Ano {} não é bissexto!!'.format(ano))

