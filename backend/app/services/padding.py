def pkcs7_pad(data: bytes, block_size: int = 8) -> bytes:
    if block_size <= 0 or block_size >= 256:
        raise ValueError("Invalid block size")
    amount = block_size - (len(data) % block_size)
    return data + bytes([amount]) * amount


def pkcs7_unpad(data: bytes, block_size: int = 8) -> bytes:
    if not data or len(data) % block_size:
        raise ValueError("Invalid PKCS#7 padded data length.")
    amount = data[-1]
    if amount < 1 or amount > block_size or data[-amount:] != bytes([amount]) * amount:
        raise ValueError("Invalid PKCS#7 padding.")
    return data[:-amount]