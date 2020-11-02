"""
Módulo Collections - Counter (contador)

Collections -> High-performance Container Datatypes

- Recebe um iteravel como parâmetro e cria um objeto do tipo Collections
Counter que é parecido com um dicionário, contendo como chave o elemento
da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.
"""
from collections import Counter  # Importando a biblioteca

# Utilizando o Counter

# Exemplo 1:

# Podemos utilizar qualquer iterável, aqui foi usado uma lista
lista = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 20, 20, 20, 20, 20]

# Utilizando o Counter
res = Counter(lista)

print(res)

# Exemplo 2:

print(Counter('Geek University'))

# Exemplo 3:

texto = """Buraco negro é uma região do espaço-tempo em que o campo
 gravitacional é tão intenso que nada — nenhuma partícula ou radiação
  eletromagnética como a luz — pode escapar dela. A teoria da relatividade geral prevê que uma 
  massa suficientemente compacta pode deformar o espaço-tempo para formar um buraco negro. O limite da região da qual 
  não é possível escapar é chamado de horizonte de eventos. Embora o horizonte de eventos tenha um efeito enorme sobre 
  o destino e as circunstâncias de um objeto que o atravessa, não tem nenhuma característica local detectável. De muitas 
  maneiras, um buraco negro age como um corpo negro ideal, pois não reflete luz. Além disso, a teoria quântica de campos 
  no espaço-tempo curvo prevê que os horizontes de eventos emitem radiação Hawking, com o mesmo espectro que um corpo 
  negro de temperatura inversamente proporcional à sua massa. Essa temperatura é da ordem dos bilionésimos de um kelvin 
  para buracos negros de massa estelar, o que a torna praticamente impossível de observar."""

palavras = texto.split()

# print(palavras)
res = Counter(palavras)
print(res)
print(res.most_common(5))  # 5 palavras com mais ocorrências


