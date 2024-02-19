from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    index = -1
    for i in range(len(A)-1,0,-1):
        if(A[i-1] < A[i]):
            index = i-1
            break
    if index == -1:
        return A[::-1]
    else:
        for i in range(len(A)-1,0,-1):
            if(A[index] < A[i]):
                A[i],A[index] = A[index],A[i]
                break
        A[index+1:] = A[index+1:][::-1]
        return A