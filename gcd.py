def calcGDC(n:int, m: int) -> int:
    # Write your code here
    return gcd(n,m);


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)