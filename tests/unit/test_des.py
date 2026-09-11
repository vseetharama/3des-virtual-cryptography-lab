from backend.app.crypto.des import decrypt_block, encrypt_block, generate_round_keys


def test_des_known_vector_and_inverse():
    key = bytes.fromhex("133457799BBCDFF1")
    block = bytes.fromhex("0123456789ABCDEF")
    ciphertext = encrypt_block(block, key)
    assert ciphertext.hex() == "85e813540f0ab405"
    assert decrypt_block(ciphertext, key) == block


def test_des_key_schedule_has_sixteen_round_keys():
    assert len(generate_round_keys(bytes.fromhex("133457799BBCDFF1"))) == 16