
# ====DESAFIO PYTHON 71 CV ====

# 0 a 20 por extenso - com Extras de sempre perguntar se o usuário deseja informar outro número
from time import sleep

tupla_vinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
                'Dezenove', 'Vinte')
    
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input("Tente novamente! Informe um número entre 0 e 20: "))
    print(f'Você digitou o número {tupla_vinte[num]}')
    op = input('Você deseja continuar? [S]/[N] ').upper()
    if op != 'S' or op == 'N':
        print('Encerrando...')
        sleep(3)
        break