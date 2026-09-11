from dataclasses import dataclass

from .des_tables import E, FP, IP, P, PC1, PC2, ROTATIONS, S_BOXES


def _permute(value: int, table: tuple[int, ...], input_bits: int) -> int:
    result = 0
    for position in table:
        result = (result << 1) | ((value >> (input_bits - position)) & 1)
    return result


def _left_rotate(value: int, amount: int, width: int) -> int:
    return ((value << amount) | (value >> (width - amount))) & ((1 << width) - 1)


def generate_round_keys(key: bytes) -> list[int]:
    if len(key) != 8:
        raise ValueError("DES keys must be exactly 8 bytes")
    permuted = _permute(int.from_bytes(key, "big"), PC1, 64)
    left, right = permuted >> 28, permuted & ((1 << 28) - 1)
    keys = []
    for rotation in ROTATIONS:
        left = _left_rotate(left, rotation, 28)
        right = _left_rotate(right, rotation, 28)
        keys.append(_permute((left << 28) | right, PC2, 56))
    return keys


def _feistel(right: int, round_key: int) -> int:
    expanded = _permute(right, E, 32)
    mixed = expanded ^ round_key
    substituted = 0
    for index in range(8):
        chunk = (mixed >> (42 - index * 6)) & 0x3F
        row = ((chunk >> 5) << 1) | (chunk & 1)
        column = (chunk >> 1) & 0x0F
        substituted = (substituted << 4) | S_BOXES[index][row][column]
    return _permute(substituted, P, 32)


@dataclass(frozen=True)
class DESRound:
    round: int
    left_hex: str
    right_hex: str
    round_key_hex: str


def encrypt_block_with_trace(block: bytes, key: bytes, decrypt: bool = False) -> tuple[bytes, list[DESRound]]:
    if len(block) != 8:
        raise ValueError("DES blocks must be exactly 8 bytes")
    round_keys = generate_round_keys(key)
    if decrypt:
        round_keys = list(reversed(round_keys))
    state = _permute(int.from_bytes(block, "big"), IP, 64)
    left, right = state >> 32, state & 0xFFFFFFFF
    rounds = []
    for index, round_key in enumerate(round_keys, 1):
        left, right = right, left ^ _feistel(right, round_key)
        rounds.append(DESRound(index, f"{left:08x}", f"{right:08x}", f"{round_key:012x}"))
    result = _permute((right << 32) | left, FP, 64).to_bytes(8, "big")
    return result, rounds


def encrypt_block(block: bytes, key: bytes) -> bytes:
    return encrypt_block_with_trace(block, key)[0]


def decrypt_block(block: bytes, key: bytes) -> bytes:
    return encrypt_block_with_trace(block, key, decrypt=True)[0]