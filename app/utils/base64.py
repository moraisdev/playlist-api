import base64


def convert_string_base64(value: str) -> str:
    value64Encode = value.encode("ascii")
    base64Bytes = base64.b64encode(value64Encode)
    return base64Bytes.decode("ascii")
