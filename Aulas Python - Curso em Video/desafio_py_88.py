
# Desafio 88 py

dados_aluno = []
while True:
    nome = input('Informe o nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    dados_aluno.append([nome, [nota1, nota2], [media]])
    op = input('Deseja cadastrar mais alunos [S][N]? ')
    if op.lower() == 's':
        continue
    else:
        break

# Média de Todos os Alunos
print('=-=-'*10)
print('Nº   NOME    MÉDIA')
print('---'*15)
for key, da in enumerate(dados_aluno):
    print(f'{key}', end='   ')
    print(f'{da[0].title()}', end='     ')
    print(f'{da[2][0]}', end='\n')

# Usuário ver a nota de cada aluno individualmente
print('---'*15)
while(True):
    aluno = int(input('Mostrar notas de qual aluno: ((999) para interromper) '))
    if aluno == 999:
        break
    else:
        try:
            print(f'Notas de {dados_aluno[aluno][0].title()} são {dados_aluno[aluno][1]}')
            continue
        except IndexError:
            print('Aluno não existe!')