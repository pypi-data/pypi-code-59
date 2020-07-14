import hashlib
import nacl.pwhash.argon2id
from itertools import cycle, islice
from functools import reduce

HASH_VERSION_MD5 = 0
HASH_VERSION_SHA256 = 1
HASH_VERSION_ARGON2ID13 = 2

algo = {
    HASH_VERSION_MD5: "md5",
    HASH_VERSION_SHA256: "sha256",
}

SODIUM_CRYPTO_PWHASH_SALTBYTES = 16


def do_hash(version, data, salt):
    if version == HASH_VERSION_ARGON2ID13:
        salt = bytes(islice(cycle(salt.encode()), 0, nacl.pwhash.argon2id.SALTBYTES))
        return nacl.pwhash.argon2id.kdf(
            32,
            data.encode(),
            salt,
            nacl.pwhash.argon2id.OPSLIMIT_INTERACTIVE,
            nacl.pwhash.argon2id.MEMLIMIT_INTERACTIVE,
        ).hex()

    hasher = hashlib.new(algo[version])
    hasher.update(salt.encode() + data.encode())
    return hasher.hexdigest()


def _explode_hash(hash_):
    hash_, salt, version = hash_.split(":", 2)
    if not version:
        version = "1"
    versions = list(map(int, version.split(":")))
    return hash_, salt, versions


def verify(password, hash_):
    recreated = password
    hash_, salt, versions = _explode_hash(hash_)
    password_hash = reduce(lambda h, v: do_hash(v, h, salt), versions, password)

    return password_hash == hash_
