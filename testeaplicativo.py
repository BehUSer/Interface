did = ''

print(f"{'~~~~~~~~ I N F O R M E  D A D O S ~~~~~~~~':^65}")

print('\n')

userV = str(input('Digite nome do usuario: '))

while did != 'N':
    print('\n')
    timeV = int(input('Digite o tempo [em segundos] de espera no app: '))
    print('\n')
    if (timeV > 0) and (timeV < 4):
        print(f'>> {userV} NORMAL! <<')
        print('\n')
    elif (timeV >= 4) and (timeV <= 6):
        print(f'>> {userV} LONGA! <<')
        print('\n')
    elif (timeV > 6):
        print(f'>> {userV} EXCESSIVA!! <<')
        print('\n')
    else:
        print("Tempo inválido! Por favor, insira um tempo válido.")
        continue
    did = str(input("Deseja inserir mais dados? [S/N]: ")).upper()
    while did not in ('S', 'N'):
        print("Resposta inválida! Por favor, insira 'S' para sim ou 'N' para não.")
        did = str(input("Deseja inserir mais dados? [S/N]: ")).upper()
    print('\n')

print(f"{'~~~~~~~~ O B R I G A D O ~~~~~~~~':^65}")
