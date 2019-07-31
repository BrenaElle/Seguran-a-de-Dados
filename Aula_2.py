from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

chave_publica = chave_privada.public_key()


imagem_original = open('Lighthouse.jpg', 'rb').read()

chave_simetrica = Fernet.generate_key()

cripto = Fernet(chave_simetrica)
imagem_encriptada = cripto.encrypt(imagem_original)

with open('imagem_encriptada_rsa.jpg', 'wb') as f:
    f.write(imagem_encriptada)


chave_sim_cript = chave_publica.encrypt(
    chave_simetrica,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# chave simétrica original = b'UsckJqPGlcWK6zMzna-3LQybcz8Em5s-MahMhIW5uoM='
# apagando a chave simétrica
del chave_simetrica
# Resta apenas a chave simétrica criptografada e protegida!

# Recuperando a chave simétrica
chave_sim_rec = chave_privada.decrypt(
    chave_sim_cript,
    padding.OAEP(

        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

cripto = Fernet(chave_sim_rec)
with open('imagem_encriptada_rsa.jpg', 'rb') as img_enc:
   with open('imagem_recuperada_rsa.jpg', 'wb') as img_rec:
       conteudo = cripto.decrypt((img_enc.read()))
       img_rec.write(conteudo)

#criptografia com RSA
