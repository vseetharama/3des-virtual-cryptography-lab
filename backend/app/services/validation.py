import re


KEY_PATTERN = re.compile(r"^[0-9a-fA-F]{48}$")


def parse_key(key_hex: str) -> bytes:
    if not isinstance(key_hex, str) or not KEY_PATTERN.fullmatch(key_hex):
        raise ValueError("Key must contain exactly 48 hexadecimal characters (24 bytes).")
    return bytes.fromhex(key_hex)


def parse_ciphertext(ciphertext_hex: str) -> bytes:
    if not isinstance(ciphertext_hex, str) or not ciphertext_hex:
        raise ValueError("Ciphertext must be a non-empty hexadecimal value.")
    if len(ciphertext_hex) % 2 or not re.fullmatch(r"[0-9a-fA-F]+", ciphertext_hex):
        raise ValueError("Ciphertext must contain an even number of hexadecimal characters.")
    value = bytes.fromhex(ciphertext_hex)
    if len(value) % 8:
        raise ValueError("Ciphertext length must be a multiple of 8 bytes.")
    return value


def validate_plaintext(plaintext: str) -> None:
    if not isinstance(plaintext, str) or not plaintext:
        raise ValueError("Plaintext must be a non-empty string.")
    try:
        plaintext.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ValueError("Plaintext must be valid UTF-8 text.") from error