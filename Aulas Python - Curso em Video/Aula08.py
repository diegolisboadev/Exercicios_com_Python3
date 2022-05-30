
# Funções em Python (def)

def mostraLinha(tam):
    print('--'*tam)


#mostraLinha(100)

# Empacotadores Python *args e **kwargs

def contador(*num):
    print(num)

contador([1,2,4,5,9], [2,4,5, 'filha'], {'a': 1, 'b': 'guvia'})

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)