
# Exercicio 90 py

from random import randint
from time import sleep

jogos = {}

print('Valores Sorteados: ')
print('\n')
for key in range(1, 5):
    jogador = key
    jogo = randint(0,6)
    print(f'O jogador{key} tirou {jogo}')
    jogos[f'jogador{key}'] = jogo
    sleep(3)

print('Ranking do Jogadores: ')
print('\n')
sorted_jogos = dict(sorted(jogos.items(), key = lambda x:x[1]))
for k, value in enumerate(sorted_jogos, 1):
    print(f'{k}º lugar: {value} com {sorted_jogos[value]}')
