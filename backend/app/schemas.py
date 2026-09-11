from pydantic import BaseModel


class EncryptRequest(BaseModel):
    plaintext: str
    key_hex: str


class DecryptRequest(BaseModel):
    ciphertext_hex: str
    key_hex: str


class ErrorBody(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    error: ErrorBody