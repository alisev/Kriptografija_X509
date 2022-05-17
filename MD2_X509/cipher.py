import typing

# -- Iekodē un dekodē ziņojumus.
class cipher(object):
    def __init__(self, filename: str): # TODO VISS
        self._read_file(filename)
        self._certificate = None
        self._message = None

    def decrypt(self):
        """ Dekodē ziņojumu. """
        pass

    def encrypt(self):
        """ Iekodē ziņojumu. """
        pass

    def _read_file(self, filename: str):
        """ Nolasa failu ar nepieciešamo informāciju """
        pass

def main(filename: str):
    cip = cipher(filename)
