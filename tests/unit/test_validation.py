import pytest

from backend.app.services.validation import parse_ciphertext, parse_key, validate_plaintext


def test_valid_key():
    assert len(parse_key("00" * 24)) == 24


@pytest.mark.parametrize("value", ["", "00", "z" * 48, "0" * 50])
def test_invalid_key(value):
    with pytest.raises(ValueError):
        parse_key(value)


@pytest.mark.parametrize("value", ["", "abc", "zz", "00"])
def test_invalid_ciphertext(value):
    with pytest.raises(ValueError):
        parse_ciphertext(value)


def test_empty_plaintext_is_rejected():
    with pytest.raises(ValueError):
        validate_plaintext("")