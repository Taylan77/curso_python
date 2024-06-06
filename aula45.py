"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez 
Next -> me entregue o proximo valor
Iter -> me entregue seu iterador
"""

texto = 'Taylan' # iteravel
# iteratador = iter(texto) # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

# O EXEMPLO ACIMA É A MESMA COISA QUE:

for letra in texto:
    print(letra)