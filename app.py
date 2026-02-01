def contadorDeCaracter ():
    while True:
        palavra = str(input('Escreva uma palavra: '))
        print(f'Sua palavra tem {len(palavra)} caracteres.')
        decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip()
        if decisao == 'S':
            continue
        elif decisao != 'S' and decisao != 'N':
            decisao = str(input('Voce deseja continuar [S/N] ? ')) .upper() .strip()
            if decisao == 'S':
                continue
            else:
                break
        else:
            break
    return 'Fim do programa'
resutaldo = contadorDeCaracter()
print(resutaldo)