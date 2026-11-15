def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    filtered = ''.join(c.lower() for c in plain_text if c.isalnum())

    encoded = []
    for c in filtered:
        if c.isdigit():
            encoded.append(c)
        else:
            i = ord(c) - ord('a')
            y = (a * i + b) % 26
            encoded.append(chr(ord('a') + y))

    result = []
    for i in range(0, len(encoded), 5):
        result.append(''.join(encoded[i:i+5]))

    return ' '.join(result)


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    a_inv = mod_inverse(a, 26)

    filtered = ''.join(c.lower() for c in ciphered_text if c.isalnum())

    decoded = []
    for c in filtered:
        if c.isdigit():
            decoded.append(c)
        else:
            y = ord(c) - ord('a')
            x = (a_inv * (y - b)) % 26
            decoded.append(chr(ord('a') + x))

    return ''.join(decoded)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y

    _, x, _ = extended_gcd(a % m, m)
    return (x % m + m) % m
