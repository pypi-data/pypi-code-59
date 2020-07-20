import xmlsec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import load_pem_x509_certificate


class Certificate:
    def __init__(self, private_key=None, certificate=None, password=None):
        if private_key:
            self.key = xmlsec.Key.from_memory(
                private_key, xmlsec.KeyFormat.PEM, password
            )
            self.key.load_cert_from_memory(certificate, xmlsec.KeyFormat.PEM),
            self.key.name = self._certificate_fingerprint(certificate)

        elif certificate:
            self.key = xmlsec.Key.from_memory(certificate, xmlsec.KeyFormat.CERT_PEM)
            self.key.name = self._certificate_fingerprint(certificate)

    def _certificate_fingerprint(self, value) -> str:
        """Return the fingerprint of a certificate.

        A fingerprint is a sha1 hash in hex.
        """
        x509 = load_pem_x509_certificate(value, default_backend())
        return x509.fingerprint(hashes.SHA1()).hex()
