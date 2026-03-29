def encode_base62(num: int) -> str:
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if num == 0:
        return chars[0]

    result = []

    while num > 0:
        remainder = num % 62
        result.append(chars[remainder])
        num //= 62

    return ''.join(reversed(result))