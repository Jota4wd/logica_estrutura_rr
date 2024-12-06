def bubble_encadeada(primeiro):
    if primeiro is None or primeiro.proximo is None:
        return primeiro

    trocado = True
    while trocado:
        trocado = False
        atual = primeiro
        while atual.proximo is not None:
            if atual.nome > atual.proximo.nome:
                atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                trocado = True
            atual = atual.proximo

    return primeiro


def insertion_encadeada(primeiro):
    if primeiro is None or primeiro.proximo is None:
        return primeiro

    novo_primeiro = None
    atual = primeiro

    while atual is not None:
        proximo = atual.proximo

        if novo_primeiro is None or atual.nome <= novo_primeiro.nome:
            atual.proximo = novo_primeiro
            novo_primeiro = atual
        else:
            anterior = novo_primeiro
            while anterior.proximo is not None and anterior.proximo.nome < atual.nome:
                anterior = anterior.proximo
            atual.proximo = anterior.proximo
            anterior.proximo = atual

        atual = proximo

    return novo_primeiro
