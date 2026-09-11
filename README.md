# 3DES Virtual Cryptography Laboratory

## Project Overview

The 3DES Virtual Cryptography Laboratory is an academic browser-based virtual laboratory for Triple Data Encryption Standard (3DES/TDES). It is intended for Cryptography and Network Security coursework, laboratory demonstrations, assignments, and faculty evaluation.

The application makes Triple DES encryption and decryption visible instead of treating cryptography as a black box. In the browser, encryption accepts **plaintext only** and decryption accepts **ciphertext in hexadecimal only**. The fixed educational key is supplied internally by the frontend, so students never enter a key. The UI shows padding, DES stage order, intermediate hexadecimal values, block information, ciphertext, reverse decryption stages, and verification.

This is an educational and legacy demonstration, **not a production cryptographic service**. 3DES and the baseline ECB mode are retained for assignment continuity and are not recommended for protecting sensitive data.

## Objectives

- Implement Triple DES using the EDE construction.
- Demonstrate the DES block cipher and its 16-round Feistel foundation.
- Visualize encryption and decryption stages in a browser.
- Demonstrate PKCS#7 padding and unpadding.
- Explain block size versus key size.
- Provide a lightweight browser learning interface and REST API.
- Provide automated tests and independent PyCryptodome verification.
- Provide Docker deployment configuration.

## Key Features

- **Interactive encryption:** enter plaintext only and inspect UTF-8 encoding, PKCS#7 padding, three DES stages, intermediate values, and hexadecimal ciphertext.
- **Interactive decryption:** enter ciphertext in hexadecimal only and inspect the reverse EDE pipeline, unpadding, recovered plaintext, and verification.
- **3DES EDE visualization:** `DES Encrypt K1 -> DES Decrypt K2 -> DES Encrypt K3`.
- **Reverse visualization:** `DES Decrypt K3 -> DES Encrypt K2 -> DES Decrypt K1`.
- **PKCS#7 processing:** DES data is padded to 8-byte blocks and validated during decryption.
- **Block information:** the UI distinguishes the 24-byte key from the 8-byte/64-bit DES block size and reports ciphertext block counts.
- **Conceptual K1/K2/K3 display:** internal components are labelled without exposing actual key material.
- **Validation:** the backend validates plaintext, key format, ciphertext hexadecimal syntax, alignment, padding, and UTF-8 recovery.
- **Testing:** unit, integration, known-answer, padding, validation, round-trip, and independent reference tests are included.
- **Docker configuration:** a Python 3.11-slim image is defined for local deployment.

## 3DES Algorithm

Triple DES applies DES three times using a 24-byte key divided into three 8-byte segments:

```text
K = K1 || K2 || K3
```

Encryption:

```text
C = E(K3, D(K2, E(K1, P)))
```

Decryption:

```text
P = D(K1, E(K2, D(K3, C)))
```

`P` is padded plaintext, `C` is ciphertext, and `E`/`D` are DES encryption/decryption using the indicated internal key. DES uses an initial permutation, 16 Feistel rounds, expansion, S-box substitution, P permutation, key schedule, and final permutation. DES decryption applies round keys in reverse order.

### Encryption pipeline

```text
Plaintext -> UTF-8 -> PKCS#7 padding -> DES Encrypt K1
          -> DES Decrypt K2 -> DES Encrypt K3 -> Ciphertext
```

### Decryption pipeline

```text
Ciphertext -> DES Decrypt K3 -> DES Encrypt K2 -> DES Decrypt K1
           -> PKCS#7 unpadding -> UTF-8 plaintext
```

## Cryptographic Configuration

| Parameter | Configuration |
|---|---|
| Algorithm | Triple DES / 3DES / TDES |
| Construction | EDE: Encrypt-Decrypt-Encrypt |
| DES stages | 3 |
| 3DES key | 24 bytes / 192 bits |
| K1 | First 8 bytes / 64 bits |
| K2 | Second 8 bytes / 64 bits |
| K3 | Third 8 bytes / 64 bits |
| DES block size | 8 bytes / 64 bits |
| Padding | PKCS#7 |
| Mode | ECB |
| Plaintext encoding | UTF-8 |
| Ciphertext representation | Hexadecimal |

The **24-byte key** is the complete 3DES key. It is divided into three internal **8-byte DES key segments**, K1, K2, and K3. The **8-byte/64-bit block size** is the amount of data processed by one DES operation; it is not the key size. Ciphertext length depends on padded plaintext length and is always a multiple of 8 bytes.

## Key Configuration in the Web Laboratory

The web laboratory uses a fixed, valid 24-byte educational key internally so that students can reproduce the same demonstration consistently. Encryption accepts plaintext only. Decryption accepts ciphertext in hexadecimal only. The user does not enter a key, and the actual hexadecimal key material is not displayed or editable in the browser UI. The key is divided into three 8-byte DES key segments and derives:

```text
K1 = key[0:8]
K2 = key[8:16]
K3 = key[16:24]
```

The UI presents K1, K2, and K3 conceptually but does not display the actual hexadecimal key or individual key values. The backend API remains independently usable and accepts `key_hex` for strict validation, direct API use, and automated testing; that field is not a user-facing browser input.

## Encryption Workflow

1. Enter plaintext only in the browser; no key input is required.
2. The backend encodes it as UTF-8.
3. PKCS#7 padding expands it to a multiple of 8 bytes.
4. Padded data is processed as 64-bit DES blocks.
5. DES Encrypt K1, DES Decrypt K2, and DES Encrypt K3 are applied.
6. Hexadecimal ciphertext, intermediate values, lengths, and stages are displayed.

## Decryption Workflow

1. Select Decrypt and enter ciphertext in hexadecimal only; no key input is required.
2. The backend validates and decodes the ciphertext.
3. DES Decrypt K3, DES Encrypt K2, and DES Decrypt K1 are applied.
4. PKCS#7 padding is validated and removed.
5. The result is decoded as UTF-8.
6. Recovered plaintext and verification status are displayed.

## Example

For the browser example:

```text
Plaintext: YashSeetha
```

`YashSeetha` is 10 UTF-8 bytes. PKCS#7 adds 6 bytes because DES uses 8-byte blocks:

```text
10 bytes plaintext + 6 bytes padding = 16 bytes
16 bytes = 2 x 64-bit blocks
```

The implementation produces:

```text
Ciphertext: 991c790a7768e0ff79f9e9c86b5f8f2e
16 bytes = 128 bits = 2 blocks
```

## System Architecture

```text
Browser HTML/CSS/JS
          |
          | HTTP + JSON
          v
FastAPI REST API
          |
          v
Validation and service layer
padding, orchestration, trace formatting
          |
          v
Educational DES/3DES implementation
          |
          v
Cryptographic result and intermediate stages
          |
          v
Frontend visualization
```

The frontend owns interaction and visualization. FastAPI owns HTTP routing and schemas. Services coordinate validation, padding, key splitting, processing, and trace formatting. Crypto modules implement DES and 3DES. Requests are processed in memory; no database is used.

## Technology Stack

| Area | Technologies |
|---|---|
| Frontend | Vanilla HTML, CSS, and JavaScript modules |
| Backend | Python, FastAPI, Uvicorn, Pydantic |
| Cryptography | Educational DES/3DES implementation; PyCryptodome reference tests |
| Testing | pytest, FastAPI TestClient, HTTPX |
| Deployment | Docker, `python:3.11-slim`, Uvicorn on port 8000 |
| Storage | None; in-memory request processing |

No database, ML/RAG component, authentication system, external API, or cloud service is required.

## Project Structure

```text
.
├── backend/
│   ├── app/
│   │   ├── api/routes.py
│   │   ├── crypto/
│   │   │   ├── des.py
│   │   │   ├── des3.py
│   │   │   └── des_tables.py
│   │   ├── services/
│   │   │   ├── des3_service.py
│   │   │   ├── padding.py
│   │   │   ├── trace_service.py
│   │   │   └── validation.py
│   │   ├── config.py
│   │   ├── main.py
│   │   └── schemas.py
│   └── requirements.txt
├── frontend/
│   ├── css/style.css
│   ├── js/api.js
│   ├── js/app.js
│   ├── js/visualizer.js
│   └── index.html
├── data/test_vectors/
│   ├── 3des_vectors.json
│   └── README.md
├── tests/
│   ├── unit/test_des.py
│   ├── unit/test_des3.py
│   ├── unit/test_padding.py
│   ├── unit/test_validation.py
│   ├── integration/test_api.py
│   ├── integration/test_round_trip.py
│   └── frontend/README.md
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

## Prerequisites

- Python 3.11 or newer. The Docker image is based on Python 3.11-slim.
- pip.
- Git, if cloning the project.
- Docker Desktop or Docker Engine for container deployment.

## Local Installation

Use the repository URL assigned to your project when cloning:

```bash
git clone <repository-url>
cd <repository-directory>
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

Start from the project root:

```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`. FastAPI Swagger documentation is available at `http://localhost:8000/docs`.

## Running the Virtual Laboratory

### Encryption

1. Open the application and keep Encrypt selected.
2. Enter plaintext only, such as `YashSeetha`; do not enter a key.
3. Start encryption.
4. Inspect PKCS#7 padding and the 8-byte/64-bit block explanation.
5. Inspect K1, K2, and K3 stage labels and intermediate hexadecimal values.
6. View the final ciphertext and block count.

### Decryption

1. Select Decrypt.
2. Enter the generated ciphertext hexadecimal value only; do not enter a key.
3. Start decryption.
4. Inspect K3 decrypt, K2 encrypt, and K1 decrypt.
5. Inspect PKCS#7 unpadding.
6. View recovered plaintext and `Verification: SUCCESS`.

## API Documentation

### `GET /health`

Returns:

```json
{"status": "ok", "service": "3des-virtual-lab"}
```

These examples document the backend API. The browser laboratory does not expose `key_hex` as a user input; it supplies the fixed educational key internally.

### `POST /api/v1/encrypt`

Accepts non-empty plaintext and a strictly validated `key_hex` value:

```json
{
  "plaintext": "YashSeetha",
  "key_hex": "133457799bbcdff11234567890abcdef23456789abcdef01"
}
```

Returns operation metadata, PKCS#7 padding metadata, three stage objects, `ciphertext_hex`, and `trace_available`. Stage objects contain operation, conceptual key label, input/output hexadecimal values, and byte lengths.

### `POST /api/v1/decrypt`

Accepts aligned hexadecimal ciphertext and a strictly validated `key_hex` value:

```json
{
  "ciphertext_hex": "991c790a7768e0ff79f9e9c86b5f8f2e",
  "key_hex": "133457799bbcdff11234567890abcdef23456789abcdef01"
}
```

Returns reverse stages, recovered `plaintext`, and `padding_removed`.

The frontend does not expose an editable key input. Browser encryption input is plaintext only, and browser decryption input is ciphertext hexadecimal only. Direct API callers and tests may provide `key_hex`. FastAPI Swagger documentation is available at `/docs`.

## API Validation and Error Handling

The implementation handles missing fields, empty plaintext, invalid key length, non-hexadecimal keys, invalid or empty ciphertext, odd-length hexadecimal input, ciphertext not aligned to 8 bytes, invalid padding, and invalid recovered UTF-8.

Missing schema fields return HTTP `422`. Application input errors return HTTP `400`. Application errors use:

```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Key must contain exactly 48 hexadecimal characters (24 bytes)."
  }
}
```

Schema errors use the same top-level `error` object with code `VALIDATION_ERROR`. Tracebacks and filesystem details are not returned.

## Testing

The test suite includes:

- DES known-answer, inverse, and 16-round key schedule tests.
- 3DES key splitting, EDE order, reverse order, and PyCryptodome comparison.
- PKCS#7 boundary and invalid-padding tests.
- Key, ciphertext, and plaintext validation tests.
- Health, encryption, decryption, and API error integration tests.
- Test-vector round trips, boundary lengths, and Unicode text.

Run:

```bash
python -m pytest -q
```

The latest validated state reported 25 passing tests and two dependency deprecation warnings from the installed FastAPI/HTTPX test stack.

## Independent Cryptographic Verification

PyCryptodome is used as an independent reference implementation. Comparing the educational implementation to an established library helps detect shared algorithm, padding, block-order, and EDE mistakes that a self-comparison would not reveal.

## Docker

The Dockerfile uses `python:3.11-slim`, installs `backend/requirements.txt`, copies backend/frontend/data files, exposes port 8000, and starts Uvicorn.

```bash
docker build -t 3des-virtual-lab .
docker run --rm -p 8000:8000 3des-virtual-lab
```

Then access:

```text
http://localhost:8000
http://localhost:8000/health
```

The Docker configuration is provided, but this README does not claim a successful Docker build or runtime unless it has been executed with a running Docker Linux engine.

## Test Vectors / Dataset

- `data/test_vectors/3des_vectors.json` contains repeatable educational inputs, valid regression cases, boundary lengths, and Unicode cases.
- `data/test_vectors/README.md` describes the vector data.

## Security and Educational Limitations

- 3DES is a legacy algorithm and is not recommended for new production designs.
- DES and 3DES use a 64-bit block size, which has important limitations.
- ECB can reveal repeated-block patterns and is not suitable for sensitive data.
- The fixed educational key exists for reproducible learning only.
- No production secret-management system is provided.
- Do not use this laboratory for passwords, personal data, or production secrets.

## Learning Outcomes

Students can learn symmetric cryptography, DES, 3DES, EDE composition, Feistel processing, key size versus block size, PKCS#7 padding, encryption/decryption relationships, hexadecimal ciphertext, REST integration, and automated independent cryptographic testing.

## Future Enhancements

Possible future enhancements, not current features, include DES round-by-round visualization, Feistel round details, expansion and P-box visualizations, S-box lookup, key-schedule visualization, bit-level block views, AES comparison, and richer guided laboratory explanations.

## Git Branch Structure

The project development branches are:

- `main`: integrated project branch.
- `backend`: backend and cryptographic development history.
- `frontend`: frontend development history.
- `final-changes`: final integration and refinement history.

This README documents the branch organization only; it does not perform Git operations.

## Project Status

The project includes the educational DES/3DES implementation, 3DES EDE and reverse decryption, UTF-8 and PKCS#7 processing, FastAPI endpoints, responsive vanilla frontend, internal K1/K2/K3 visualization, structured validation errors, deterministic test vectors, independent PyCryptodome tests, and Docker configuration.

It is functionally complete as an academic virtual laboratory. Docker execution remains dependent on the local Docker engine being available.

## License / Academic Use

No `LICENSE` file is currently present, so no formal open-source license is claimed. This project is intended for academic learning, coursework, laboratory demonstration, and evaluation. Add an appropriate license separately if redistribution terms are required.
