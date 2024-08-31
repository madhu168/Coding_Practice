k = 3
a = [20, 7, 5, 4]

a.sort()
q = []
while k > 0:
    if len(q) == 0:
        temp = a[-1]
        del a[-1]
        q.append(temp // 2)
        k -= 1
    else:
        temp = a[-1]
        if q[0] > temp:
            temp = q.pop(0)
            q.append(temp // 2)
        else:
            del a[-1]
            q.append(temp // 2)
        k -= 1
    print(q)

print(sum(q) + sum(a))
