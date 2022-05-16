import typing
import os

class inputFilename(object):
    def __init__(self):
        self.error_message = "Fails neeksistē."
        self.request = "Norādiet faila nosaukumu."
        self.validity_check = self._is_file_valid

    def input(self):
        filename = str(input(self.request))
        return filename

    def _is_file_valid(self, filename: str) -> bool:
        """ Pārbauda, vai dotais fails eksistē. """
        if os.path.exists(filename):
            return True
        return False