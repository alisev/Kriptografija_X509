from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

from datetime import datetime
import json
import sys
import typing

from name import Name
    
# -- Sagatavo vēl neparakstītu sertifikātu.
class TBScertificate(object):
    _exponent = 65537
    _issuer = {
        "C": "LV",
	    "O": "AV17098",
	    "OU": "Root CA",
        "DN": "Alise Linda Viluma",
	    "CN": "Alise Linda Viluma"
        }
    _public_key_length = 2048
    _time_base = datetime(2022, 5, 15)
    _valid_digest = {'SHA-3': hashes.SHA256()}
    _valid_signer = {'RSA': rsa.generate_private_key}

    def __init__(self, filename: str):
        # Obligātie lauki
        self.version = None
        self.serial_number = None
        self.signature = None
        self.issuer = None
        self.validity = None
        self.subject = None
        self.subject_public_key = None
        # Neobligātie lauki
        self.extensions = None # v3
        self.unique_identifier = None # v2
        # Iestata laukus
        self._read_file(filename)

    def build(self) -> x509.CertificateBuilder:
        """ Izgatavo sertifikātu. """
        subject_attribute = self.subject.build_name_attribs()
        issuer_attribute = self.issuer.build_name_attribs()

        builder = x509.CertificateBuilder()
        builder = builder.subject_name(x509.Name(subject_attribute))
        builder = builder.issuer_name(x509.Name(issuer_attribute))
        builder = builder.not_valid_before(self.validity['notBefore'])
        builder = builder.not_valid_after(self.validity['notAfter'])
        builder = builder.serial_number(self.serial_number)
        builder = builder.public_key(self.subject_public_key['subject_public_key'])
        if self.version == 2: # TODO
            raise NotImplementedError("TODO: Pievienot extensions.")
        if self.version >= 1:
            raise NotImplementedError("TODO: Pievienot unique identifier.")
        return builder

    def get_hash_algorithm(self):
        """ Funkcija, kas atgriež vajadzīgo hash algoritmu. """
        algorithm_name = self.signature['hash']
        algorithm = self._valid_digest[algorithm_name]
        return algorithm

    def get_public_key_algorithm(self):
        """ Funkcija, kas atgriež vajadzīgo paraksta algoritmu. """
        algorithm_name = self.signature['public']
        algorithm = self._valid_signer[algorithm_name]
        return algorithm

    def _is_seconds_field_valid(self, date: datetime) -> bool:
        """ Pārbauda, vai sekunžu vērtība ir derīga. """
        if date.strftime("%S") != "00":
            return True
        return False

    def _read_file(self, filename: str):
        """ Nolasa no faila informāciju, ar kuru aizpildīt sertifikātu. """
        with open(filename) as file:
            data = json.load(file)
        self.serial_number = self._set_serial_num()
        self.signature = self._set_signature_method(data['signature'])
        self.issuer = Name(self._issuer)
        self.validity = self._set_validity()
        self.subject = self._set_subject(data['subject'])
        self.subject_public_key = self._set_subject_public_key() # TODO
        # TODO Lauki extensions un unique_identifier pašlaik netiek speciāli apstrādāti.
        if 'extensions' in data:
            self.extensions = data['extensions']
        if 'unique_id' in data:
            self.unique_identifier = data['unique_id']
        self.version = self._set_version()

    def _set_serial_num(self) -> int:
        """ Aprēķina sertifikāta sērijas numuru, izmantojot laika vērtību, kad programma tika veidota un vērtību, kad tika piekļūts šai funkcijai. """
        now = datetime.now()
        try:
            value = int((now - self._time_base).total_seconds())
            if value <= 0:
                raise ValueError("Sērijas numuram ir jābūt pozitīvam skaitlim.")
        except Exception as e:
            print(e)
            sys.exit(1)
        return value

    def _set_signature_method(self, method: list) -> dict:
        """ Pārbauda, vai norādītā paraksta metode ir derīga. """
        try:
            if method[0] in self._valid_signer and method[1] in self._valid_digest:
                return {'public': method[0],
                        'hash': method[1],
                        'str': "{}With{}Encryption".format(method[0], method[1])}
            else:
                raise ValueError("Failā ir norādīts neatbalstīts paraksta algoritms.")
        except Exception as e:
            print(e)
            sys.exit(1)

    def _set_subject(self, data: dict):
        """ Iestata informāciju par lietotāju. """
        subject = Name(data)
        if not subject._check_subject(self.issuer):
            raise Exception('Norādītā lietotāja datiem ir jāsakrīt ar izdēvēja.')
        return subject

    def _set_subject_public_key(self) -> dict:
        """ Iestata informāciju par publisko atslēgu. """
        algorithm_name = self.signature['str']
        algorithm = self.get_public_key_algorithm()
        private_key = algorithm(
            public_exponent = self._exponent,
            key_size = self._public_key_length
            )
        public_key = private_key.public_key()
        return {'algorithm': algorithm_name,
                'subject_public_key': public_key,
                'subject_private_key': private_key
                }

    def _set_validity(self) -> dict:
        """ Ievada sertifikāta derīguma termiņu. Izmanto YYMMDDHHMMSSZ formātu.
            Gadījumā, ja sekunžu vērtība ir 00, tā tiek nomainīta uz 01, lai sertifikāts būtu derīgs."""
        _format = "%Y%m%d%H%M%SZ"
        _valid_years = 50
        today = datetime.today()
        if not self._is_seconds_field_valid(today):
            today = today.replace(seconds = 1)
        until = today.replace(year = _valid_years + today.year)
        valid_from_str = today.strftime(_format)
        valid_until_str = until.strftime(_format)
        return {'notBefore': today,
                'notAfter': until,
                'notBeforeStr': valid_from_str,
                'notAfterStr': valid_until_str}

    def _set_version(self) -> int:
        """ Piešķir atbilstošo versijas vērtību. """
        if self.extensions != None:
            return 2
        elif self.unique_identifier != None:
            return 1
        return 0