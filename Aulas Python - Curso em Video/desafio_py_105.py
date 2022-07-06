
# Exercicio 105


def tamMensagens(msg):
    print('~'*len(msg))
    print(msg)
    print('~'*len(msg))

def helper(funcao):
    return help(funcao)

while True:
    tamMensagens('SISTEMA DE AJUDA PyHELP')
    funcao = input('Função ou Biblioteca: ')
    if 'fim' not in funcao.lower():
        tamMensagens(f"Acessando o manual do comando '{funcao}'")
        helper(funcao)
    else:
        break
tamMensagens('ATÉ LOGO!')