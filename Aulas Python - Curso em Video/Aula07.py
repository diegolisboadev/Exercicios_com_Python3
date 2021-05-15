
# Dicionários
pessoas = {'nome': 'Diego', 'sexo': 'M', 'idade': 26}
print(pessoas)

print(f"O {pessoas['nome']} tem {pessoas['idade']}")

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for i in pessoas.items():
    print(i)

# del pessoas['nome']
# pessoas['peso'] = 98.5
# pessoas.update({'fluxo': 20})

####################################

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

##################################################################

estado = {}
brasil = []

for c in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

print(brasil)