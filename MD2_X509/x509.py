import typing

# -- X.509 sertifikāta izgatavošanai
class x509(object):
    def __init__(self, filename: str, name: str = "Alise Linda Viļuma", signed_by: str = "Alise Linda Viļuma"):
        self._name = name
        self._signed_by = signed_by
        self._read_file(filename)

    def create(self):
        pass

    def sign(self):
        pass

    def _read_file(self, filename: str):
        pass

def main(filename: str):
    cert = x509(filename)
    cert.create()
    cert.sign()