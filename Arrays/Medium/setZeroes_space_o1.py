matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
col0 = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            if j != 0:
                matrix[0][j] = 0
            else:
                col0 = 0
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[i])):
        if matrix[i][j] != 0:
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

if matrix[0][0] == 0:
    for j in range(len(matrix[0])):
        matrix[0][j] = 0

if col0 == 0:
    for i in range(len(matrix)):
        matrix[i][0] = 0

print(matrix)
            
        