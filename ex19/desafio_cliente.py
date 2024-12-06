# cliente.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import time

def main():
        cliente = Cliente()
        try:
            cliente.iniciar()
        except:
            cliente.encerrar()


class Cliente:
    def __init__(self, host='localhost', port=5000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        
        # Interface gráfica
        self.janela = tk.Tk()
        self.janela.title("Chat Cliente")
        self.criar_widgets()
        
    def criar_widgets(self):
        # Área de chat
        self.chat_area = scrolledtext.ScrolledText(self.janela, wrap=tk.WORD, width=40, height=20)
        self.chat_area.pack(padx=10, pady=10)
        
        # Campo de entrada
        self.entrada = tk.Entry(self.janela, width=40)
        self.entrada.pack(padx=10, pady=5)
        
        # Botão de enviar
        self.btn_enviar = tk.Button(self.janela, text="Enviar", command=self.enviar_mensagem)
        self.btn_enviar.pack(pady=5)
        
        # Bind Enter key
        self.entrada.bind('<Return>', lambda e: self.enviar_mensagem())
        
    def conectar(self):
        try:
            self.socket.connect((self.host, self.port))
            self.adicionar_mensagem("Conectado ao servidor!")
            
            # Inicia thread para receber mensagens
            thread_receber = threading.Thread(target=self.receber_mensagens)
            thread_receber.daemon = True
            thread_receber.start()
            
        except Exception as e:
            self.adicionar_mensagem(f"Erro ao conectar: {str(e)}")
            
    def enviar_mensagem(self):
        mensagem = self.entrada.get()
        if mensagem:
            try:
                self.socket.send(mensagem.encode('utf-8'))
                self.adicionar_mensagem(f"Você: {mensagem}")
                self.entrada.delete(0, tk.END)
            except:
                self.adicionar_mensagem("Erro ao enviar mensagem")
                
    def receber_mensagens(self):
        while True:
            try:
                mensagem = self.socket.recv(1024).decode('utf-8')
                self.adicionar_mensagem(f"Recebido: {mensagem}")
            except:
                self.adicionar_mensagem("Desconectado do servidor")
                break
                
    def adicionar_mensagem(self, mensagem):
        self.chat_area.insert(tk.END, mensagem + '\n')
        self.chat_area.see(tk.END)
        
    def iniciar(self):
        self.conectar()
        self.janela.mainloop()
        
    def encerrar(self):
        try:
            self.socket.close()
        except:
            pass
        self.janela.quit()

if __name__ == '__main__':
	main()