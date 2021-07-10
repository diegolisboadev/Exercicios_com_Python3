
# Exercicio 91 py
import datetime

ctps = {}
ano_de_contratacao = 0
salario = 0
aposentadoria = 0

nome = input('Nome: ')
ano_de_nascimento = int(input('Ano de Nascimento: '))
carteira_de_trabalho = int(input('Carteira de Trabalho (0 não tem): '))

ctps_dict = {
        'nome': nome.capitalize(), 
        'idade': (datetime.date.today().year - ano_de_nascimento), 
        'ctps': carteira_de_trabalho
    }

if(carteira_de_trabalho != 0):
    ano_de_contratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salário R$: '))
    aposentadoria = (ano_de_contratacao + 35) - ano_de_nascimento

    ctps_dict.update(
        {
            'ano_de_contratacao': ano_de_contratacao, 
            'salario': salario,
            'aposentadoria': aposentadoria
        }
    )

print('-=-='*20)

print(ctps_dict)

for (key, value) in ctps_dict.items():
    print(f'{key} tem o valor {value}')