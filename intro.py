import time
import os
import json
from game import rotinaNatalina

def clear():
    os.system('cls')


with open('criancas.json', 'r') as f:
    listaCriancas = json.load(f)

def introGame():
    print("Bem vindo às aventuras natalinas da Infinity School!")
    time.sleep(2)
    while True:
        escolha = input("""
Escolha sua opção:
    1 - Jogar
    2 - Como Jogar
    3 - Sobre
    4 - Sair
                    
                """)
        clear()
        match escolha:
            case '1':
                rotinaNatalina(listaCriancas)
                break
            case '2':
                print("""
Na aventura de hoje, você terá o papel do papai Noel da Infinity School.
Seu trabalho será avaliar a lista de mensagens que as crianças escreveram nesse natal.

Algumas delas são boazinhas e se comportaram bem durante o ano, mas outras crianças foram muito mimadas e não vão receber presentes esse ano.
Para cada criança boa recompensada, você acumulará pontos. Para cada criança mal educada recompensada, você perderá pontos.
Seja o papai Noel DEV mais premiado da Infinity School!
         
                """)
                time.sleep(5)
                input("Pressione ENTER para voltar...")
                clear()
            case '3':
                print("""

    Trabalho criado através de muita criatividade e carinho!
                    
A chave para o aprendizado é a persistência e humildade nos estudos!
                                
                                    Feito por Elisson Victor.
                      """)
                time.sleep(3)
                input("pressione ENTER para voltar...")
                clear()
            case '4':
                print("Até logo! Ho ho ho....")
                break
            case 'hohoho':
                print("Feliz Natal! Boas festas para você e sua família!")
            case _:
                print("Entrada inválida.")
                time.sleep(1)
                clear()
