import typing

class verifier(object):
    def __init__(self, filename):
        self._read_file(filename)
        self.certificate = None

    def verify(self) -> bool:
        sub = self._verify_subject()
        key = self._verify_key()
        if sub and key:
            return True
        return False

    def _read_file(self, filename: str):
        pass

    def _verify_subject(self) -> bool:
        return False

    def _verify_key(self) -> bool:
        return False

def main(filename: str):
    ver = verifier(filename)
    ver.verify()