from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

with open('claveLorenzo.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

message = b'Este mensaje es superimportante. Por eso lo firmo.'
signature = b'2*_#\x0f\xcan=\x89)\xf4@\xd8\xbb\xe7\t\xab\x89\xd0\n\xb6k\xde\xe5\xbc\xb2\xbe\x9f\n\x1b&\xd0\xd0\x82P\xd5a\x84\xc4\xb8\xd8t\x0b\xac\xea\xa7\xd4\x93\xc9@\xd8U\xe1\x93;#\x14q\xe7P\xb1\x8d\xa8S\xc5F\x98\xe8\xb6\r\xfchU\xcc\xc2\x0b\x93\x91\xfd#\xd05\xd3\x921\xc2w\xa6c\xaa\xde\xc2n`\x11\xa5\xb4\xe7%\x81\xc5(\xf0\xd5`\xf0>D\xbbIN\xc4\x9e\x9c\xf2\xc6\xea1\xc9\x96\x89\n\xc0E\xd9\x05m\xd5\xd6\xcf\xdf\xee\xb4\x83Q\xcf\x0b\xea\xf1=\xa9\\%a8\xbc4\x82\xa5\xf8\x88HWvH\xae,\xd7\x10\x04\x90\xc2\x0c\xb9\x14\x8d\xb2\n>\x0b\xdb\xd2z\xac=M}\x01N%\x1akd\x0e$\xad\xa9bV|k6\x86\xe7-N\xbd\xf1C\x89\x01\x14\x13\x03id\xf6\x8c\xa3/\xf8N?w\x0c\x07\x0c\xf6\x1b\\jU\xe7\xa3\xe4\x9cDO\xd8\x10\x17\xc8F\x1d4\x0e\xc9\xe2Qz#G\xba\\\x01V\x1c\x13\x1d\x08,\x02\xa4&\xbb\xdf'

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
 )