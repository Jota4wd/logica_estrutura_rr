from tkinter import *

class MeuApp:
	def __init__(self, pai):
		self.pai = pai
		self.meu_container1 = Frame(pai, padx=20, pady=20)
		self.meu_container1.pack()

		self.button1 = Button(self.meu_container1)
		self.button1.configure(text='OK')
		self.button1.pack(side=LEFT)
		self.button1.focus_force()
		self.button1.bind('<Button-1>', self.button1_click)
		self.button1.bind('<Return>', self.button1_click)

		self.button2 = Button(self.meu_container1)
		self.button2.configure(text='Cancel')
		self.button2.pack(side=RIGHT)
		self.button2.bind('<Button-1>', self.button2_click)
		self.button2.bind('<Return>', self.button2_click)

	def button1_click(self, event):
		report_event(event)
		self.button1['text'] = 'clicado'

	def button2_click(self, event):
		report_event(event)
		self.pai.quit()


def report_event(event):
	event_name = {
        '2': 'KeyPress',
        '4': 'ButtonPress'
    }
	print(f'Time:', {event.time})
	print(f'EventType: {event_name.get(str(event.type), "Unknown")} EventWidget: {event.widget} EventKeySymbol: {event.keysym}')

raiz = Tk()
meuapp = MeuApp(raiz)
raiz.mainloop()