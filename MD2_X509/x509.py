import typing
import tbscertificate as tbs

# -- X.509 sertifikāta izgatavošanai
class x509(object):
    def __init__(self, filename: str):
        self.TBScertificate = None
        self.signature_algorithm = None
        self.signature_value = None
        self._create(filename)

    def _create(self, filename: str):
        """ Izgatavo sertifikātu. """
        self.TBScertificate = tbs.TBScertificate(filename)
        self.signature_algorithm = self._set_signature_algorithm() # TODO funkcija
        self.signature_value = self._set_signature_value() # TODO funkcija

    def _set_signature_algorithm(self) -> dict:
        """ Iestata informāciju par paraksta algoritmu. """
        params = [] # TODO var būt nepieciešamība iegūt un norādīt papildus parametrus.
        return {'algorithm': self.TBScertificate.signature,
                'parameters': params}

    def _set_signature_value(self) -> bytes:
        """ Aprēķina paraksta vērtību. """
        signature = None # TODO jāaprēķina
        return signature

def main(filename: str):
    cert = x509(filename)