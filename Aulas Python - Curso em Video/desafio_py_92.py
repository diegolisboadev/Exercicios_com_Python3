
# Exercicio 92 py

part = []
dict_jogador = {}
soma = 0

nome_jogador = input('Nome Jogador: ')
partidas_jogadas = int(input(f'Quantas partidas {nome_jogador} jogou? '))

for partidas in range(partidas_jogadas):
    part.append(int(input(f'Quantos gols na partida {partidas}? ')))

# Insere no Dicionário
dict_jogador.update({'nome_jogador': nome_jogador.capitalize(), 'gols': part, 'total': sum(part)})

#
print('-=-='*20)
print(dict_jogador)
print('-=-='*20)

for (key, value) in dict_jogador.items():
    print(f'O campo {key} tem o valor {value}.')

print('-=-='*20)

print(f"O jogador {nome_jogador} jogou {partidas_jogadas} partidas")
for k, p in enumerate(part):
    print(f'Na partida {k}, fez {p} gols.')
print(f'Foi um total de {sum(part)} gols.')