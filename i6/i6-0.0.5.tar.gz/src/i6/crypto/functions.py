import i6
from i6.crypto.AES import AES

import uuid
import string
import secrets
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def password(length = 32):
    """
        Generate a random password.

        Example:
        ```
        print(i6.crypto.password())
        ```
    """

    if (length < 8) or (not isinstance(length, int)):
        raise ValueError('Password length must be larger than 8')

    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    
    return password

def sha256(data):
    """
        Returns a sha256 hash of the provided data.

        Example:
        ```
        print(i6.crypto.sha256('hello'))
        ```
    """

    if isinstance(data, str):
        data = data.encode()
    
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    return digest.finalize()

def uuid():
    """
        Returns a uuid of the current host.

        Example:
        ```
        print(i6.crypto.uuid())
        ```
    """

    return f"{i6.shell.uname()}-{uuid.UUID(int=uuid.getnode())}"

def derive_key(data, salt, length=32):
    """
    Derive key from given data and salt.

    Example:
    ```
    print(i6.crypto.derive_key(i6.crypto.uuid(), os.urandom(16)))
    ```
    """

    if isinstance(data, str):
        data = data.encode()
    if isinstance(salt, str):
        salt = salt.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(data)

def verify_key(data, key, salt, length=32):
    """
    Verify key from given data, key and salt.

    Example:
    ```
    import os

    salt = os.urandom(16)
    key = i6.crypto.derive_key(i6.crypto.uuid(), salt)
    print(i6.crypto.verify_key(i6.crypto.uuid(), key, salt))
    ```
    """

    if isinstance(data, str):
        data = data.encode()
    if isinstance(key, str):
        key = key.encode()
    if isinstance(salt, str):
        salt = salt.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    try:
        kdf.verify(data, key)
        return True
    except cryptography.exceptions.InvalidKey:
        return False
