
#====DESAFIO PYTHON 61 CV ====

#Ler o primeiro termo e razão e mostra os 10 primeiros valores da PA com WHILE
#E dando opção de escolha para o usuário ver mais valores

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

#FUNÇÃO DA FORMULA P.A.
def formula(primeiro_termo, termos, razao):
    formula = (primeiro_termo + (termos * razao) + razao)
    return formula

form = formula(primeiro_termo, 9, razao)

cont = 0

while primeiro_termo < form:
    print(primeiro_termo, end=" -> ")
    primeiro_termo += razao
    cont += 1

    if(primeiro_termo == form):
            termos = int(input("\nInforme mais termos[0 para sair]: "))
            if(termos != 0):
                form = formula(primeiro_termo, termos, razao)
            else:
                pass


print("Fim!")
print("Foram Listados {} termos da PA".format(cont))
