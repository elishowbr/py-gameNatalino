import time
import os

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
                print(f'Nota de comportamento: {criancaRestante["nota_comportamento"]}')
                time.sleep(1)
                print(f'Cartinha: {criancaRestante["cartinha"]}\n')
                time.sleep(1)
                decisao = input("Essa criança merece presente? (s/n) ")
                match decisao.lower():
                    case 's':
                        clear()
                        criancaRestante["respondida"] = True
                        print('Agora falta os pontos')
                        break
                    case 'n':
                        clear()
                        criancaRestante["respondida"] = True
                        print('agora falta verificar os pontos')
                        break
                    case _:
                        print('Entrada inválida')
                        time.sleep(2)
                        clear()
    else:
        print('Verificaçao dos pontos finais')
            