
# Jogo da Velha Python

jogador1 = input('Jogador 1 - Informe seu Nome: ')
jogador2 = input('Jogador 2 - Informe seu Nome: ')

matriz = [[None,None,None], [None,None,None], [None,None,None]]

print("-="*20)
print("Iniciando o Jogo da Velha")
print("-="*20)
for j, m in enumerate(matriz):
    posicao = int(input('Informe uma posição: '))
    matriz[j][posicao] = 'X'

print(matriz)
