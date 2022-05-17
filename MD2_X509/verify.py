import typing

class verifier(object):
    def __init__(self, filename):
        self.certificate = self._read_file(filename) # TODO var mainīties

    def verify(self) -> bool:
        """ Veic nepieciešamās darbības, lai noteiktu, vai sertifikāts ir derīgs. """
        sub = self._verify_subject()
        key = self._verify_key()
        if sub and key:
            return True
        return False

    def _read_file(self, filename: str): # TODO
        """ Nolasa sertifikātu. """
        pass

    def _verify_subject(self) -> bool:
        """ Salīdzina sertifikātā norādīto izdēvēju ar sertifikāta turētāju. """
        if self.certificate.issuer == self.ceritifcate.subject:
            return True
        return False

    def _verify_key(self) -> bool: # TODO
        """ Nosaka, vai sertifikāta paraksts atbilst publiskajai atslēgai. """
        return False

def main(filename: str):
    ver = verifier(filename)
    ver.verify()