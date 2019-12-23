def leiastr(tente):
    while True:
        try:
            valor = str(input(tente)).strip().upper()[0]
        except:
            print('Por favor, ', end='')
        else:
            break
    return valor


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
