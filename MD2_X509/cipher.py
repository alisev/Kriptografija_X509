import typing

class cipher(object):
    def __init__(self, filename: str):
        self._read_file(filename)
        self._certificate = None
        self._message = None

    def decrypt(self):
        pass

    def encrypt(self):
        pass

    def _read_file(self, filename: str):
        pass

def main(filename: str):
    cip = cipher(filename)
