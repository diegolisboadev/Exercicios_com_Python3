
# Exercicio 94 py

part = []
lista_jogadores = []
dict_jogador = {}
soma = 0

while True:
    nome_jogador = input('Nome Jogador: ')
    partidas_jogadas = int(input(f'Quantas partidas {nome_jogador} jogou? '))

    for partidas in range(partidas_jogadas):
        part.append(int(input(f'Quantos gols na partida {(partidas + 1)}? ')))

    # Insere na Lista Lista Jogadores e Limpar as Listas
    jogador = {'nome_jogador': nome_jogador.capitalize(), 'gols': part.copy(), 'total': sum(part)} 
    lista_jogadores.append(jogador.copy())
    jogador.clear()
    part.clear()

    opcao = input('Quer continuar? [S/N]').lower()
    if opcao not in 'sn': 
        print('Erro! Informe S ou N.')
    elif opcao in 'n':
        break

# 2º Parte
print('Code   Nome   Gols   Total')
print('----'*10)
for key, jogadores in enumerate(lista_jogadores):
    print(f'{key}   {jogadores["nome_jogador"]}     {jogadores["gols"]}     {jogadores["total"]}')

print('----'*10)

while True:
    escolha_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if escolha_jogador == 999: break

    if escolha_jogador > len(lista_jogadores): 
        print(f'Erro! Jogador {escolha_jogador} não existe!')
    else:
        print(f"LEVANTAMENTO DO JOGADOR {lista_jogadores[escolha_jogador]['nome_jogador']}")
        for k, p in enumerate(lista_jogadores[escolha_jogador]['gols']):
            print(f'Na partida {k}, fez {p} gols.')