"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

plv_secreta = 'programaçao'
letra_acertada = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in plv_secreta:
        letra_acertada += letra_digitada
    
    plv_formada = ''
    for letra_secreta in plv_secreta:
        if letra_secreta in letra_acertada:
            plv_formada += letra_secreta
        else:
            plv_formada += '*'
    print('Palavra formada:', plv_formada)

    if plv_formada == plv_secreta:
        os.system('cls')
        print('VOCE GANHOU! PARABÉNS!!')
        print('A palavra era:', plv_secreta)
        print('Tentativas:', tentativas)
        letra_acertada = ''
        tentativas = 0





    

