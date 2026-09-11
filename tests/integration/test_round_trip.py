import json
from pathlib import Path

from backend.app.services.des3_service import decrypt_text, encrypt_text


vectors = json.loads((Path(__file__).parents[2] / "data/test_vectors/3des_vectors.json").read_text(encoding="utf-8"))


def test_all_vectors_round_trip_and_reference_vector():
    for vector in vectors:
        if not vector.get("valid_for_baseline", True):
            continue
        encrypted = encrypt_text(vector["plaintext"], vector["key_hex"])
        decrypted = decrypt_text(encrypted["ciphertext_hex"], vector["key_hex"])
        assert decrypted["plaintext"] == vector["plaintext"]
        if "expected_ciphertext_hex" in vector:
            assert encrypted["ciphertext_hex"] == vector["expected_ciphertext_hex"]