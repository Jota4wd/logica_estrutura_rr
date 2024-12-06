from tkinter import *

class Aplicacao:
	def __init__(self, pai):
		self.pai = pai
		self.cesta = Frame(pai,padx=30,pady=30)
		self.cesta.pack()
		self.rotulo = Label(self.cesta)
		self.rotulo.pack(side=LEFT)
		for i in range(24):
			for j in range(60):
				for z in range(60):
					self.rotulo.configure(text=str(i)+':'+str(j)+':'+str(z))
					self.rotulo.update()


raiz = Tk(None, None, 'Teste da Janela')
ap = Aplicacao(raiz)
raiz.mainloop()
