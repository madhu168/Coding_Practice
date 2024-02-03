class Solution:
    def fib(self, n: int) -> int:
        if(n == 0):
            return 0
        if(n==1):
            return 1
        i = 2
        second_last = 0
        last = 1
        ans = 0
        while(i < n+1):
            ans = second_last + last
            second_last = last
            last = ans
            i = i + 1
        return ans