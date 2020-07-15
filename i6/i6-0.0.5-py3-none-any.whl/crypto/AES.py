import os
import cryptography
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class AES():
    """
        A simple AES GCM interface.

        Example
        ```
        aes = AES()

        ct = aes.encrypt('hello')
        
        print(ct)
        print(aes.decrypt(ct))
        ```
    """


    def __init__(self, key = None, aad = None, nonce = None):
        if key is None:
            self.__key = AESGCM.generate_key(bit_length=256)
        else:
            self.__key = key

        if aad is None:
            self.__aad = os.urandom(32)
        else:
            self.__aad = aad
        
        if nonce is None:
            self.__nonce = os.urandom(12)
        else:
            self.__nonce = nonce
        
        self.__suite = AESGCM(self.__key)

    def encrypt(self, data):
        """
            Encrypt data.
            
            Example
            ```
            aes = AES()

            ct = aes.encrypt('hello')
            
            print(ct)
            ```
        """

        if isinstance(data, str):
            data = data.encode()
        return self.__suite.encrypt(self.__nonce, data, self.__aad)

    def decrypt(self, data):
        """
            Decrypt data.
            
            Example
            ```
            aes = AES()

            ct = aes.encrypt('hello')
            
            print(aes.decrypt(ct))
            ```
        """

        try:
            return self.__suite.decrypt(self.__nonce, data, self.__aad).decode()
        except UnicodeDecodeError:
            return self.__suite.decrypt(self.__nonce, data, self.__aad)
