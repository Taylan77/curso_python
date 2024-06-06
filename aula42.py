frase = 'Botafogo Campeao'

i = 0
qtd_letras_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual_letras = frase.count(letra_atual)

    if qtd_letras_apareceu_mais_vezes < qtd_atual_letras:
        qtd_letras_apareceu_mais_vezes = qtd_atual_letras
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi "{}" que apareceu {}X'\
    .format(letra_apareceu_mais_vezes, qtd_letras_apareceu_mais_vezes)
    )