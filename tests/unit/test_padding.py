import pytest

from backend.app.services.padding import pkcs7_pad, pkcs7_unpad


@pytest.mark.parametrize("length,padding", [(1, 7), (7, 1), (8, 8), (9, 7), (16, 8), (17, 7)])
def test_padding_boundaries(length, padding):
    padded = pkcs7_pad(b"a" * length)
    assert len(padded) - length == padding
    assert pkcs7_unpad(padded) == b"a" * length


def test_invalid_padding_is_rejected():
    with pytest.raises(ValueError):
        pkcs7_unpad(b"1234567\x02")