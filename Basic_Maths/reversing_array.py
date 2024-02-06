from typing import List

a = []

def printNos(x: int) -> List[int]: 
    # Write your code here
    a.append(x)
    if(x==1):
        return a[::-1]
    return printNos(x-1)