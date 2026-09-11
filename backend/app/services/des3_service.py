from ..crypto.des3 import decrypt as des3_decrypt
from ..crypto.des3 import encrypt as des3_encrypt
from .padding import pkcs7_pad, pkcs7_unpad
from .trace_service import format_stages
from .validation import parse_ciphertext, parse_key, validate_plaintext


def encrypt_text(plaintext: str, key_hex: str) -> dict[str, object]:
    validate_plaintext(plaintext)
    key = parse_key(key_hex)
    raw = plaintext.encode("utf-8")
    padded = pkcs7_pad(raw)
    ciphertext, stages = des3_encrypt(padded, key)
    return {
        "operation": "encrypt",
        "block_size_bytes": 8,
        "key_size_bytes": 24,
        "padding": {"scheme": "PKCS7", "block_size_bytes": 8, "original_length_bytes": len(raw), "padded_length_bytes": len(padded), "padding_bytes": len(padded) - len(raw)},
        "stages": format_stages(stages),
        "ciphertext_hex": ciphertext.hex(),
        "trace_available": True,
    }


def decrypt_text(ciphertext_hex: str, key_hex: str) -> dict[str, object]:
    ciphertext = parse_ciphertext(ciphertext_hex)
    key = parse_key(key_hex)
    padded, stages = des3_decrypt(ciphertext, key)
    plaintext_bytes = pkcs7_unpad(padded)
    try:
        plaintext = plaintext_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("Recovered plaintext is not valid UTF-8.") from error
    return {
        "operation": "decrypt",
        "block_size_bytes": 8,
        "key_size_bytes": 24,
        "stages": format_stages(stages),
        "plaintext": plaintext,
        "padding_removed": True,
    }