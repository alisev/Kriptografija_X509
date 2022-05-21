from cryptography import x509
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PublicFormat
import typing

def read_certificate(filename: str) -> x509.Certificate:
    """ Nolasa sertifikāta failu. """
    with open(filename, "rb") as f:
        pem_data = f.read()
    cert = x509.load_pem_x509_certificate(pem_data)
    return cert

def read_private_key(filename: str): # TODO
    """ Nolasa privāto atslēgu. """
    with open(filename, "rb") as f:
        pem_data = f.read()
    key = load_pem_private_key(pem_data, password = None) # TODO izlemt, kā tiks veidota parole, ja vispār tiek veidota.
    return key

def read_text_file(filename: str):
    """ Nolasa parastu teksta failu. """
    with open(filename, "rb") as f:
        data = f.read()
    return data