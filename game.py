import time
import os
from points import atualizarPontos

def clear():
    os.system('cls')

def rotinaNatalina(listaDeCriancas=list):
    pontuacao = 0
    print(f"""   Boa noite, Sr. Noel!
                
Hoje teremos {listaDeCriancas.__len__()} crianças para a análise.
""")
    time.sleep(2)

    for criancaRestante in listaDeCriancas:
        if criancaRestante["respondida"]:
            pass
        else:
            while True:
                print(f'Criança: {criancaRestante["nome"]}')
                time.sleep(1)
                print(f'Idade: {criancaRestante["idade"]}')
                time.sleep(1)
                print(f'Cartinha: {criancaRestante["cartinha"]}\n')
                time.sleep(1)
                decisao = input("Essa criança merece presente? (s/n) ").lower()
                match decisao:
                    case 's':
                        clear()
                        criancaRestante["respondida"] = True
                        pontuacao = atualizarPontos(notaComportamento=criancaRestante["nota_comportamento"], pontuacaoAtual=pontuacao, update=decisao)
                        break
                    case 'n':
                        clear()
                        criancaRestante["respondida"] = True
                        pontuacao = atualizarPontos(notaComportamento=criancaRestante["nota_comportamento"], pontuacaoAtual=pontuacao, update=decisao)
                        break
                    case _:
                        print('Entrada inválida')
                        time.sleep(2)
                        clear()
    else:
        print('Fim do expediente!!!')
        time.sleep(1)
        print('Foi um longo dia de trabalho... espero que tenha feito boas decisões hoje...')
        time.sleep(1)
        print(f"""
                Fim de Jogo!
            SUA PONTUACAO: {pontuacao}""")
            