from tkinter import *

class MeuApp:
	def __init__(self, pai):
		self.pai = pai
		self.meu_container1 = Frame(pai)
		self.meu_container1.pack()

		self.button1 = Button(self.meu_container1, command=self.button1_click)
		self.button1.configure(text='OK', background='blue')
		self.button1.pack(side=LEFT)
		self.button1.focus_force()

		self.button2 = Button(self.meu_container1, command=self.button2_click)
		self.button2.configure(text='Cancel', background='yellow')
		self.button2.pack(side=RIGHT)

	def button1_click(self):
		print('button1_click event handler')
		self.button1.configure(text='clicado')

	def button2_click(self):
		print('button2_click event handler')
		self.pai.quit()


raiz = Tk()
meuapp = MeuApp(raiz)
raiz.mainloop()