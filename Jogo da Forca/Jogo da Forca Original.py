from lib.temas import *
from lib.leia import *
from lib.menu import *
from lib.arquivo import *
from random import randint
from time import sleep
arq = 'cadastrojogodaforca.txt'
te = 'arquivotemporario.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    # Menu inicial
    cabecalho('JOGO DA FORCA LOGIN')
    resp = menu(['LOGIN', 'CADASTRAR', 'SAIR'])
    if resp == 1:
        # Menu de login
        cabecalho('LOGIN')
        n = str(input('Nome: '))
        s = str(input('Senha: '))
        if login(te, arq, n, s):
            # Menu do jogo
            cabecalho('JOGO DA FORCA')
            print(f'BEM VINDO {n}, seu login foi feito com sucesso!\n')
            while True:
                while True:
                    opc = menu(['JOGAR', 'VOLTAR'])
                    if opc == 1 or opc == 2:
                        break
                    else:
                        print('\033[31mERRO! Digite uma opção Válida!\033[m')
                if opc == 2:
                    break
                while True:
                    # Escolhendo um tema para o jogo
                    ran1 = randint(0, 1)
                    tema1 = paises if ran1 == 0 else frutas
                    tema2 = 'País' if ran1 == 0 else 'Fruta'
                    # Escolhendo um item do tema
                    ran2 = randint(0, len(tema1) - 1)
                    item = tema1[ran2]
                    # Lista com acertos e erros do jogador
                    vidas = 6
                    acertos = []
                    erros = []
                    # Iniciando o Jogo
                    cabecalho('JOGO DA FORCA')
                    print(f'>>> DICA! É um(a) {tema2} com {len(item)} letras <<<')
                    while True:
                        chave = ''
                        print('\n ____\n/   |   ')
                        print('|   O' if len(erros) >= 1 else '|')
                        lin1 = ''
                        if len(erros) == 2:
                            lin1 = '   |   '
                        elif len(erros) == 3:
                            lin1 = '  /|   '
                        elif len(erros) >= 4:
                            lin1 = '  /|\  '
                        print(f'|{lin1}')
                        lin2 = ''
                        if len(erros) == 5:
                            lin2 = '  /    '
                        elif len(erros) == 6:
                            lin2 = '  / \  '
                        print(f'|{lin2}')
                        print('|\n=========')
                        if len(erros) == 6:
                            print(f'ENFORCADO! Mais sorte na próxima {n}')
                            print(f'Vidas: {vidas}')
                            print('Erros: ', end='')
                            for e in erros:
                                print(f'{e}', end=' ')
                            print(f'\nO nome do(a) {tema2} era {item}')
                            print('GAME OVER')
                            break
                        print(f'Vidas: {vidas}')
                        print('Erros: ', end='')
                        for e in erros:
                            print(f'{e}', end=' ')
                        for c in item:
                            chave += c if c in acertos else '-'
                        print(f'\n{tema2}: {chave}')
                        if item == chave:
                            print(f'\nPARABÉNS {n}, você acertou!')
                            break
                        jogador = leiastr('Digite uma letra: ')
                        if jogador in item:
                            if jogador not in acertos:
                                acertos.append(jogador)
                            else:
                                print(f'{n} Você já digitou essa letra!')
                        else:
                            if jogador not in erros:
                                erros.append(jogador)
                                if len(erros) >= 1:
                                    vidas -= 1
                            else:
                                print(f'{n} Você já digitou essa letra!')
                    while True:
                        resp = leiastr(f'Quer Jogar Novamente {n}? [S/N]')
                        if resp in 'SN':
                            break
                    if resp == 'N':
                        break
        else:
            print('Usuário ou Senha inválido!')
    elif resp == 2:
        # Menu de novo cadastro
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        senha = leiaint('Senha: ')
        cadastrar(arq, nome, senha)
    elif resp == 3:
        break
    else:
        print('\033[31mERRO! Digite uma opção Válida!\033[m')
cabecalho('Finalizando...')
sleep(2)
print('Volte Sempre!')
