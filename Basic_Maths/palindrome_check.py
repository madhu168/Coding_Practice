n=int(input())  
# taking n as a input 
## write your code !!

n = str(n)
m = n
n = n[::-1]
if(m == n):
    print("true")
else:
    print("false")