
# ====DESAFIO PYTHON 72 CV ====

# tupla brasileirão 2020 exercicio

tabela_brasileiro = ('Atletico Paranaense', 'Atlético Goianiense', 'Atlético Mineiro', 'Bahia',
                    'Botafogo', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo', 'Fluminense',
                    'Fortaleza', 'Goiás', 'Grémio', 'Internacional', 'Palmeiras', 'Red Bull Bragantino',
                    'Santos', 'São Paulo', 'Sport', 'Vasco da Gama')

print('**'*50)
# Tabela times e posições # enumarate(iterator, inicio da lista) # contador iniciar em 1
for pos, time in enumerate(tabela_brasileiro, 1):
    print(pos, ' - ', time)

print('**'*50)
# Mostra os 5 primeiros colocados
print(f'Os 5 primeiros colocados são: {tabela_brasileiro[:5]}')

print('**'*50)
# Os últimos 4 colocados da tabela
print(f'Os últimos 4 colocados da tabela são {tabela_brasileiro[-4:]}')

print('**'*50)
# Times em ordem alfabética
print(f'Os times em ordem alfabética {sorted(tabela_brasileiro)}')

print('**'*50)
# Posição do time do Grêmio na Tabela
print(f'O time do Grêmio está na {tabela_brasileiro.index("Grémio") + 1}ª posição.')