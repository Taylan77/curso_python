#                 E X E R C I C I O 

# Faça seu nome ter entres a letras o simbolo [*]

nome = 'Taylan'

indice = 0
novo_nome = ''
while indice < len(nome):
    letras = nome[indice]
    novo_nome += f'*{letras}'
    indice += 1


novo_nome += '*'
print(novo_nome)