def Base(base=10, num=0):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'  # Maximum Base here is 36
    x = num % base
    rest = num // base
    if rest == 0:
        return digits[x]
    return Base(base, rest) + digits[x]
