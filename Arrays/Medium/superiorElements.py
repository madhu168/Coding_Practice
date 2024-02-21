from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    ans = []
    ans.append(a[-1])
    max_ele = a[-1]
    for i in range(len(a)-2,-1,-1):
        if a[i] > max_ele:
            ans.append(a[i])
            max_ele = a[i]
    return ans