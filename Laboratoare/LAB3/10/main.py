m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
for i in range(m):
    for j in range(i+1, n):
        if matrix[i][0] > matrix[j][0]:
            matrix[i] , matrix[j] = matrix[j], matrix[i]
print(matrix)