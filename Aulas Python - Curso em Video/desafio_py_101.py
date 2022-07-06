
# Exercicio

def fatorial(num = 1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print('--------------------------')
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} x' if c != 1 else f'{c} =', end=' ')
    return f

print(fatorial(5))

