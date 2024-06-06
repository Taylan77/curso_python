# Operadores IN e NOT IN
# Strings são iteráveis
#  0 1 2 3 4 5 
#  T A Y L A N
# -6-5-4-3-2-1

# nome = 'Taylan'
# print(nome[2])
# print(nome[-4])
# print('Tay' in nome)
# print('sla' in nome)
# print(10 * '-')
# print('Tay' not in nome)
# print('sla' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Oque deseja encontrar? ')

if encontrar in nome:
    print('{} esta em {}'.format(encontrar, nome))
else:
    print('{} nao esta em {}'.format(encontrar, nome))