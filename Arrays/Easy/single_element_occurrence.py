from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    ans_map = {}
    for i in range(len(arr)):
        if arr[i] in ans_map:
            ans_map[arr[i]] += 1
        else:
            ans_map[arr[i]] = 1
    ans = 0
    for i in ans_map:
        if ans_map[i] == 1:
            ans = i
    return ans