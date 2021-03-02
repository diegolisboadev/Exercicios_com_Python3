
# ====DESAFIO PYTHON 75 CV ==== #

# Descobrir e separar as vogais dessas palavras abaixo

palavras = ('bolo', 'pedra', 'risada', 'folha', 'aprender')

resultado = None
for palavra in palavras:
    resultado = f'Na palavra {str(palavra).upper()} temos'
    for p in palavra:
        if p in 'aeiou':
            resultado += f' {p}'
    print(resultado) # Imprimi o resultado