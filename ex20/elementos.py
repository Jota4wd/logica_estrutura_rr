from tkinter import *

class Aplicacao:
    def __init__(self, pai):
        self.pai = pai
		
		# criar o menu basico
        self.menu = Menu(pai)
        # Adicionar o menu
        self.pai.config(menu=self.menu)

        # Criar nosso submenu
        self.subMenu = Menu(self.menu)

        # Adicionar nosso submenu ao menu básico
        self.menu.add_cascade(label="Opção 1", menu=self.subMenu)

        # Adicionar itens ao submenu
        self.subMenu.add_command(label="Nada", command=self.nada)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Sair", command=self.pai.quit)

        # Criar um container
        self.cesta = Frame(pai, padx=30, pady=30)
        self.cesta.pack()

        self.lb2 = LabelFrame(self.cesta)
        self.lb2.configure(text="Eu sou um LabelFrame", padx=10, pady=10)
        self.lb2.pack(padx=20, pady=20)

        self.rotulo = Label(self.lb2)
        self.rotulo.configure(text="Eu sou um Label. Ao lado tem um Entry")
        self.rotulo.pack()

        self.entrada = Entry(self.lb2)
        self.entrada.pack()

        self.botao1 = Button(self.lb2)
        self.botao1.configure(text="Eu sou um Botão")
        self.botao1.pack()

        self.botao2 = Checkbutton(self.lb2)
        self.botao2.configure(text="Eu sou um CheckButton")
        self.botao2.pack()

        self.canvas = Canvas(self.lb2)
        self.canvas["bg"] = "cyan"
        self.canvas.create_line(0, 0, 200, 100)
        self.canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")
        self.canvas.create_text(100, 100, text="Eu sou um canvas")
        self.canvas.pack()

    def nada(self):
        print("Não vou fazer nada!")

# Inicialização da aplicação
raiz = Tk()
meuapp = Aplicacao(raiz)
raiz.mainloop()