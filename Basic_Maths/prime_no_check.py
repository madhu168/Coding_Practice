n = int(input())
if(n <= 1):
    print("NO")
for i in range(2,math.sqrt(n)+1):
    if(n%i==0):
        print("NO")
        return;
print("YES")