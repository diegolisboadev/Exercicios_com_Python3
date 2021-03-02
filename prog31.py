
#PARAMETROS POSICIONAIS(*, LISTAS) E NOMEADOS ARBITRÁRIOS (**, DICIONÁRIO)

#Atividade 1

def pedidos_sanduiches(*pedidos):
    for p in pedidos:
        print("Pedido do Sanduiche  de {} foi anotado com sucesso!".format(p))

#chamadas
pedidos_sanduiches('carne', 'frando', 'pimenta', 'limão')
print("="*30)
pedidos_sanduiches('peixe', 'sardinha')
print("="*30)
pedidos_sanduiches('mariscos')

print('='*30)

#Atividade 2
def build_profile(nome, sobrenome, **user_info):
    profile = {}
    profile['nome'] = nome
    profile['sobrenome'] = sobrenome

    for key, value in user_info.items():
        profile[key] = value

    return profile

#chamada da função

profile = build_profile("diego", 'pires', end="rua união", idade=25)

print(profile)

print("="*30)

#Atividade 3

def info_carro(nome_fab, modelo, **more_dados):
    info_carro = {}
    info_carro['nome_fab'] = nome_fab
    info_carro['modelo'] = modelo

    for key, value in more_dados.items():
        info_carro[key] = value

    return info_carro

#chamada
carro = info_carro('prisma', '20a9', color='green', tow_package=True)

print(carro)


