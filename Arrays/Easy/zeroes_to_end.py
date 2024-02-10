def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    non_nums_zeros = []
    count = 0
    for i in range(len(a)):
        if(a[i] != 0):
            non_nums_zeros.append(a[i])
        else:
            count += 1
    non_nums_zeros += [0] * count
    return non_nums_zeros
