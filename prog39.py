
#ATIVIDADE 1
'''with open('text_files/guest.txt', 'r+') as file:
    nome = input("Informe seu Nome: ").strip()
    file.write(nome + "\n")
    arqui = file.readlines()

for r in arqui:
    print("Nome: {}".format(arqui))'''

#ATIVIDADE 2

import os.path

'''ativo = True

while ativo:
    nome = input("Informe seu Nome: ").strip()
    saudacao = "Sem bem vindo(a) " + nome
    print(saudacao)

    #Gravando no ARQUIVO
    path = 'text_files/guest_book.txt'

    #Verificar se o path file existe
    if os.path.exists(path):
        mod = 'a'
    else:
        mod = 'w'

    with open(path, mod) as file:
        file.write(nome + '\n')
        file.write(saudacao + '\n')

    sair = input("Deseja sair? [s/n]")
    if(sair.lower() == 's'):
        ativo = False
    elif sair.lower() == 'n':
        ativo = True
    else:
        print('Ops! Valor Inválido.')'''

#ATIVIDADE 2

conta = 0

while True:

    quest = input("Porque você gosta de Programação? ").strip()
    conta += 1

    #Gravando no arquivo
    path = 'text_files/respostas.txt'

    with open(path, 'a') as file:
        file.write('{} - {} \n'.format(conta, quest))
        #file.write('{}'.format())


    if conta > 5:
        verifica = input("Deseja continuar ou finalizar [S/N]").upper()
        if(verifica == 'N'):
            exit(-1)





