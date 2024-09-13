m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    l = [int(x) for x in input().split()]
    matrix.append(l)
k = int(input("k = "))
for i in range(m):
    l = [0 for _ in range(n)]
    for j in range(n):
        x = (j + k) % n
        l[x] = matrix[i][j]
    for y in range(n):
        matrix[i][y] = l[y]
    print(*matrix[i], sep = " ")
