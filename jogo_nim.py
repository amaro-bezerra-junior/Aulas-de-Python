tipo_jogo = 0

def computador_escolhe_jogada(n, m):
    computador_remove = 1

    while computador_remove != m:
        if (n - computador_remove) % (m+1) == 0:
            return computador_remove

        else:
            computador_remove += 1

    return computador_remove


def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        jogador_remove = int(input('Quantas peças você vai tirar? '))
        if jogador_remove > m or jogador_remove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogada_valida = True

    return jogador_remove


def campeonato():
    nRodada = 1
    while nRodada <= 3:
        print()
        print('**** Rodada', nRodada, '****')
        print()
        partida()
        nRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computador_remove = computador_escolhe_jogada(n, m)
            n = n - computador_remove
            if computador_remove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computador_remove, 'peças')

            vezDoPC = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove
            if jogador_remove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogador_remove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

while tipo_jogo == 0:
    print("Bem-vindo ao jogo NIM! Escolha")
    print(" ")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    tipo_jogo = int(input("Sua opção: "))
    print(" ")
    if tipo_jogo == 1:
        print("Você escolheu partida isolada!")
        partida()
        break
    else:
        print("Opção invalida!")
        tipo_jogo = 0