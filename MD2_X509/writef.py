from cryptography.hazmat.primitives import serialization

import os
import typing

# -- Izveido faila nosaukumu.
def create_filename(serial_num: int, blueprint: dict) -> str:
    filename = "{}_{}.{}".format(str(serial_num), blueprint['marker'], blueprint['extension'])
    return filename

# -- Izveido sertifikāta un atslēgas failu nosaukumus pēc noteikta formāta.
def create_filenames(serial_num: int) -> tuple:
    _filename_blueprint = {
        'certificate': {
            'extension': 'pem',
            'marker': 'CERTIFICATE'
            },
        'key': {
            'extension': 'pem',
            'marker': 'KEY'
            }
        }
    cert_filename = create_filename(serial_num, _filename_blueprint['certificate'])
    key_filename = create_filename(serial_num, _filename_blueprint['key'])
    return cert_filename, key_filename

# -- Saglabā sertifikātu.
def write_certificate_file(certificate, filename: str, folder: str = "output"):
    destination = os.path.join(folder, filename)
    with open(destination, "wb") as f:
        f.write(certificate.public_bytes(encoding = serialization.Encoding.PEM))

# -- Saglabā atslēgu.
def write_key_file(private_key, filename: str, folder: str = "output"):
    destination = os.path.join(folder, filename)
    with open(destination, "wb") as f:
        f.write(private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm = serialization.BestAvailableEncryption(b"secretmessage"),
        ))

# -- Rezultātu ierakstīšana datnē
def write_file(certificate, private_key, serial_num: int):
    filename_cert, filename_key = create_filenames(serial_num)
    write_certificate_file(certificate, filename_cert)
    write_key_file(private_key, filename_key)

