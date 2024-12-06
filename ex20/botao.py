from tkinter import *

raiz = Tk()
cesta = Frame(raiz)
cesta.pack()
botao = Button(cesta)
botao['text'] = 'hello world'
botao['background'] = 'blue'
botao.pack()
raiz.mainloop()