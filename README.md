# 3DES Virtual Cryptography Laboratory

An academic browser-based visualization of Triple DES EDE using a 24-byte hexadecimal key, DES's 8-byte block size, PKCS#7 padding, and ECB mode. It is intentionally a legacy demonstration, not a production cryptographic service.

## Run locally

```powershell
python -m pip install -r backend/requirements.txt
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`. The API is documented at `/docs` during development.

## Test

```powershell
python -m pytest -q
```

## Docker

```powershell
docker build -t 3des-virtual-lab .
docker run --rm -p 8000:8000 3des-virtual-lab
```

## API

- `GET /health`
- `POST /api/v1/encrypt` with `plaintext` and `key_hex`
- `POST /api/v1/decrypt` with `ciphertext_hex` and `key_hex`

Stage values are computed by the educational DES implementation. Tests independently compare the 3DES result with PyCryptodome.