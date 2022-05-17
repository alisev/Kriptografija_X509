import Crypto
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA

import typing

import tbscertificate as tbs

"""
   Users of a public key require confidence that the associated private
   key is owned by the correct remote subject (person or system) with
   which an encryption or digital signature mechanism will be used.
   This confidence is obtained through the use of public key
   certificates, which are data structures that bind public key values
   to subjects.  The binding is asserted by having a trusted CA
   digitally sign each certificate.  The CA may base this assertion upon
   technical means (a.k.a., proof of possession through a challenge-
   response protocol), presentation of the private key, or on an
   assertion by the subject.  A certificate has a limited valid
   lifetime, which is indicated in its signed contents.  Because a
   certificate's signature and timeliness can be independently checked
   by a certificate-using client, certificates can be distributed via
   untrusted communications and server systems, and can be cached in
   unsecured storage in certificate-using systems.
"""

# -- X.509 sertifikāta izgatavošanai
class x509(object):
    def __init__(self, filename: str):
        self.TBScertificate = None
        self.signature_algorithm = None
        self.signature_value = None
        self.create(filename)

    def create(self, filename: str):
        """ Izgatavo sertifikātu. """
        self.TBScertificate = tbs.TBScertificate(filename)
        self.signature_algorithm = self._set_signature_algorithm()
        self.signature_value = self._compute_signature_value()

    def _compute_signature_value(self) -> bytes:
        """ Aprēķina paraksta vērtību. """

        """
        This signature value is encoded as a BIT STRING and included in the
        signature field. The details of this process are specified for each
        of the algorithms listed in [RFC3279], [RFC4055], and [RFC4491].

        By generating this signature, a CA certifies the validity of the
        information in the tbsCertificate field. In particular, the CA
        certifies the binding between the public key material and the subject
        of the certificate.
        """
        pass

    def _set_signature_algorithm(self) -> dict:
        """ Iestata informāciju par paraksta algoritmu. """
        params = []
        return {'algorithm': self.TBScertificate.signature,
                'parameters': params}

def main(filename: str):
    cert = x509(filename)