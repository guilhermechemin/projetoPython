import os


def limpar_terminal():
    os.system('cls')


limpar_terminal()

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letraDigitada = input('Digite uma letra:')
    tentativas += 1
    if len(letraDigitada) > 1:
        letraDigitada = input('Digite apenas uma letra: ')
        continue

    if letraDigitada in palavra_secreta:
        letras_acertadas += letraDigitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print("PARABÉNS! VOCÊ GANHOU! ")
        print("Palavra Secreta: ", palavra_secreta.upper())
        print("Nº Tentativas: ", tentativas)
        break
