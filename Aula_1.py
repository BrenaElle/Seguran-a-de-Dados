import os
import base64
import random
import struct
import hashlib


from cryptography.fernet import Fernet

imagem_original = open('Penguins.jpg', 'rb').read()

chave = Fernet.generate_key()

cripto = Fernet(chave)

imagem_encriptada = cripto.encrypt(imagem_original)

with open('imagem_encriptada.jpg', 'wb') as f:
    f.write(imagem_encriptada)

with open('imagem_encriptada.jpg', 'r') as img_enc:
    with open('imagem_recuperada.jpg', 'wb') as img_rec:
        conteudo = cripto.decrypt(str.encode(img_enc.read()))
        img_rec.write(conteudo)

#Criptografia com Aes, é para uma imagem mais segura, sendo necessário ter no computador
#o python baixado, e o pip também,sendo diferente os metódos de uso entre o Linux e o Windows, depois dos comandos
#o código a cima é para criptografar uma imagem e depois para recuperá-la.

#Comandos necessários no Cmd("py -m pip" pois o pip já vem no python, é só chamar e depois disso tem que baixar a criptografia e o código é "py -m pip install cryptography")

#depois chamar no Terminal da pasta( py Aula_1.py(nome da pasta))


#A diferença entre o Aes e o Rsa, um é métrico e o outro assimétrico, o Rsa usa pares de chaves(pública e privada) e o outro
#maior proteção da chave(ok, mais qual?)
#AES = Simétrico, usado para pequenas quantidades de dados.
#RSA = Assimétrico, usado para grandes quantidades de dados.