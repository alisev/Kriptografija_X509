import typing
import os

class inputFilename(object):
    def __init__(self, request: str = "Norādiet faila nosaukumu."):
        self.error_message = "Fails neeksistē."
        self.request = request
        self.validity_check = self._is_file_valid

    def input(self):
        filename = str(input(self.request))
        return filename

    def _is_file_valid(self, filenames_str: str) -> bool:
        """ Pārbauda, vai dotais fails/faili eksistē. """
        filenames = filenames_str.split(',')
        for filename in filenames:
            if os.path.exists(filename):
                return True
        return False