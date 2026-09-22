# 3DES Virtual Cryptography Laboratory

## Project Report

**Course:** Cryptography and Network Security  
**Project Title:** 3DES Virtual Cryptography Laboratory  
**Student Name:** [Enter your name]  
**Register Number:** [Enter your register number]  
**Class / Semester:** [Enter class and semester]  
**Department:** [Enter department]  
**Institution:** [Enter institution name]  
**Project Guide:** [Enter guide name]  
**Academic Year:** [Enter academic year]  
**Submission Date:** [Enter date]

> This report describes the implemented educational web laboratory. The project is intended for learning and demonstration. It is not a production cryptographic service.

---

## Abstract

The 3DES Virtual Cryptography Laboratory is a browser-based educational application that demonstrates the Triple Data Encryption Standard (3DES or TDEA) using the Encrypt-Decrypt-Encrypt (EDE) construction. The application makes the internal encryption process visible instead of treating encryption as a black box. Users can enter plaintext for encryption or hexadecimal ciphertext for decryption and inspect UTF-8 conversion, PKCS#7 padding, DES stage order, intermediate hexadecimal values, block information, final output, and verification.

The system contains a vanilla HTML, CSS, and JavaScript frontend and a Python FastAPI backend. The backend validates input, performs padding and unpadding, executes the educational DES/3DES implementation, formats intermediate stages, and returns structured JSON responses. Automated unit and integration tests verify DES, 3DES, padding, validation, API behavior, round trips, test vectors, and independent PyCryptodome comparisons.

3DES and ECB mode are included for academic continuity and algorithm visualization. They are legacy choices and must not be used for protecting modern sensitive information.

**Keywords:** DES, Triple DES, 3DES, TDEA, EDE, symmetric encryption, Feistel cipher, PKCS#7, ECB, FastAPI, cryptography visualization.

---

## Table of Contents

1. Introduction  
2. Problem Statement  
3. Aim and Objectives  
4. Scope and Significance  
5. Existing and Proposed System  
6. Requirements  
7. Technology Stack  
8. System Architecture  
9. Project Structure  
10. Cryptographic Theory  
11. System Workflow  
12. Module Description  
13. Frontend Design  
14. Backend API Design  
15. Input Validation and Error Handling  
16. Implementation Details  
17. Testing and Evaluation  
18. Demonstration Example  
19. Deployment Instructions  
20. Security and Ethical Considerations  
21. Limitations  
22. Future Enhancements  
23. Conclusion  
24. References  
25. Appendix A: Commands  
26. Appendix B: Viva Questions

---

## 1. Introduction

Cryptography provides techniques for protecting information from unauthorized access and modification. Symmetric-key cryptography uses the same secret key, or related key material, for encryption and decryption. DES is a historical symmetric block cipher based on a 16-round Feistel structure. Triple DES applies DES three times to increase the effective security and useful lifetime of DES-based systems.

Although cryptographic libraries can perform encryption in a single function call, students often cannot see what occurs between the original message and the final ciphertext. This project addresses that learning problem through an interactive virtual laboratory. It shows the major stages of the 3DES EDE pipeline, the effect of padding, the distinction between key size and block size, and the reverse decryption process.

The application uses a fixed educational key in the browser workflow so that demonstrations are repeatable and the user interface remains focused on the algorithm. Direct API calls and automated tests can provide a validated hexadecimal key explicitly.

---

## 2. Problem Statement

Traditional demonstrations of encryption often display only the plaintext, key, and final ciphertext. This hides important concepts such as block processing, padding, DES stage order, intermediate values, and the relationship between encryption and decryption.

The problem addressed by this project is:

> How can Triple DES encryption and decryption be implemented as an interactive, testable, and visually understandable web laboratory that exposes the important processing stages while maintaining strict input validation?

---

## 3. Aim and Objectives

### 3.1 Aim

To develop a browser-based virtual laboratory that demonstrates Triple DES encryption and decryption and makes the internal EDE processing stages visible to students.

### 3.2 Objectives

- Implement DES and Triple DES using the EDE construction.
- Demonstrate the 16-round Feistel foundation of DES.
- Apply UTF-8 encoding to application plaintext.
- Apply and validate PKCS#7 padding for the 8-byte DES block size.
- Display the three encryption stages: `Encrypt K1`, `Decrypt K2`, and `Encrypt K3`.
- Display the reverse decryption stages: `Decrypt K3`, `Encrypt K2`, and `Decrypt K1`.
- Explain the difference between the 24-byte 3DES key and the 8-byte DES block size.
- Provide a REST API for encryption and decryption.
- Validate keys, plaintext, ciphertext syntax, block alignment, padding, and recovered UTF-8.
- Provide automated tests and independent reference verification.
- Provide a Docker configuration for local deployment.

---

## 4. Scope and Significance

### 4.1 Scope

The project covers:

- Educational DES and 3DES processing.
- 24-byte three-key 3DES configuration.
- ECB-mode block processing for demonstration.
- PKCS#7 padding and unpadding.
- Browser visualization of inputs, outputs, and intermediate stages.
- FastAPI endpoints for encryption, decryption, and health checking.
- Automated testing and repeatable test vectors.
- Local and Docker-based execution.

### 4.2 Significance

The project helps students understand:

- Symmetric encryption and decryption.
- DES block and key concepts.
- Feistel rounds and reversed round-key use during decryption.
- Triple encryption composition.
- Padding and block alignment.
- Hexadecimal ciphertext representation.
- REST API integration with a browser client.
- The importance of validation and independent testing.

---

## 5. Existing and Proposed System

### 5.1 Existing System

A basic cryptographic program normally accepts input and returns ciphertext or recovered plaintext. It may use a library call without explaining the transformations between stages. Such a program is useful for computation but provides limited visibility for classroom learning.

### 5.2 Proposed System

The proposed system is an interactive virtual laboratory with:

- A browser interface for encryption and decryption.
- A structured FastAPI backend.
- Visible PKCS#7 padding information.
- Visible DES stage order and intermediate hexadecimal data.
- Controlled validation errors.
- Known-answer, round-trip, unit, integration, and independent reference tests.
- A health endpoint and generated API documentation.
- A Docker deployment option.

---

## 6. Requirements

### 6.1 Functional Requirements

1. The system shall accept non-empty plaintext for encryption.
2. The system shall accept hexadecimal ciphertext for decryption.
3. The system shall validate a 24-byte key represented by 48 hexadecimal characters.
4. The system shall encode plaintext using UTF-8.
5. The system shall apply PKCS#7 padding to 8-byte DES blocks.
6. The system shall perform 3DES EDE encryption.
7. The system shall perform reverse 3DES decryption.
8. The system shall return ciphertext as hexadecimal text.
9. The system shall return recovered plaintext after valid decryption.
10. The system shall expose intermediate processing stages.
11. The system shall return controlled JSON errors for invalid requests.
12. The system shall provide a health-check endpoint.

### 6.2 Non-Functional Requirements

- The interface should be simple enough for classroom demonstrations.
- The implementation should be modular and maintainable.
- Requests should be processed in memory without a database.
- The API should return predictable JSON structures.
- The application should run locally on Windows, Linux, macOS, and Docker.
- The system should not expose stack traces or filesystem details to API users.
- The project should include automated tests for core behavior.

---

## 7. Technology Stack

| Area | Technology |
|---|---|
| Frontend markup | HTML5 |
| Frontend styling | CSS3 |
| Frontend behavior | Vanilla JavaScript ES modules |
| Backend language | Python 3.11 or newer |
| Web framework | FastAPI |
| ASGI server | Uvicorn |
| Data validation | Pydantic |
| Reference cryptography | PyCryptodome in independent tests |
| Testing | pytest and FastAPI TestClient |
| API client format | JSON over HTTP |
| Deployment | Docker and `python:3.11-slim` |
| Storage | None; request processing is in memory |

---

## 8. System Architecture

```text
+-----------------------------+
| Browser                     |
| HTML + CSS + JavaScript     |
| Input controls and trace UI |
+--------------+--------------+
               |
               | HTTP JSON requests
               v
+-----------------------------+
| FastAPI application         |
| /health                      |
| /api/v1/encrypt              |
| /api/v1/decrypt              |
+--------------+--------------+
               |
               v
+-----------------------------+
| Validation and service layer|
| Key parsing                 |
| Ciphertext validation       |
| UTF-8 conversion            |
| PKCS#7 padding              |
| Trace formatting            |
+--------------+--------------+
               |
               v
+-----------------------------+
| Educational DES / 3DES      |
| DES tables                  |
| DES rounds and key schedule|
| EDE and reverse EDE         |
+--------------+--------------+
               |
               v
+-----------------------------+
| JSON result and visualization|
| Ciphertext / plaintext       |
| Intermediate stages          |
| Verification information     |
+-----------------------------+
```

The frontend is served by the FastAPI application. The backend owns cryptographic processing, validation, and response generation. The frontend owns user interaction and visualization.

---

## 9. Project Structure

```text
.
|-- backend/
|   |-- requirements.txt
|   `-- app/
|       |-- config.py
|       |-- main.py
|       |-- schemas.py
|       |-- api/routes.py
|       |-- crypto/
|       |   |-- des_tables.py
|       |   |-- des.py
|       |   `-- des3.py
|       `-- services/
|           |-- des3_service.py
|           |-- padding.py
|           |-- trace_service.py
|           `-- validation.py
|-- data/test_vectors/
|   |-- 3des_vectors.json
|   `-- README.md
|-- frontend/
|   |-- index.html
|   |-- css/style.css
|   `-- js/
|       |-- api.js
|       |-- app.js
|       `-- visualizer.js
|-- tests/
|   |-- frontend/README.md
|   |-- integration/test_api.py
|   |-- integration/test_round_trip.py
|   |-- unit/test_des.py
|   |-- unit/test_des3.py
|   |-- unit/test_padding.py
|   `-- unit/test_validation.py
|-- Dockerfile
|-- README.md
`-- PROJECT_REPORT.md
```

### 9.1 Important Modules

| Module | Responsibility |
|---|---|
| `des_tables.py` | Official DES permutation, substitution, and rotation tables |
| `des.py` | DES block processing, rounds, key schedule, encryption, and decryption |
| `des3.py` | 3DES EDE composition and reverse decryption |
| `padding.py` | PKCS#7 padding and validation |
| `validation.py` | Plaintext, key, and ciphertext validation |
| `des3_service.py` | Application-level encryption and decryption orchestration |
| `trace_service.py` | Intermediate stage formatting for the frontend |
| `routes.py` | FastAPI endpoint definitions |
| `schemas.py` | Request schema definitions |
| `app.js` | Frontend form behavior and operation mode handling |
| `api.js` | Browser-to-API communication |
| `visualizer.js` | Pipeline and result rendering |

---

## 10. Cryptographic Theory

### 10.1 DES Block and Key Concepts

DES processes one 64-bit block, which is 8 bytes. The DES input key representation is 8 bytes, with 64 key bits including parity positions and a 56-bit effective key portion in the traditional DES design.

The 3DES configuration in this project uses a 24-byte key divided into three 8-byte segments:

```text
K = K1 || K2 || K3
K1 = K[0:8]
K2 = K[8:16]
K3 = K[16:24]
```

The 24-byte key is not the same thing as the 8-byte data block size.

### 10.2 DES Feistel Structure

A DES block is divided into a left half and a right half. For round `i`:

```text
L_i = R_(i-1)
R_i = L_(i-1) XOR F(R_(i-1), K_i)
```

The DES round function contains:

```text
32-bit right half
      |
      v
Expansion permutation: 32 bits -> 48 bits
      |
      v
XOR with round key
      |
      v
S-box substitution: 48 bits -> 32 bits
      |
      v
P permutation
      |
      v
32-bit round output
```

DES applies 16 Feistel rounds. Decryption uses the same structure but applies the round keys in reverse order.

### 10.3 Triple DES EDE Encryption

The required three-stage encryption pipeline is:

```text
Padded plaintext
    -> DES Encrypt K1
    -> DES Decrypt K2
    -> DES Encrypt K3
    -> Ciphertext
```

Mathematically:

```text
C = E_K3(D_K2(E_K1(P)))
```

### 10.4 Triple DES Decryption

The reverse pipeline is:

```text
Ciphertext
    -> DES Decrypt K3
    -> DES Encrypt K2
    -> DES Decrypt K1
    -> Padded plaintext
    -> PKCS#7 unpadding
    -> UTF-8 plaintext
```

Mathematically:

```text
P = D_K1(E_K2(D_K3(C)))
```

### 10.5 PKCS#7 Padding

DES requires input lengths that are multiples of 8 bytes. For block size `B = 8` and plaintext length `L`, the padding length is:

```text
p = B - (L mod B)
```

The application appends `p` bytes, each having the numeric value `p`. If the original input is already aligned, a complete block of eight `08` bytes is appended.

Examples:

| Plaintext length | Padding bytes |
|---:|---|
| 7 bytes | `01` |
| 6 bytes | `02 02` |
| 5 bytes | `03 03 03` |
| 8 bytes | `08 08 08 08 08 08 08 08` |

During decryption, the padding length and every padding byte are checked before the padding is removed.

---

## 11. System Workflow

### 11.1 Encryption Workflow

1. The user selects **Encrypt**.
2. The user enters plaintext in the browser.
3. The browser sends an encryption request to `/api/v1/encrypt`.
4. The backend validates the plaintext and key.
5. The plaintext is encoded as UTF-8 bytes.
6. PKCS#7 padding is applied to reach an 8-byte boundary.
7. DES Encrypt K1 is applied.
8. DES Decrypt K2 is applied.
9. DES Encrypt K3 is applied.
10. The ciphertext is converted to hexadecimal text.
11. The backend returns padding metadata, stage data, ciphertext, and trace status.
12. The frontend renders the pipeline and result.

### 11.2 Decryption Workflow

1. The user selects **Decrypt**.
2. The user enters hexadecimal ciphertext.
3. The browser sends a decryption request to `/api/v1/decrypt`.
4. The backend validates hexadecimal syntax and 8-byte alignment.
5. Reverse 3DES processing is performed.
6. PKCS#7 padding is validated and removed.
7. The bytes are decoded as UTF-8.
8. The backend returns the recovered plaintext and reverse stage data.
9. The frontend displays the recovered message and verification result.

### 11.3 Browser Key Behavior

The browser workflow uses a fixed valid educational key internally. The user does not enter the key in the interface. The interface presents the conceptual labels `K1`, `K2`, and `K3` without exposing the actual key material. Direct API users and tests may provide `key_hex` for controlled validation and verification.

---

## 12. Module Description

### 12.1 DES Module

The DES module contains the official DES tables and implements the core block cipher operations. It performs initial and final permutations, the 16 Feistel rounds, expansion, S-box substitution, P permutation, and round-key generation. Decryption uses reverse round-key order.

### 12.2 3DES Module

The 3DES module splits the 24-byte key into K1, K2, and K3 and applies the EDE sequence to each padded block. It also exposes the reverse sequence for decryption and records stage inputs and outputs for tracing.

### 12.3 Padding Module

The padding module applies PKCS#7 padding before encryption. It validates the final block during decryption and raises a controlled error if the padding is missing, malformed, or inconsistent.

### 12.4 Validation Module

The validation module checks:

- Plaintext is present and non-empty.
- Key is exactly 48 hexadecimal characters.
- Ciphertext is non-empty hexadecimal text.
- Ciphertext has an even number of hexadecimal characters.
- Decoded ciphertext length is aligned to 8 bytes.
- Recovered plaintext is valid UTF-8.

### 12.5 Service Layer

The service layer coordinates validation, UTF-8 conversion, padding, cryptographic processing, trace formatting, and response creation. This keeps HTTP routing separate from cryptographic and application logic.

### 12.6 Frontend Modules

The frontend provides:

- Encrypt and decrypt mode selection.
- Plaintext and ciphertext input fields.
- A reset operation.
- Pipeline stage display.
- Padding metadata display.
- Ciphertext and recovered plaintext output.
- Verification status.
- Responsive layout for classroom demonstration.

---

## 13. Frontend Design

The frontend is built with standard HTML, CSS, and JavaScript modules. It does not require a frontend build tool or database.

### 13.1 Encryption Interface

The encryption interface contains:

- Plaintext textarea with the placeholder `Enter plain text`.
- Encrypt mode selection.
- Run encryption button.
- Reset button.
- Internal key configuration explanation.
- Stage trace and result area.

### 13.2 Decryption Interface

The decryption interface contains:

- Ciphertext hexadecimal textarea.
- Decrypt mode selection.
- Run decryption button.
- Input validation messages.
- Reverse pipeline display.
- Recovered plaintext and verification status.

### 13.3 Educational Display

The interface explains that:

- The key size is 24 bytes.
- The DES block size is 8 bytes or 64 bits.
- K1, K2, and K3 are three conceptual 8-byte components.
- ECB and 3DES are shown for educational purposes and are not modern production recommendations.

**Suggested screenshot locations for the final report:**

- `[Insert Screenshot 1: Initial encryption screen]`
- `[Insert Screenshot 2: Encryption result and three stages]`
- `[Insert Screenshot 3: Decryption result and verification]`
- `[Insert Screenshot 4: FastAPI Swagger documentation]`

---

## 14. Backend API Design

The backend is a FastAPI application served by Uvicorn.

### 14.1 Health Endpoint

```http
GET /health
```

Example response:

```json
{
  "status": "ok",
  "service": "3des-virtual-lab"
}
```

### 14.2 Encryption Endpoint

```http
POST /api/v1/encrypt
Content-Type: application/json
```

Request:

```json
{
  "plaintext": "YashSeetha",
  "key_hex": "133457799bbcdff11234567890abcdef23456789abcdef01"
}
```

Response fields include:

- `operation`
- `block_size_bytes`
- `key_size_bytes`
- `padding`
- `stages`
- `ciphertext_hex`
- `trace_available`

### 14.3 Decryption Endpoint

```http
POST /api/v1/decrypt
Content-Type: application/json
```

Request:

```json
{
  "ciphertext_hex": "991c790a7768e0ff79f9e9c86b5f8f2e",
  "key_hex": "133457799bbcdff11234567890abcdef23456789abcdef01"
}
```

Response fields include:

- `operation`
- `block_size_bytes`
- `key_size_bytes`
- `stages`
- `plaintext`
- `padding_removed`

### 14.4 Error Response

Application validation errors use HTTP 400 and the following structure:

```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Key must contain exactly 48 hexadecimal characters (24 bytes)."
  }
}
```

Missing or incorrectly typed schema fields use HTTP 422 with a `VALIDATION_ERROR` code.

### 14.5 API Documentation

FastAPI automatically provides interactive documentation at:

```text
http://localhost:8000/docs
```

---

## 15. Input Validation and Error Handling

Validation is performed before cryptographic processing. This prevents malformed input from reaching the DES implementation and makes failures understandable to API users.

| Invalid condition | Expected behavior |
|---|---|
| Empty plaintext | HTTP 400 controlled error |
| Missing request field | HTTP 422 schema error |
| Key shorter or longer than 48 hex characters | HTTP 400 controlled error |
| Non-hexadecimal key | HTTP 400 controlled error |
| Empty ciphertext | HTTP 400 controlled error |
| Odd-length ciphertext | HTTP 400 controlled error |
| Non-hexadecimal ciphertext | HTTP 400 controlled error |
| Ciphertext not aligned to 8 bytes | HTTP 400 controlled error |
| Invalid PKCS#7 padding | HTTP 400 controlled error |
| Invalid recovered UTF-8 | HTTP 400 controlled error |

The API does not return tracebacks or local filesystem details.

---

## 16. Implementation Details

### 16.1 Encryption Service Logic

The encryption service performs the following logical operations:

```text
validate_plaintext(plaintext)
parse_key(key_hex)
raw = plaintext.encode("utf-8")
padded = pkcs7_pad(raw)
ciphertext, stages = des3_encrypt(padded, key)
return formatted result
```

### 16.2 Decryption Service Logic

The decryption service performs the following logical operations:

```text
ciphertext = parse_ciphertext(ciphertext_hex)
key = parse_key(key_hex)
padded, stages = des3_decrypt(ciphertext, key)
plaintext_bytes = pkcs7_unpad(padded)
plaintext = plaintext_bytes.decode("utf-8")
return formatted result
```

### 16.3 Trace Data

Each stage records the operation, conceptual key label, input hexadecimal value, output hexadecimal value, and byte lengths. This allows the frontend to display the transformation while keeping the actual internal educational key values hidden from the browser interface.

### 16.4 Data Storage

The application has no database. Input data is processed in memory during each request. The repository includes static test-vector data for repeatable testing.

---

## 17. Testing and Evaluation

### 17.1 Test Categories

The test suite contains:

- DES known-answer tests.
- DES inverse and round-key schedule tests.
- 3DES key-splitting tests.
- 3DES EDE order tests.
- Reverse decryption tests.
- PKCS#7 boundary and invalid-padding tests.
- Plaintext, key, and ciphertext validation tests.
- Health endpoint tests.
- Encryption and decryption API integration tests.
- Encryption-decryption round-trip tests.
- Test-vector tests.
- Unicode and boundary-length tests.
- Independent PyCryptodome comparison tests.

### 17.2 Test Commands

From the repository root:

```powershell
python -m pytest -q
```

### 17.3 Known Integration Check

The integration test uses the educational plaintext `YashSeetha` and a 24-byte hexadecimal key. The expected ciphertext is:

```text
991c790a7768e0ff79f9e9c86b5f8f2e
```

The test then decrypts this ciphertext and verifies that the original plaintext is recovered.

### 17.4 Test Results

The test suite was executed with the project virtual environment and completed successfully:

```text
25 passed, 2 warnings in 1.09s
```

The warnings are dependency deprecation warnings from the installed FastAPI, Starlette, HTTPX, and AnyIO test stack. They do not indicate a project test failure.

### 17.5 Evaluation Criteria

| Criterion | Evidence |
|---|---|
| Correct DES behavior | DES known-answer and inverse tests |
| Correct 3DES composition | EDE order and PyCryptodome comparison tests |
| Correct padding | Padding boundary and invalid-padding tests |
| Correct API behavior | FastAPI integration tests |
| Correct round trip | Encrypt then decrypt tests |
| Input safety | Validation tests and controlled errors |
| Educational visibility | Frontend stage and metadata display |
| Deployability | Local Uvicorn and Docker configuration |

---

## 18. Demonstration Example

### 18.1 Encryption Example

Input plaintext:

```text
YashSeetha
```

The text contains 10 UTF-8 bytes. DES uses an 8-byte block size, so PKCS#7 adds 6 bytes:

```text
10 bytes plaintext + 6 bytes padding = 16 bytes
16 bytes = 2 DES blocks
```

Using the project educational key, the expected ciphertext is:

```text
991c790a7768e0ff79f9e9c86b5f8f2e
```

The browser displays three stages:

```text
Stage 1: DES Encrypt K1
Stage 2: DES Decrypt K2
Stage 3: DES Encrypt K3
```

### 18.2 Decryption Example

The ciphertext is entered as hexadecimal text:

```text
991c790a7768e0ff79f9e9c86b5f8f2e
```

The reverse process is:

```text
Stage 1: DES Decrypt K3
Stage 2: DES Encrypt K2
Stage 3: DES Decrypt K1
```

After padding validation and removal, the recovered plaintext is:

```text
YashSeetha
```

The expected verification result is `SUCCESS`.

---

## 19. Deployment Instructions

### 19.1 Local Windows Setup

Open PowerShell in the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000
```

If PowerShell blocks virtual-environment activation for the current session:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

### 19.2 Linux or macOS Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

### 19.3 Docker Setup

Build the image:

```bash
docker build -t 3des-virtual-lab .
```

Run the container:

```bash
docker run --rm -p 8000:8000 3des-virtual-lab
```

Open:

```text
http://localhost:8000
```

Docker execution depends on Docker Desktop or a running Docker Engine.

---

## 20. Security and Ethical Considerations

This project is for education and algorithm visualization. It must not be used to protect passwords, personal data, financial data, health data, production secrets, or other sensitive information.

Important considerations:

- 3DES is a legacy algorithm and is not recommended for new systems.
- DES has a small 64-bit block size compared with modern requirements.
- ECB mode reveals repeated-block patterns.
- The fixed educational key is intentionally predictable.
- No production secret-management system is provided.
- The displayed key configuration is for repeatable learning, not secure deployment.
- Real applications should use modern authenticated encryption, such as AES-GCM or ChaCha20-Poly1305, with proper key management.

---

## 21. Limitations

- The project uses ECB mode for assignment continuity and visualization.
- The educational key is fixed in the browser workflow.
- There is no authentication or authorization system.
- There is no database or persistent storage.
- The project is not designed for production confidentiality.
- The browser does not provide round-by-round visualization for every DES Feistel round.
- Docker execution requires a working local Docker engine.
- The final report should include fresh test output and screenshots taken from the actual running application.

---

## 22. Future Enhancements

Possible future improvements include:

1. Add DES round-by-round Feistel visualization.
2. Show expansion, S-box, P-permutation, and key-schedule details.
3. Add bit-level block visualization.
4. Add an AES-GCM comparison using modern authenticated encryption.
5. Add selectable educational input vectors.
6. Add downloadable experiment reports from the browser.
7. Add a guided lesson mode with questions and explanations.
8. Add accessibility improvements and more keyboard navigation.
9. Add deployment through a secure hosting platform.
10. Add automated browser tests for frontend interactions.
11. Add a server-side configuration system for non-production demonstrations.
12. Replace the legacy demonstration mode with a modern algorithm for practical security examples.

---

## 23. Conclusion

The 3DES Virtual Cryptography Laboratory successfully combines cryptographic processing, REST API design, and browser visualization into one educational application. It demonstrates the complete 3DES EDE workflow, including UTF-8 conversion, PKCS#7 padding, DES stage sequencing, hexadecimal ciphertext, reverse decryption, and verification.

The layered architecture separates the frontend, API routes, validation, services, cryptographic primitives, and tests. This structure makes the project easier to understand, test, and extend. The automated test suite and independent reference comparisons provide evidence that the implementation follows the required algorithm and handles invalid inputs in a controlled manner.

The project meets its academic purpose as a visualization and learning tool. Because 3DES and ECB are legacy choices, the application should remain limited to classroom demonstrations and should not be used for real-world sensitive data.

---

## 24. References

1. National Institute of Standards and Technology, **Data Encryption Standard (DES)**, FIPS PUB 46-3.
2. National Institute of Standards and Technology, **Recommendation for Block Cipher Modes of Operation**, SP 800-38A.
3. FastAPI Documentation, https://fastapi.tiangolo.com/
4. Pydantic Documentation, https://docs.pydantic.dev/
5. Uvicorn Documentation, https://www.uvicorn.org/
6. PyCryptodome Documentation, https://pycryptodome.readthedocs.io/
7. Python Documentation, https://docs.python.org/3/
8. Project source code and test vectors in this repository.

---

## 25. Appendix A: Commands

### Check the Current Git Branch

```powershell
git branch --show-current
git status --short --branch
```

### Run the Application

```powershell
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run the Tests

```powershell
python -m pytest -q
```

### Check the API Health Endpoint

```powershell
Invoke-WebRequest http://localhost:8000/health
```

### Check GitHub Synchronization

```powershell
git fetch origin
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
```

---

## 26. Appendix B: Viva Questions

### Q1. What is 3DES?

3DES is a symmetric block cipher that applies the DES primitive three times, normally using the EDE sequence: encrypt with K1, decrypt with K2, and encrypt with K3.

### Q2. Why is the sequence called EDE?

The sequence contains Encrypt, Decrypt, and Encrypt operations.

### Q3. What is the DES block size?

DES processes 64-bit blocks, which is 8 bytes.

### Q4. What is the 3DES key size in this project?

The project uses a 24-byte key divided into three 8-byte components: K1, K2, and K3.

### Q5. Why is padding required?

DES processes complete 8-byte blocks. PKCS#7 padding makes arbitrary-length plaintext fit that block size.

### Q6. Why is UTF-8 handled before padding?

The cryptographic algorithm processes bytes, so application text must first be converted from characters into UTF-8 bytes.

### Q7. How does DES decryption work?

DES decryption uses the same Feistel structure but applies the generated round keys in reverse order.

### Q8. Why is ECB not recommended?

ECB encrypts equal plaintext blocks into equal ciphertext blocks, which can reveal repeated patterns.

### Q9. Why is the key hidden in the browser interface?

The fixed educational key keeps demonstrations reproducible while allowing students to focus on the algorithm. The interface presents conceptual K1, K2, and K3 labels instead of editable key material.

### Q10. What would be used in a modern production system?

A modern system should use an authenticated encryption mode such as AES-GCM or ChaCha20-Poly1305 with secure random nonces and proper secret management.

---

## Final Submission Checklist

- [ ] Replace all student and institution placeholders.
- [ ] Add the project guide and academic year.
- [ ] Run the application successfully.
- [ ] Capture frontend screenshots.
- [ ] Capture the Swagger API documentation screen.
- [ ] Run `python -m pytest -q`.
- [ ] Paste the current test output into Section 17.4.
- [ ] Confirm the example ciphertext using the running project.
- [ ] Add any institution-specific certificate or declaration pages.
- [ ] Review the report for formatting requirements before submission.
