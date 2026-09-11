from dataclasses import dataclass

from .des import decrypt_block, encrypt_block, encrypt_block_with_trace


@dataclass(frozen=True)
class DES3Stage:
    operation: str
    key_label: str
    input_bytes: bytes
    output_bytes: bytes


def split_key(key: bytes) -> tuple[bytes, bytes, bytes]:
    if len(key) != 24:
        raise ValueError("3DES keys must be exactly 24 bytes")
    return key[:8], key[8:16], key[16:]


def _transform(data: bytes, key: bytes, operation: str) -> bytes:
    transform = encrypt_block if operation == "DES_ENCRYPT" else decrypt_block
    return b"".join(transform(data[index:index + 8], key) for index in range(0, len(data), 8))


def encrypt(data: bytes, key: bytes) -> tuple[bytes, list[DES3Stage]]:
    k1, k2, k3 = split_key(key)
    stages = []
    current = data
    for operation, label, stage_key in (("DES_ENCRYPT", "K1", k1), ("DES_DECRYPT", "K2", k2), ("DES_ENCRYPT", "K3", k3)):
        output = _transform(current, stage_key, operation)
        stages.append(DES3Stage(operation, label, current, output))
        current = output
    return current, stages


def decrypt(data: bytes, key: bytes) -> tuple[bytes, list[DES3Stage]]:
    k1, k2, k3 = split_key(key)
    stages = []
    current = data
    for operation, label, stage_key in (("DES_DECRYPT", "K3", k3), ("DES_ENCRYPT", "K2", k2), ("DES_DECRYPT", "K1", k1)):
        output = _transform(current, stage_key, operation)
        stages.append(DES3Stage(operation, label, current, output))
        current = output
    return current, stages