# servidor.py
import socket
import threading

class Servidor:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes = []  # Lista para armazenar as conexões dos clientes
        
    def iniciar(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor iniciado em {self.host}:{self.port}")
        
        while True:
            cliente_socket, endereco = self.server_socket.accept()
            print(f"Nova conexão de {endereco}")
            
            # Cria uma nova thread para cada cliente
            thread_cliente = threading.Thread(
                target=self.handle_cliente,
                args=(cliente_socket, endereco)
            )
            thread_cliente.start()
            self.clientes.append(cliente_socket)
            
    def handle_cliente(self, cliente_socket, endereco):
        """Função que lida com cada cliente em uma thread separada"""
        try:
            while True:
                # Recebe mensagem do cliente
                mensagem = cliente_socket.recv(1024).decode('utf-8')
                if not mensagem:
                    break
                
                print(f"Mensagem de {endereco}: {mensagem}")
                
                # Envia a mensagem para todos os outros clientes
                self.broadcast(mensagem, cliente_socket)
                
        except:
            print(f"Cliente {endereco} desconectado")
        finally:
            # Remove o cliente da lista e fecha a conexão
            if cliente_socket in self.clientes:
                self.clientes.remove(cliente_socket)
            cliente_socket.close()
            
    def broadcast(self, mensagem, remetente):
        """Envia mensagem para todos os clientes exceto o remetente"""
        for cliente in self.clientes:
            if cliente != remetente:
                try:
                    cliente.send(mensagem.encode('utf-8'))
                except:
                    cliente.close()
                    if cliente in self.clientes:
                        self.clientes.remove(cliente)

if __name__ == '__main__':
    servidor = Servidor()
    try:
        servidor.iniciar()
    except KeyboardInterrupt:
        print("\nServidor encerrado")
    finally:
        # Fecha todas as conexões
        for cliente in servidor.clientes:
            cliente.close()
        servidor.server_socket.close()