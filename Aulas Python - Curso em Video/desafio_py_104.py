
# Exercicio 104

def notas(*notas, sit=False):
    """
        -> Função para analisar a situação de vários alunos
        :param notas: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    media = sum(notas) / len(notas)

    dicio = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'media': media
    }

    if sit:
        situacao = None
        match(media):
            case media if media >= 7:
                situacao = 'BOA'
            case media if media >= 5:
                situacao = 'RAZOAVEL'
            case _:
                situacao = 'RUIM'
        dicio.update({ 'situacao':  situacao })

    return dicio

print('-----------------------------------')
print(notas(5.5, 2.5, 10, 6.5, sit=True))
help(notas)

