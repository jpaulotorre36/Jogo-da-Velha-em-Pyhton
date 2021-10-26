
#Jogo da Velha para treinar game com python
#autor: João Paulo 
import os
import random
from colorama import Fore, Back, Style

#variaveis
jogarNovamente = "s" #p/ jogar novamente
jogadas = 0 #numero de jogadas
quemJoga = 2 #total de jogadores CPU=1 e jogador=2
maxJogadas = 9 #maximo de jogadas
vit= "n" # boolean para decidir se ganhou ou não 
#array para o jogo da velha 
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

#função para fazer as jogadas
def tela():
    global velha #delcarado como global por motivos pessoais
    global jogadas
    os.system("cls")
    #desenhando o array, matriz do jogo da velha
    print("    0   1   2")
    print("0:  " + velha[0][0]+ " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0]+ " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0]+ " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)
    
#tela() 
#teste do desenho no cmd/terminal 


#loop de jogadas do jogador e da CPU 
#definir se ganhou ou não e continuar a jogar

#função de jogadas
def jogadorJoga():
    #variaveis que serão usadas
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        l=int(input("Linha...: "))
        c=int(input("Coluna...: "))
        #verificar se a celula está vaga, caso não esteja jogue novamente
        try:
            while velha[l][c]!= " ":
                l=int(input("Linha...: "))
                c=int(input("Coluna...: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha ou Coluna invalida")

#jogada da cpu
def cpujoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga ==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2



        

while True: 
    tela()
    jogadorJoga()
    cpujoga()
    


