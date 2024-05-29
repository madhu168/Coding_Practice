class Solution:
    def largestOddNumber(self, num: str) -> str:
        num1 = num
        n = len(num)
        num1 = num1[::-1]
        for i in range(len(num1)):
            if int(num1[i]) % 2 != 0:
                return num[:n-i]
        return ""