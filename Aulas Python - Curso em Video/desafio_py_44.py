
#====DESAFIO PYTHON 44 CV ====

from random import choice
from time import sleep

print('{:=^40}'.format(' JOKENPÓ '))

print('Escolha entre PEDRA, PAPEL ou TESOURA')

usuario_esc = str(input('Informe a sua escolha: ')).strip().upper()

esc_computador = choice(list(['PEDRA', 'PAPEL', 'TESOURA']))

print('='*50)


print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÓ!!')

resultado = None

if usuario_esc == esc_computador:
    resultado = 'EMPATOU!!'

elif usuario_esc == 'PEDRA' and esc_computador == 'TESOURA' \
        or usuario_esc == 'TESOURA' and esc_computador == 'PAPEL' \
        or usuario_esc == 'PAPEL' and esc_computador == 'PEDRA':
    resultado = 'JOGADOR VENCEU!!'

else:
    resultado = 'COMPUTADOR VENCEU!!'

print('O computador escolheu {} \nVocê escolheu {} \n{}'.format(esc_computador, usuario_esc, resultado))