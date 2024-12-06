import os
from PIL import Image

def encode_image(image_path, message, output_path):
    # Converte a mensagem em uma string binária
    binary_message = ''.join(format(ord(c), '08b') for c in message) + '00000000'

    # Abre e converte a imagem para RGB
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # Verifica se a imagem é grande o suficiente
    if len(binary_message) > width * height:
        raise ValueError("Mensagem muito grande para esta imagem")

    # Cria uma nova imagem
    encoded = Image.new('RGB', (width, height))

    message_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            # Se ainda há bits para esconder
            if message_index < len(binary_message):
                # Modifica o bit menos significativo do canal vermelho
                pixel[0] = (pixel[0] & ~1) | int(binary_message[message_index])
                message_index += 1

            encoded.putpixel((x, y), tuple(pixel))

    # Salva a imagem em PNG (sem compressão)
    output_path = output_path.rsplit('.', 1)[0] + '.png'
    encoded.save(output_path, 'PNG')
    return output_path

def decode_image(image_path):
    # Abre a imagem
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # Extrai os bits da mensagem
    binary_message = ''
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            binary_message += str(pixel[0] & 1)

            # Verifica se encontramos o terminador (8 zeros)
            if len(binary_message) >= 8 and '00000000' in binary_message:
                # Encontra onde termina a mensagem
                end_index = binary_message.index('00000000')
                binary_message = binary_message[:end_index]

                # Converte bits para caracteres
                message = ''
                for i in range(0, len(binary_message), 8):
                    byte = binary_message[i:i+8]
                    if len(byte) == 8:
                        message += chr(int(byte, 2))
                return message

    return "Nenhuma mensagem encontrada"

def main():
    while True:
        print('\n--- Esteganografia ---')
        print('<1> -> Codificar mensagem em imagem')
        print('<2> -> Decodificar mensagem de imagem')
        print('<0> -> Sair')

        escolha = input('Enter: ')

        if escolha == '1':
            image_path = input('Caminho da imagem: ')
            if not os.path.exists(image_path):
                print('Erro: Arquivo de imagem não encontrado.')
                continue

            message = input('Mensagem a ser escondida: ')
            output_path = input('Caminho da imagem de saída: ')

            try:
                final_path = encode_image(image_path, message, output_path)
                print(f'Mensagem codificada com sucesso na imagem: {final_path}')
                print('Nota: A imagem foi salva em formato PNG para preservar a mensagem.')
            except Exception as e:
                print(f'Erro ao codificar a mensagem: {e}')

        elif escolha == '2':
            image_path = input('Caminho da imagem com a mensagem codificada: ')
            if not os.path.exists(image_path):
                print('Erro: Arquivo de imagem não encontrado.')
                continue

            try:
                decoded_message = decode_image(image_path)
                print('Mensagem decodificada:', decoded_message)
            except Exception as e:
                print(f'Erro ao decodificar a mensagem: {e}')

            input('Pressione Enter para continuar...')

        elif escolha == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
