def encode(plain: str) -> list:
    return [ord(elem) - 96 for elem in plain]
def decode(encoded: list) -> str:
    return "".join(chr(elem + 96) for elem in encoded)
