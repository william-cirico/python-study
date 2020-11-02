# add (adiciona), update (atualiza), clear, discard
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}
lista = [8, 9, 10, 11]
print(s1, s2)
s1.add(6)
print(s1)
s2.update(lista)
print(s2)
s1.clear()
print(s1)
s2.discard(8)
print(s2)
# union | (une)
s1 = s1 | s2
print(s1)
# intersection & (todos os elementos presentes nos dois sets)
s3 = s1 & s2
print(s3)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
s1 = {1, 2, 3, 5}
s2 = {1, 2, 3, 4}
s3 = s1.symmetric_difference(s2)
print(s3)