from Crypto.Cipher import DES3

from backend.app.crypto.des3 import decrypt, encrypt, split_key
from backend.app.services.padding import pkcs7_pad


def test_key_split():
    key = bytes(range(24))
    assert split_key(key) == (key[:8], key[8:16], key[16:])


def test_3des_matches_pycryptodome():
    key = bytes.fromhex("133457799bbcdff11234567890abcdef23456789abcdef01")
    padded = pkcs7_pad(b"YashSeetha")
    actual, stages = encrypt(padded, key)
    expected = DES3.new(key, DES3.MODE_ECB).encrypt(padded)
    assert actual == expected
    assert [stage.key_label for stage in stages] == ["K1", "K2", "K3"]
    recovered, reverse_stages = decrypt(actual, key)
    assert recovered == padded
    assert [stage.key_label for stage in reverse_stages] == ["K3", "K2", "K1"]