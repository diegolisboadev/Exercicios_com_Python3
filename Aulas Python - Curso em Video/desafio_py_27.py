#====DESAFIO PYTHON 27 CV ====

#Um número entre 0 e 5 e usuário terá que adivinhar o número

from random import randint
from time import sleep

aleatorio = randint(0,5)

num = int(input('Chute o número que o computador escolheu: '))

print('Processando...')
sleep(5) #Função sleep faz o computador ter um delay

if num == aleatorio:
    print('PARABÉNS!! O número escolhido {} é igual à {}'.format(num, aleatorio))

else:
    print('AHH, DESCULPE, VOCÊ PERDEU!! O número é escolhido pelo computador foi {}'.format(aleatorio))


print('Obrigado por jogar!!')