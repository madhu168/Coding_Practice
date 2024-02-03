from typing import List

def generateFibonacciNumbers(n: int) -> int: 
    # Write your code here
    if(n<=1):
        return n
    last = generateFibonacciNumbers(n-1)
    second_last = generateFibonacciNumbers(n-2)
    print("last:",last)
    print("second_last:",second_last)
    print("n:",n)
    return last + second_last


print(generateFibonacciNumbers(4))