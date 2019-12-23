def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
        ler = a.read().split('\n')
    except:
        print('Erro ao ler arquivo!')
    else:
        return ler


def cadastrar(arq, nome='Visitante', senha=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{senha}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {nome} feito com sucesso.')
            a.close()


def login(arq, arq2, nome='Visitante', senha=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{senha}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            a.close()
            a = open(arq, 'rt')
            teste = a.read().split('\n')
            if teste[0] in lerarquivo(arq2):
                limpar(arq)
                return True
            else:
                limpar(arq)
                return False


def limpar(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
