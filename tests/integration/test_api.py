from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)
KEY = "133457799bbcdff11234567890abcdef23456789abcdef01"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_encrypt_and_decrypt_endpoints():
    encrypted = client.post("/api/v1/encrypt", json={"plaintext": "YashSeetha", "key_hex": KEY})
    assert encrypted.status_code == 200
    assert encrypted.json()["ciphertext_hex"] == "991c790a7768e0ff79f9e9c86b5f8f2e"
    assert len(encrypted.json()["stages"]) == 3
    decrypted = client.post("/api/v1/decrypt", json={"ciphertext_hex": encrypted.json()["ciphertext_hex"], "key_hex": KEY})
    assert decrypted.status_code == 200
    assert decrypted.json()["plaintext"] == "YashSeetha"


def test_invalid_requests_return_controlled_errors():
    response = client.post("/api/v1/encrypt", json={"plaintext": "Hello", "key_hex": "bad"})
    assert response.status_code == 400
    assert "traceback" not in response.text.lower()
    response = client.post("/api/v1/decrypt", json={"ciphertext_hex": "abc", "key_hex": KEY})
    assert response.status_code == 400