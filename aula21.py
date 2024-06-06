"""
OPERADORES LOGICOS
and (e) or (ou) not (nao)
and - Todas as condicoes precisa ser verdadeiras.
Se qualquer valor for considerado falso,
a expressao inteira sera avaliada naquele valor.
Sao consideradas falsy (que voce ja viu)
0 0.0 '' False
Tambem existe o tipo None que é usado para representar um não valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Voce entrou')
else:
    print('Voce saiu')




# Avaliação curto circuito

# print(True and False and True)

# print(True and 0 and True)