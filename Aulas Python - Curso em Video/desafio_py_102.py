
# Exercicio 103

def ficha(nome='<desconhecido>', gols=0):
    return nome, gols

print('---------------------------')
n = input('Nome do Jogador: ') or None

try: 
    g = int(input('Gols do Jogador: ')) 
except ValueError:
    g = 0
 
if n == None:
    nome, gols = ficha(gols=g)
else:
    nome, gols = ficha(nome=n, gols=g)

print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')