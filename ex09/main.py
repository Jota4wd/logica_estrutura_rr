from arvore_expressao import ArvoreExpressao
from huffman import Huffman

# Teste da Árvore de Expressão
print("=== Teste Árvore de Expressão ===")
arvore = ArvoreExpressao()
expressao = "ab+cd-*"  # representa (a+b)*(c-d)
raiz = arvore.criar_arvore_expressao(expressao)
print("Expressão em ordem: ")
arvore.imprimir_em_ordem(raiz)
print("\n")

# Teste do Huffman
print("=== Teste Codificação Huffman ===")
texto = "essa mensagem sera codificada"
huffman = Huffman()
huffman.criar_arvore(texto)
huffman.gerar_codigos()

print("Códigos Huffman:")
for char, codigo in huffman.codigos.items():
    print(f"'{char}': {codigo}")