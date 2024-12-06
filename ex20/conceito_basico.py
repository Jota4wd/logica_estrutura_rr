import os

def main():
	while 1:
		gera_gui()
		resposta = input().lower()
		if resposta =='a':
			handle_a()
		elif resposta == 'b':
			handle_b()
		elif resposta == 'c':
			handle_c()
		elif resposta =='x':
			os.system('clear')
			print('cya')
			break
		else:
			input('opção invalida')

def handle_a():
	print('errado tente novamente')
	input('continuar')

def handle_b():
	print('correto')
	input('continuar')

def handle_c():
	print('errado tente novamente')
	input('continuar')

def gera_gui():
	os.system('clear')
	print('                Jogo Realmente Desafiador')
	print('================================================================')
	print('Pressione a tecla correspondente a resposta e depois tecle enter')
	print('(A).Animal (B).Vegetal (C).Mineral (X).Sair')
	print('================================================================')
	print('O que eh trilio?')

if __name__ == '__main__':
	main()