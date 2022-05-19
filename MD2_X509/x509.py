from cryptography import x509
import typing

import tbscertificate as tbs
import writef

# -- X.509 sertifikāta izgatavošanai
class my_x509(object):
    def __init__(self, filename: str):
        self.TBScertificate = None
        self.certificate = None
        self.signature_algorithm = None
        self.signature_value = None
        self._create(filename)

    def save(self):
        """ Saglabā sertifikātu un privāto atslēgu kā failus. """
        _output_dir = "output"
        writef.write_file(
            self.certificate,
            self.TBScertificate.subject_public_key['subject_private_key'],
            self.TBScertificate.serial_number
            )

    def _create(self, filename: str):
        """ Izgatavo sertifikātu. """
        self.TBScertificate = tbs.TBScertificate(filename)
        self.certificate = self.TBScertificate.build()
        self.signature_algorithm = self._set_signature_algorithm()
        self.signature_value = self._set_signature_value()

    def _set_signature_algorithm(self) -> dict:
        """ Iestata informāciju par paraksta algoritmu. """
        params = [] # TODO var būt nepieciešams iegūt un norādīt papildus parametrus.
        return {'signature': self.TBScertificate.signature,
                'parameters': params}

    def _set_signature_value(self) -> x509.Certificate:
        """ Paraksta sertifikātu. """
        private_key = self.TBScertificate.subject_public_key['subject_private_key']
        algorithm_name = self.signature_algorithm['signature']['hash']
        algorithm = self.TBScertificate._valid_digest[algorithm_name]
        certificate = self.certificate.sign(
            private_key = private_key,
            algorithm = algorithm
            )
        return certificate

def main(filename: str):
    cert = my_x509(filename)
    cert.save()