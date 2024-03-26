#JOGO DA FORCA - ROSALINA OLIVEIRA ARRUDA

import random  #vai ser usado para escolher a palavra aleatoria
from os import system, name 

#função para limpar a tela a cada execução
def limpa_tela():

    #se for windows
    if name == 'nt':
        _ = system('cls')

    #mac e linux
    else:
        _ = system('clear')

def display(chances):

    estagios = [ #estagio6
        """
            --------
            |      |
            |      O
            |     \|/
            |      |
            |     / \
            |
            -
         """,
         #estagio5
        """
            --------
            |      |
            |      O
            |     \|/
            |      |
            |     / 
            |
            -
         """,
         #estagio4
        """
            --------
            |      |
            |      O
            |     \|/
            |      |
            |      
            |
            -
         """,
         #estagio3
        """
            --------
            |      |
            |      O
            |     \|
            |      
            |      
            |
            -
         """,
         #estagio2
        """
            --------
            |      |
            |      O
            |     
            |      
            |      
            |
            -
         """,
         #estagio1
        """
            --------
            |      |
            |      
            |     
            |      
            |      
            |
            -
         """
    ]
    return estagios[chances-1]


def game():

    limpa_tela()

    print("Bem-vindo(a) ao jogo da Forca!!")
    print("Adivinhe a palavra abaixo:\n")

    #lista de paravras para o jogo:
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #escolhendo randomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = [letra for letra in palavra]

    tabuleiro = ['_'] * len(palavra)

    #numero maximo de chances do usuario
    chances = 6

    #lista de letras erradas
    letras_tentativas = []

    #loop para que possa tentar varias vezes
    while chances > 0:

        print(display(chances))
        print('Palavra: ', tabuleiro)
        print('\n')

        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in letras_tentativas:
            print('Você já tentou essa letra, escolha outra!!')
            continue

        letras_tentativas.append(tentativa)

        if tentativa in letras_descobertas:
            print('Você acertou uma letra!')
            
            for indice in range(len(letras_descobertas)):

                if letras_descobertas[indice] == tentativa:
                   tabuleiro[indice] = tentativa
        
            if '_' not in tabuleiro:
                print('\nVocê venceu!! A palavra era:', palavra)
                break

        else:
            print('Ops. Essa letra não está na palavra. Chance:', chances)
            print(letras_tentativas)
            chances -= 1

    if '_' in tabuleiro:
        print('\nVocê perdeu!! A palavra era:', palavra)


#indica que o script é um programa em python
if __name__ == '__main__':
    game()
    print('\nJogue novamente!! :D \n')