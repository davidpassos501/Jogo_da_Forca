from lib.leia import leiaint


def linha(tam=40):
    return print('=' * tam)


def cabecalho(txt):
    linha()
    print(txt.center(40))
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'[ {c} ] - {item}')
        c += 1
    opc = leiaint('\n[ ? ] - Sua Opção: ')
    return opc

