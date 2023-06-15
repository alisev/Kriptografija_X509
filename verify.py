from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from datetime import datetime
import typing

import readf

class verifier(object):
    def __init__(self, filenames: list):
        self.certificate = None
        self.private_key = None
        self._read_files(filenames)

    def verify(self):
        """ Veic nepieciešamās darbības, lai noteiktu, vai sertifikāts ir derīgs. """
        subject = self._verify_subject()
        key = self._verify_key()
        if subject and key:
            print("Šis sertifikāts IR derīgs.")
        else:
            print("Šis sertifikāts NAV derīgs.")

    def _read_files(self, filenames: list) -> list:
        """ Ielādē sertifikātu un privāto atslēgu. """
        certificate_filename = filenames[0]
        key_filename = filenames[1]
        self.certificate = readf.read_certificate(certificate_filename)
        self.private_key = readf.read_private_key(key_filename)

    def _verify_key(self) -> bool:
        """ Nosaka, vai izdēvēja paraksts atbilst lietotāja publiskajai atslēgai. """
        try:
            self.private_key.public_key().verify(
                self.certificate.signature,
                self.certificate.tbs_certificate_bytes,
                padding.PKCS1v15(),
                self.certificate.signature_hash_algorithm,
            )
        except:
            return False
        else:
            return True

    def _verify_subject(self) -> bool:
        """ Salīdzina sertifikātā norādīto izdēvēju ar sertifikāta turētāju. """
        if self.certificate.issuer == self.certificate.subject:
            return True
        return False

def main(filenames_str: str):
    filenames = filenames_str.split(',')
    ver = verifier(filenames)
    ver.verify()
