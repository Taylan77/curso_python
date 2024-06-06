"""
Interpolaçao basica de strings
s - strings
d e i - int
f - float
x e X hexadecimal (ABCDEF0123456789)
"""

nome = 'Taylan'
preço = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preço)
print(variavel)
print('O hexadecimal de %d é %04x' % (200, 200))