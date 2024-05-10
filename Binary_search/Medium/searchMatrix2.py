from typing import *

def searchElement(matrix : List[List[int]], target : int) -> int:
    # Write your code here.
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m-1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return 1
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    
    return -1