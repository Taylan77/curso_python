"""
Flag (bandeira) - Marcar um local
None = Nao valor
is e is not = é ou nao é (tipo, valor, identidade)
id = identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faça algo')

if passou_no_if is None:
    print('Nao passou no if')

if passou_no_if is not None:
    print('Passou no if')
