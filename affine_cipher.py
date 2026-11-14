from math import gcd
from string import ascii_lowercase

M = len(ascii_lowercase)
GROUP_SIZE = 5


def _check_coprime(a):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")


def _mmi(a):
    for x in range(1, M):
        if (a * x) % M == 1:
            return x
    raise ValueError("a and m must be coprime.")


def encode(plain_text, a, b):
    _check_coprime(a)
    result = []
    for char in plain_text.lower():
        if char.isdigit():
            result.append(char)
        elif char.isalpha():
            i = ord(char) - ord("a")
            result.append(chr((a * i + b) % M + ord("a")))
    encoded = "".join(result)
    return " ".join(
        encoded[i : i + GROUP_SIZE] for i in range(0, len(encoded), GROUP_SIZE)
    )


def decode(ciphered_text, a, b):
    _check_coprime(a)
    a_inv = _mmi(a)
    result = []
    for char in ciphered_text.lower():
        if char.isdigit():
            result.append(char)
        elif char.isalpha():
            y = ord(char) - ord("a")
            result.append(chr((a_inv * (y - b)) % M + ord("a")))
    return "".join(result)
