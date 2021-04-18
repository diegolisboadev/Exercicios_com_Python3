
# Desafio 87 py
from random import sample
from time import sleep

print('---'*20)
print('JOGO DA MEGA-SENA'.center(50))
print('---'*20)

jogo_quant = int(input('Quantos jogos você quer que eu sorteie? '))

print('---'*20)
print(f'--- SORTEANDO {jogo_quant} JOGOS ---'.center(50))
print('---'*20)

jogos = []
for k, j in enumerate(range(1, (jogo_quant+1))):
    jogo = sample(range(1, 60), 6)
    sleep(1)
    print(f'Jogo {j}: {sorted(jogo)}')
    if jogo not in jogos:
        jogos.append(sorted(jogo))
print('---------- BOA SORTE ----------')

#print('\nTodos os Jogos Gerados nessa Jogada:')
#print(jogos)