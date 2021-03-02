#Dicionário dict -  Python

#Exemplo com {}
entidades = {
    'Instituicao': []
}

#Com dict()
entidades = dict(Instituicao: [])

#Itens adicionados após a criação do Dicionário
entidades = dict()
entidades['Instituicao'] = []

#Removendo elementos do dicionário del()
entidades = dict()
entidades['Empreendimento'] = 'EntidadeEmpreendimento'
print(entidades)
Resultado: {'Empreendimento': 'EntidadeEmpreendimento'}

del entidades['Empreendimento']
print(entidades)

Resultado: {}

#Dicionários das Entidades
entidades = {
    'Instituicao': [
        ('IdInstituicao','bigint',
         'Identificador da instituição-PK'),
        ('IdTipoInstituicao', 'bigint',
         'Id do tipo de instituição'),
        ('NomInstituicao', 'varchar',
         'Nome da instituicao'),
        ('NumCNPJ', 'varchar', 'Número do CNPJ')
        ]
    }

#Removendo a extensão de um arquivo
def extract_entity_name(filename):
	return filename.split('.')

extract_entity_name('Exemplo.exe')
