"""
Introduçao ao try / except
try -> tentar executar um codigo
except -> ocorreu algum erro ao tentar executar 
"""

n_str = input('Vou dobrar o numero que vc digitar: ')

try:
    print('STR:', n_str) 
    n_float = float(n_str)
    print('FLOAT:', n_float)
    print('O dobro de {} é {:.2f}'.format(n_str, n_float * 2))
except:
    print('Isso nao é um numero!')

# if n_str.isdigit():
#     n_float = float(n_str)
#     print('O dobro de {} é {:.2f}'.format(n_str, n_float * 2))
# else:
#     print('Isso nao é um numero!')