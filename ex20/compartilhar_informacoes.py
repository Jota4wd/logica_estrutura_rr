from tkinter import *

class Aplicacao:
    def __init__(self, pai):
        # Guarda o último botão pressionado
        self.ultimo_pressionado = None

        self.pai = pai
        self.porta_objetos = Frame(pai)
        self.porta_objetos.pack(padx=20, pady=20)

        self.primeiro_botao = Button(self.porta_objetos, text='NENHUM CLICADO', command=self.primeiro_botao_clique)
        self.primeiro_botao.pack()

        self.segundo_botao = Button(self.porta_objetos, text='NENHUM CLICADO', command=self.segundo_botao_clique)
        self.segundo_botao.pack()

        self.terceiro_botao = Button(self.porta_objetos, text='NENHUM CLICADO', command=self.terceiro_botao_clique)
        self.terceiro_botao.pack()

    def primeiro_botao_clique(self):
        self.ultimo_pressionado = 'PRIMEIRO'
        self.atualiza_botoes()

    def segundo_botao_clique(self):
        self.ultimo_pressionado = 'SEGUNDO'
        self.atualiza_botoes()

    def terceiro_botao_clique(self):
        self.ultimo_pressionado = 'TERCEIRO'
        self.atualiza_botoes()

    def atualiza_botoes(self):
        self.segundo_botao.configure(text='SEGUNDO: << CLICADO POR ÚLTIMO = ' + str(self.ultimo_pressionado))
        self.primeiro_botao.configure(text='PRIMEIRO: << CLICADO POR ÚLTIMO = ' + str(self.ultimo_pressionado))
        self.terceiro_botao.configure(text='TERCEIRO: << CLICADO POR ÚLTIMO = ' + str(self.ultimo_pressionado))

# Inicialização da aplicação
raiz = Tk()
raiz.title('teste de informacoes')
ap = Aplicacao(raiz)

raiz.mainloop()
