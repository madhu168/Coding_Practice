class Solution:
    def my_pow(self, base: int, exponent: int) -> int:
        modulo = (10 ** 9) + 7
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulo
            base = (base * base) % modulo
            exponent //= 2
        return result 
    def countGoodNumbers(self, n: int) -> int:
        modulo = (10 ** 9) + 7
        return (self.my_pow(5, (n+1)//2) * self.my_pow(4, n//2)) % modulo
        