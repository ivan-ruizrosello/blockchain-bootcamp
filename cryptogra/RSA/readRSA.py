from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

with open('clavePrivada.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

ciphertext = b'`F\xd9\xe4\xfa\x948\xc5\xc4\x00g1+\xfbX\x17Yn_\xcc<h\xa2H\xb1pO\x9e\xa32\x17\xc9\x94}\xde\x92`\x0eQEN\xd7@x\x96\x98\x19\x06l\r\xf55\x1aT\xfb:\xd8c9\xc3\xd3\xdft\xb7\x86\xea\x81\xcd3 \xad\xd1\x7f\t\xa6\xbeU\xb1\xa1\x91B\xf1b\xf1\xcc\xa6\xfaV\xdc\xee\xa5r9&\xf7J\x87\x97\xc9\x01&\xd1M\xecp\xbdX\t\x00/\x89\x85\x1c\xd8w\x1f\xfb\xab\xef\xf0\xc2\xcf>\x19\x85\n\x83\\L\xb7!}Z\xaf\xb8\xd6\xc5u\xfeN9T\x8a\xffF$\n\xc9\xc7\xfd8.4\xb38Q\xa9\x15\xe0\xf4i\xac\xe5T;\x0cT\xf4\x80 \xf8Zk\x15\x96\xc0\xffd\xbe*Pd\x97*e\xd9\x06\xad\xdc\x97\x19\xc6\xf0\xdbV\x05\x15v\x89\xed\x1c\x85@\x98;\xbd5V\xe0\xae\xc9\xad\xc7\x91\xa7\x9f].\x14\xd0\xf3\n\xab\x8b\xf4eaO_\x17\n\x12\xa3\x0ea\xe7w\xc6r\x8d&\xd7dW"\x9c\xcc\xa3\xf3\x18\xf8\xd2\x0e\xdc\x8e+'

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None)
)

print('plaintext: ', plaintext)