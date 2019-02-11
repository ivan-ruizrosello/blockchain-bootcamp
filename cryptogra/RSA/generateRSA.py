from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

miMensaje = b'Mensaje de prueba'

ciphertext = public_key.encrypt(
        miMensaje,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
          label=None
     )
)

plaintext = private_key.decrypt(ciphertext,padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
 ))
# print(ciphertext)
# print(plaintext)

pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
print('pem: ', pem.decode('utf-8'))

archivo = open('clavePublica.pem', 'w')
archivo.write(pem.decode('utf-8'))
archivo.close()

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
archivo = open('clavePrivada.pem', 'w')
archivo.write(pem.decode('utf-8'))
archivo.close()