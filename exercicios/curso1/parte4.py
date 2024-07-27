import math
# EXERCÍCIO 1
informacoes_pessoais = {
    'pessoa1': {'nome': 'Marcelo Duarte de Aguiar', 'idade': 18, 'cidade': 'Porto Alegre', 'cpf': 12312312312}
}
# EXERCÍCIO 2
# -
informacoes_pessoais['pessoa1']['idade'] = 19
# -
informacoes_pessoais['pessoa1']['profissao'] = 'estudante'
# -
informacoes_pessoais['pessoa1'].pop('cpf')

# EXERCÍCIO 3
quadrados_ate_cinco = {}
for numero in range(1, 6):
    quadrados_ate_cinco[f'quadrado_de_{numero}'] = math.pow(numero, 2)
print(quadrados_ate_cinco)

# EXERCÍCIO 4
chave = 'quadrado_de_5'
print('existe' if chave in quadrados_ate_cinco else 'não existe')

# EXERCÍCIO 5
contador_de_palavras = {}
frase = 'um dois dois tres tres tres quatro quatro quatro quatro cinco cinco cinco cinco cinco'
palavras_da_frase = frase.split(' ')
for palavra in palavras_da_frase:
    if palavra in contador_de_palavras:
        contador_de_palavras[f'{palavra}'] += 1
    else:
        contador_de_palavras[f'{palavra}'] = 1

print(contador_de_palavras)