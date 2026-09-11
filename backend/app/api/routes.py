from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..schemas import DecryptRequest, EncryptRequest
from ..services.des3_service import decrypt_text, encrypt_text

router = APIRouter()


@router.post("/encrypt")
def encrypt(request: EncryptRequest) -> dict[str, object]:
    try:
        return encrypt_text(request.plaintext, request.key_hex)
    except ValueError as error:
        return JSONResponse(status_code=400, content={"error": {"code": "INVALID_INPUT", "message": str(error)}})


@router.post("/decrypt")
def decrypt(request: DecryptRequest) -> dict[str, object]:
    try:
        return decrypt_text(request.ciphertext_hex, request.key_hex)
    except ValueError as error:
        return JSONResponse(status_code=400, content={"error": {"code": "INVALID_INPUT", "message": str(error)}})