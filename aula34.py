"""
Repetiçoes
while (enquanto)
Executa uma açao enquanto uma condiçao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print('O seu nome é {}'.format(nome))

    if nome == 'sair':
        break

print('Acabou!')