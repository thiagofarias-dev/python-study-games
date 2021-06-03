import random

def jogar():
    
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    erros = 0

    while(True):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))

        if (erros == len(palavra_secreta)):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    imprime_mensagem_fim_de_jogo(palavra_secreta)

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print()
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print()
    print("Você perdeu!")

def imprime_mensagem_fim_de_jogo(palavra_secreta):
    print("A palavra secreta era ", palavra_secreta)
    print()
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()