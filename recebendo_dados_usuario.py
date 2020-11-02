"""
Recebendo dados do usuário

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
"""
#Entrada de dados
#print("Qual é o seu nome?")
#nome = input() # Input = Entrada
nome = input('Qual seu nome? ')

#Exemplo de print antigo
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print moderno
#print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print atual
print(f'Seja bem-vindo(a) {nome}')
#print("Qual é a sua idade? ")
#idade = input()
idade = input("Qual é a sua idade? ")

#Processamento

#Saída de dados
#Exemplo de print antigo
#print('%s tem %s anos' % (nome, idade))

#Exemplo de print moderno
#print('{0} tem {1} anos'.format(nome, idade))

#Exemplo de print atual
print(f'{nome} tem {idade} anos')
"""
#int(idade) -> Cast
#Cast é a conversão de um tipo de dado para outro
"""
print(f'{nome} nasceu em {2020 - int(idade)}')

