from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    ans = {}
    ans_l = []
    for i in range(n):
        if edges[i] in ans:
            ans[edges[i]] = ans[edges[i]] + 1
        else:
            ans[edges[i]] = 1
    for i in range(1,n+1):
        if i in ans:
            ans_l.append(ans[i])
        else:
            ans_l.append(0)
    return ans_l