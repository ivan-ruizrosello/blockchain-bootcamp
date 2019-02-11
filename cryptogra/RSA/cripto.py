# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
#
# digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
# digest.update(b"Esto es un mensaje secreto")
# d = digest.finalize()
# print ('sha512: ', d)
# print ('sha512: ', d.hex())





from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key_A = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
# Fermat primes 3, 5, 17, 257, 65537
#key size =2048 or 4096. Not less than 512, 1024

public_key_A = private_key_A.public_key()

private_key_B = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
public_key_B = private_key_B.public_key()

#Ciphering
#from A side
#with public key B

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
message = b"encrypted data"
ciphertext = public_key_B.encrypt(message,
padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
#OAEP is the recommended choice for any new protocols or applications
# PKCS1v15 should only be used to support legacy protocols.

print('ciphertext: ', ciphertext)
print('ciphertext: ', ciphertext.hex())

#Deciphering
#with private key B

plaintext = private_key_B.decrypt(ciphertext,
padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print('plaintext: ', plaintext)
print(plaintext == message)








