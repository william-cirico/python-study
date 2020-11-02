"""
Dicionários
Obs.: Em algumas linguagens, os dicionários são conhecidos como mapas

- Dicionários são coleções do tipo chave/valor
- Dicionários são representados por chaves

Obs.:
    - Chave e valor são separados por dois pontos (:);
    - Chave e valor podem ser de qualquer tipo de dado;
    - É possível misturar tipos de dados.
"""
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos:

# 1) Acessando via chave
print(paises['br'])
print(paises['py'])

# KeyError se a chave não existir

# 2) Acessando via get (recomendado)

print(paises.get('br'))
print(paises.get('ru'))  # Retorna None

pais = paises.get('ru')
if pais:
    print('Encontrei o país')
else:
    print('Não encontrei o país')

pais = paises.get('ru', 'Não encontrado')
print(f'País: {pais}')

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado
localidades = {
    (35.6895, 396917): 'Escritório em Tókio',
    (35.6895, 396237): 'Escritório em Berlim',
    (35.6439, 316917): 'Escritório em Paris'
}
print(localidades)

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 (Mais comum)
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}

receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# * Em dicionários não podem haver chaves repetidas

# Remover dados de um dicionário

# Forma 1 (Mais comum)
receita.pop('mar')
# Obs.: Sempre informar a chave

# Forma 2
del receita['fev']
print(receita)
# Obs.: Neste caso o valor removido não é retornado

"""
Exemplo de Uso:

Carrinho de Compras
    Produto 1
        - nome;
        - quantidade;
        - preço,
    Produto 2
        - nome;
        - quantidade;
        - preço
"""

carrinho = []
produto1 = ['Playstation 4', 1, 230.00]
produto2 = ['God of War', 1, 250.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teriamos que saber qual é o índice de cada informação no produto.

produto1 = ('Playstation 4', 1, 230.00)
produto2 = ('God of War', 1, 250.00)

carrinho = (produto1, produto2)
print(carrinho)

# Utilizando Dicionário
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto1 = {'nome': 'God of Ward', 'quantidade': 1, 'preco': 250.00}


# Métodos do dicionário

d = dict(a=1, b=2, c=3)
print(d)
d.clear()  # Limpar dicionário

# Copiando dicionário

# Forma 1 (Deep Copy)
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 (Shallow Copy)
novo = d
print(novo)
novo['e'] = 5
print(d)
print(novo)

# Forma não usual de criação de dicionário
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
# O método fromkeys recebe dois parâmetros: Um iterável em um valor.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)






