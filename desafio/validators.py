import re


def is_valid_categoria_titulo(value) -> bool:
    return bool(value.strip())


def is_valid_cor(value) -> bool:
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    return bool(re.match(pattern, value))
