from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())

data = b"Mensaje que quiero firmar"
signature = private_key.sign(data, hashes.SHA256())


print('Signature: ', utils.decode_dss_signature(signature))

public_key = private_key.public_key()
validation = public_key.verify(signature, data, hashes.SHA256())
print('validation: ', validation)