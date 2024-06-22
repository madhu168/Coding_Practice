class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        ans = self.myPow(x,n//2)
        if n%2 == 1:
            return ans * ans * x
        return ans * ans