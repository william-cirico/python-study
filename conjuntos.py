"""
Conjuntos

- Conjuntos em qualquer linguagem de programção se refere à Teoria
dos Conjuntos da Matemática

- Em Python, os conjuntos são chamados de Sets.

* Sets não possuem valores duplicados;
* Sets não possuem valores ordenados;
* Elementos não são acessados via índice;

Conjuntos são utilizados quando precisamos armazenar elementos mas
não nos importamos com a ordenação deles.

Os conjuntos são referenciados em Python com chaves {}

- Diferença entre Conjuntos (sets) e mapas em Python:
    * Um dicionário tem chave/valor;
    * Um conjunto tem apenas valor;
"""

# Definindo um conjunto:

# Forma 1
S = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(S)

# Obs.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erro

# Forma 2 (Mais comum)
s = {1, 2, 3, 4, 5, 5}

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista}')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla: {tupla}')

# Dicionários não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario}')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Usos interessantes com sets
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo']
print(cidades)
print(len(cidades))

# Quantas cidades distintas temos?
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
print(s)

# Remover elementos em um conjunto

# Forma 1
s.remove(3)  # Valor a ser removido
# Obs.: Caso o valor não seja encontrado será gerado KeyError

# Forma 2
s.discard(2)  # Não gera erro

# Copiando um conjunto para outro...

# Forma 1 (Deep Copy)
novo = s.copy()

novo.add(4)

print(s)
print(novo)

# Forma 2 (Shallow Copy)
novo = s
novo.add(5)

print(s)
print(novo)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos do Set

# Imagine que temos 2 conjuntos: Um contendo estudantes do curso
# Python e um do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro'}
estudantes_java = {'Fernando', 'Gustavo', 'Patricia'}

# Existem alunos que cursaram os dois cursos

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# Forma 2 - Utilizando o caractere | (pipe)
unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, Valor Máximo, Valor Mínimo e tamanho
s = {1, 2, 3, 4, 5, 6}
print((sum(s)))
print((max(s)))
print((min(s)))
print((len(s)))




