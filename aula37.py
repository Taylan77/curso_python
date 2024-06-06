"""
Repetiçoes
while (enquanto)
Executa uma açao enquanto uma condiçao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('O numero 6 esta sendo PULADO!')
        continue

    if contador >= 10 and contador <= 30:
        continue

    print(contador)
    
    if contador == 40:
        break

print("Acabou!")