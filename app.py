palavra = str(input('Escreva uma palavra: '))
print(f'Sua palavra tem {len(palavra)} caracteres.')
decisao = str(input('Voce deseja continuar [S/N] ? '))
while decisao == 'S':
    palavra = str(input('Escreva uma palavra: '))
    print(f'Sua palavra tem {len(palavra)} caracteres.')
    decisao = str(input('Voce deseja continuar [S/N] ? '))
