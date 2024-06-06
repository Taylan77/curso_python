"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor da memória (mutavel)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)