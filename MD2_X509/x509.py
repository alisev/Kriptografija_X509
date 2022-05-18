import typing

import tbscertificate as tbs

# -- X.509 sertifikāta izgatavošanai
class x509(object):
    def __init__(self, filename: str):
        self.TBScertificate = None
        self.signature_algorithm = None
        self.signature_value = None
        self._create(filename)

    def save(self):
        """ Saglabā sertifikātu """
        pass

    def _create(self, filename: str):
        """ Izgatavo sertifikātu. """
        self.TBScertificate = tbs.TBScertificate(filename)
        self.signature_algorithm = self._set_signature_algorithm()
        #self.signature_value = self._set_signature_value() # TODO funkcija

    def _set_signature_algorithm(self) -> dict:
        """ Iestata informāciju par paraksta algoritmu. """
        params = [] # TODO var būt nepieciešams iegūt un norādīt papildus parametrus.
        return {'algorithm': self.TBScertificate.signature,
                'parameters': params}

    def _set_signature_value(self) -> bytes:
        """ Aprēķina paraksta vērtību. """
        message = 'example' # TODO
        key = self.TBScertificate.subject_public_key
        print(key)
        algorithm = self.TBScertificate.get_hash_algorithm()
        hash = algorithm(message) # Nestrādā, trūkst key n 
        signer = PKCS1_v1_5.new(key) # nomainīt algoritmu
        signature = signer.sign(hash)
        return signature

def main(filename: str):
    cert = x509(filename)