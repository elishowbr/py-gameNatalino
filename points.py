def atualizarPontos(notaComportamento = int, pontuacaoAtual = int, update = str):
    saveState = pontuacaoAtual
    if update == 's':
        if notaComportamento >= 6:
            pontuacaoAtual += notaComportamento
        else:
            pontuacaoAtual -= notaComportamento
    else:
        if notaComportamento <= 6:
            pontuacaoAtual += notaComportamento * 2
        else:
            pontuacaoAtual -= notaComportamento * 2
    print(f'PONTOS: {saveState} -> {pontuacaoAtual}')
    return pontuacaoAtual