from ..crypto.des3 import DES3Stage


def format_stages(stages: list[DES3Stage]) -> list[dict[str, object]]:
    return [
        {
            "stage": index,
            "operation": item.operation,
            "key": item.key_label,
            "input_hex": item.input_bytes.hex(),
            "output_hex": item.output_bytes.hex(),
            "input_length_bytes": len(item.input_bytes),
            "output_length_bytes": len(item.output_bytes),
        }
        for index, item in enumerate(stages, 1)
    ]