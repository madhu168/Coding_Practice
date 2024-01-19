def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    ans = 0
    for i in range(1,n+1):
        ans = ans + (n//i) * i
    return ans