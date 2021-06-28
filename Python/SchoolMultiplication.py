import math


def Mult(a, b, i=1):
    if a == 0 or b == 0:
        return 0
    bStr = str(b)
    return Mult(a, math.floor(b/10), i*10) + a*int(bStr[len(bStr)-1])*i


print(Mult(11, 110))
