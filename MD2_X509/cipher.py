from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
import typing

import readf
import writef


# -- Iekodē un dekodē ziņojumus.
class cipher(object):
    def __init__(self, filenames: list, direction: str):
        self.hash_algorithm = None
        self.message = None
        self.key = None
        self._read_files(filenames, direction)

    def decrypt(self):
        """ Dekodē ziņojumu. """
        private_key = self.key
        plaintext = private_key.decrypt( 
            self.message,
            padding.OAEP(
                mgf = padding.MGF1(algorithm = hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )
        return plaintext

    def encrypt(self):
        """ Iekodē ziņojumu. """
        if len(self.b_message) > 190:
            raise ValueError("Iekodējamais ziņojums ir par garu.")
        public_key = self.key
        ciphertext = public_key.encrypt(
            self.message,
            padding.OAEP(
                mgf = padding.MGF1(algorithm = hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )
        return ciphertext

    def save(self, output: bytes):
        """ Saglabā rezultātu """
        writef.save_message(output)

    def _read_files(self, filenames: list, direction: str):
        """ Ielādē sertifikātu un privāto atslēgu. """
        key_filename = filenames[0]
        message_filename = filenames[1]

        if direction == "E":
            certificate = readf.read_certificate(key_filename)
            self.key = certificate.public_key()
        else:
            self.key = readf.read_private_key(key_filename)

        self.message = readf.read_text_file(message_filename)

def main_dec(filenames_str: str):
    cip = _new_cipher(filenames_str, "D")
    plaintext = cip.decrypt()
    cip.save(plaintext)

def main_enc(filenames_str: str):
    cip = _new_cipher(filenames_str, "E")
    ciphertext = cip.encrypt()
    cip.save(ciphertext)

def _new_cipher(filenames_str: str, direction: str):
    filenames = filenames_str.split(',')
    cip = cipher(filenames, direction)
    return cip