import os
import binascii

nome = str(input('nome do arquivo: '))
arquivo = open(nome, 'rb')
print('listagem do arquivo: ')

bytes = arquivo.read()

if bytes != '':
    hex_str = str(binascii.hexlify(bytes))
    print(hex_str)

print('fim')
