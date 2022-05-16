import typing

class inputOption(object):
    def __init__(self):
        self.error_message = "Ievadiet derīgu vērtību."
        self.request = "Norādiet veicamo darbību."
        self.validity_check = self._is_option_valid

    def input(self):
        option = int(input(self.request))
        return option

    def _is_option_valid(self, i: int) -> bool:
        """ Pārbauda, vai izvēlētā opcija ir derīga. """
        if i >= 1 and i <= 3:
            return True
        return False
