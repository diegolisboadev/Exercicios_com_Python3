
# Exercicio 95 py
# TODO

def maior(*inteiros):
    print(f'Foram informados {len(inteiros)} ao todo.')
    return max(inteiros)

print(maior(2,9,4,5,7,1))
print(maior(4,7,0))
print(maior(1,2))
print(maior(6))
print(maior(None))
