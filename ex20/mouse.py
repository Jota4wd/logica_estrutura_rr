from tkinter import *

class Aplicacao:
	def __init__(self, pai):
		self.pai = pai
		self.cesta = Frame(pai,padx=30, pady=30, bg='red')
		self.cesta.pack()

		self.botao1 = Button(self.cesta)
		self.botao1.configure(text='OK', background='green')
		self.botao1.pack(side=LEFT)
		self.botao1.bind('<Button-1>', self.button1_click)

		self.botao2 = Button(self.cesta)
		self.botao2.configure(text='Cancel', background='red')
		self.botao2.pack(side=RIGHT)
		self.botao2.bind('<Button-1>', self.button2_click)

		self.num_cliquesB1 = 0

	def button1_click(self, event):
		self.num_cliquesB1 += 1
		self.botao1.configure(text=str(self.num_cliquesB1))

	def button2_click(self, event):
		self.pai.quit()


raiz = Tk(None, None, 'teste de janela')
ap = Aplicacao(raiz)
raiz.mainloop()