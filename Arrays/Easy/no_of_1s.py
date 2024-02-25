n = 25
counter = 0
while n:
    n &= n-1
    counter += 1
print(counter)