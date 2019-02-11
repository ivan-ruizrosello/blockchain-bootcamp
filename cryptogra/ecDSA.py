from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import (dsa, ec, utils)
from cryptography.hazmat.primitives import hashes


private_key = ec.generate_private_key(
    # ec.SECP384R1(),
    ec.SECP256K1(), # Es la curva eliptica que usa bitcoin
    default_backend()
)
data = b"Mensaje que quiero firmar"
signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

print('Signature: ', utils.decode_dss_signature(signature))

public_key = private_key.public_key()
validation = public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
print('validation: ', validation)