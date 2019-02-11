from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

with open('claveLorenzo.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

message = b"Nos pegamos?"
ciphertext = public_key.encrypt(message,
padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
#OAEP is the recommended choice for any new protocols or applications
# PKCS1v15 should only be used to support legacy protocols.

print('ciphertext: ', ciphertext)
print('ciphertext: ', ciphertext.hex())