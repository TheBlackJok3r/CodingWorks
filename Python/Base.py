def Base(base=10, num=0):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'  # Maximum Base here is 36
    x = num % base
    rest = num // base
    if rest == 0:
        return digits[x]
    return Base(base, rest) + digits[x]



# works only with lowercase letters
def BaseToDec(num, fromBase):
    a = 0
    for i in num:
        a *= fromBase
        b = ord(i)
        if b > 57:
            a += int(b-87)
        else:
            a += int(chr(b))
    return a
