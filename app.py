def contadorDeCaracter ():
    palavra = str(input('Escreva uma palavra: '))
    print(f'Sua palavra tem {len(palavra)} caracteres.')
    decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip()
    if decisao == 'S':
        while decisao == 'S':
            palavra = str(input('Escreva uma palavra: '))
            print(f'Sua palavra tem {len(palavra)} caracteres.')
            decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip()
    elif decisao != 'S' and decisao != 'N':
        print('elif')
        decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip()
        if decisao == 'S':
            while decisao == 'S':
                palavra = str(input('Escreva uma palavra: '))
                print(f'Sua palavra tem {len(palavra)} caracteres.')
                decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip() 

    return 'Fim do programa'
resutaldo = contadorDeCaracter()
print(resutaldo)