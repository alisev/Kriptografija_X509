from cryptography.x509 import NameAttribute
from cryptography.x509.oid import NameOID
import typing

# -- Name klase, kas tiek izmantota, lai aprakstītu sertifikāta izdēvēju un lietotāju.
class Name(object):
    _identifiers = {
        'C': NameOID.COUNTRY_NAME,
        'O': NameOID.ORGANIZATION_NAME,
        'OU': NameOID.ORGANIZATIONAL_UNIT_NAME,
        'DN': NameOID.DN_QUALIFIER,
        'S': NameOID.JURISDICTION_STATE_OR_PROVINCE_NAME,
        'CN': NameOID.COMMON_NAME,
        'SN': NameOID.SERIAL_NUMBER
        }

    def __init__(self, data: dict):
        self.data = None
        self._set_data(data)

    def build_name_attribs(self) -> list:
        """ Pārveido objektu par NameAttribute. """
        fields = []
        for attrib in self.data:
            field = NameAttribute(self._identifiers[attrib], self.data[attrib])
            fields.append(field)
        return fields

    def convert_to_string(self) -> str:
        """ Konvertē datus uz STRING formātu. Neatbalstītās vērtības tiek izlaistas. """
        base_string = "{} = {}"
        str_parts = []
        for key in self.data:
            if key in self._identifiers:
                str_part = base_string.format(key, self.data[key])
                str_parts.append(str_part)
        result = ', '.join(str_parts)
        return result

    def _check_subject(self, issuer) -> bool:
        """ Pārbauda, vai lietotājs sakrīt ar norādīto izdēvēju. """
        if self.data == issuer.data:
            return True
        return False

    def _set_data(self, data: dict):
        """ Pārbauda, vai ir aizpildīti obligātie lauki """
        if not 'DN' in data:
            raise Exception("Ievadītajos datos nav norādīta DN vērtība.")
        self.data = data