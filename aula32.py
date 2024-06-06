#                       E X E R C I C I O S 

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# try:
#     n1 = int(input('Digite um numero: '))
#     if n1 % 2 == 0:
#         print('O numero {} é par' .format(n1))
#     else:
#         print('O numero {} é impar' .format(n1))
# except:
#     print('O numero que voce digitou NÃO é um numero INTEIRO!!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# try:
#     hora = int(input('Que horas sao agora? '))
#     if hora >= 0 and hora <= 11:
#         print('Bom dia!!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Hora invalida')
# except:
#     print('Voce precisa digitar um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
nome_letras = len(nome)
print(nome_letras)

if nome_letras > 1:
    if nome_letras <= 4:
        print('Seu nome é curto')
    elif nome_letras == 5 or nome_letras == 6:
        print('Seu nome é normal')
    elif nome_letras > 6:
        print('Seu nome é muito grande')
else: 
    print('Digite mais de uma letra!')  