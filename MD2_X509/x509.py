import typing

import tbscertificate as tbs
import writef

# -- X.509 sertifikāta izgatavošanai
class myX509(object):
    def __init__(self, filename: str):
        self.TBScertificate = None
        self.private_key = None
        self.certificate = None
        self._create(filename)

    def save(self):
        """ Saglabā sertifikātu un privāto atslēgu kā failus. """
        writef.write_file(
            self.certificate,
            self.private_key,
            self.certificate.serial_number
            )

    def _create(self, filename: str):
        """ Izgatavo sertifikātu. """
        self.TBScertificate = tbs.TBScertificate(filename)
        self.private_key = self.TBScertificate.subject_public_key['subject_private_key']
        self.certificate = self._set_certificate()

    def _set_certificate(self):
        """ Paraksta sertifikātu. """
        algorithm_name = self.TBScertificate.signature['hash']
        algorithm = self.TBScertificate._valid_digest[algorithm_name]()
        certificate_build = self.TBScertificate.build()
        certificate = certificate_build.sign(
            private_key = self.private_key,
            algorithm = algorithm
            )
        return certificate

def main(filename: str):
    cert = myX509(filename)
    cert.save()