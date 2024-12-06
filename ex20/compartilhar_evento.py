import os
from tkinter import *

class Aplicacao:
    def __init__(self, pai):
        self.numero_cliques = 0
        nome_botao = 'PRIMEIRO'
        
        self.pai = pai
        self.porta_objetos = Frame(pai)
        self.porta_objetos.pack(padx=20, pady=20)
        
        self.primeiro_botao = Button(self.porta_objetos,text='0', \
            command=lambda arg=nome_botao : self.primeiro_botao_clique(arg))
        self.primeiro_botao.pack()
        
    def primeiro_botao_clique(self,nome):
        self.numero_cliques += 1
        self.primeiro_botao.configure(text=str(nome)+":"+str(self.numero_cliques))

os.system('clear')
raiz = Tk()
raiz.title('Teste de eventos')
ap = Aplicacao(raiz)

raiz.mainloop()
