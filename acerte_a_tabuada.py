from random import randint
bordas = '\033[037m-=-\033[m' * 10
continuar = 'S'
cont = 0
cont_acertos = 0
cont_erros = 0
print(bordas)
print('{:^30}'.format('ACERTE A TABUADA'))
print(bordas)
print()
while continuar == 'S':
    aleatorio1 = randint(1, 10)
    aleatorio2 = randint(1, 10)
    cont += 1
    print(f'{cont}º questão:')
    resultado = int(input(f'{aleatorio1} x {aleatorio2} = '))
    if aleatorio1 * aleatorio2 == resultado:
        print('Parabéns, você acertou! \033[033m✨\033[m')
        cont_acertos += 1
    else:
        print('Você precisa estudar mais!')
        cont_erros += 1
    print()
    continuar = input('Deseja continuar? [S/N] ')[0].strip().upper()
    while continuar not in 'NS':
        continuar = input('Erro! Digite S ou N')[0].strip().upper()
print(f'\n{bordas}{bordas}')
print(f'       \033[033m✨\033[m Fim do jogo! Você acertou {cont_acertos} e errou {cont_erros}! \033[033m✨\033[m')
