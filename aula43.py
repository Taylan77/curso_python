""" ESTRUTURA DE REPETICAO COM O (FOR)"""

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')