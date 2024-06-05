import os


def limpar_terminal():
    os.system('cls')


limpar_terminal()
lista = []
apagar = 0
while True:

    opcao = input(
        'Selecione uma opção \n [i]nserir [a]pagar [l]istar:').lower()
    if opcao == 'i':
        os.system('cls')
        compra = input('Digite o produto para adicionar: ')
        lista.append(compra)

    elif opcao == 'a':
        os.system('cls')
        if not lista:
            print('Lista Vazia!')

        else:
            try:
                apagar = int(input('Escolha o Indice para apagar: '))
                if apagar < 0:
                    print('Indice Inválido!')
                else:
                    print('Item: ', lista[apagar], ' apagado!')
                    lista.pop(apagar)

            except (ValueError, IndexError):
                print('Indice Inválido!')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista Vazia!')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)
