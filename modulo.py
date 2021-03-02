
"""função fazer pizza"""

def make_pizza(size, *toppings):
    print("\n Fazendo a pizza {} com os seguintes sabores.".format(str(size)))
    for top in toppings:
        print("Pedido de Pizza do tipo: {} ".format(top))


"""imprimir nome"""
def imprimir_nome(nome):
    print("Bem Vindo {}".format(nome.title()))