"""    CALCULADORA COM WHILE   """


while True:

    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-*/) : ')

    numeros_validos = None
    n1_float = 0
    n2_float = 0
#    !!!!!!! Defina variaveis fora do bloco !!!!!!!!!

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
            print('Um ou ambos numeros sao invalidos!')
            continue #Faz com que o codigo pare nesse local e volte ao começo

    operador_permitidos = '+-*/'
    
    if operador not in operador_permitidos: # Not in = Nao está entre
        print('Operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador!')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '*':
        print(n1_float * n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    else:
        print('NUNCA DEVERIA CHEGAR AQUI!!!!')
    


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


