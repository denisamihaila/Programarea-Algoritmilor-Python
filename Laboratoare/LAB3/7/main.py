m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    l = [int(x) for x in input().split()]
    matrix.append(l)
new = []
for i in range(n):
    l = [0 for _ in range(m)]
    new.append(l)
for j in range(m):
    for i in range(n):
        new[i][j] = matrix[j][i]
for i in range(n):
    print(*new[i], sep = " ")