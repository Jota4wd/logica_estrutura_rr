from tkinter import *

class MinhaAplicacao:
	def __init__(self, meu_pai):
		self.minha_cesta = Frame(meu_pai)
		self. minha_cesta.pack()
		self.botao1 = Button(self. minha_cesta)
		self. botao1['text']= 'hello world!'
		self. botao1.pack()

raiz= Tk()
minhapp = MinhaAplicacao(raiz)
raiz.mainloop()