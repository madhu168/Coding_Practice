from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    a = 1
    i = 1
    ans = [1]
    while(a <= n):
        i += 1
        a = a * i
        if(a <= n):
            ans.append(a)
    return ans