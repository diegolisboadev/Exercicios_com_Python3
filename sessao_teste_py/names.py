
from sessao_teste_py.names_function import get_formated_name

print("(q) para sair do programa")

while True:
    first = input("Por favor informe seu primeiro nome: ")
    if first == 'q':
        break
    last = input("Por favor informe seu último nome: ")
    if last == 'q':
        break

    formated_name = get_formated_name(first, last)
    print("Nome formatado ficou: {}".format(formated_name))