#For Pythonico com break

impostos = ['MEI', 'Simples']

for imposto in impostos:
    if imposto.startswith('M'):
        break
    print(imposto)
