n = int(input("n = "))
matrix = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(i*n+j+1)
    matrix.append(a)
print(matrix)
for i in range(n // 2):
    for j in range(i, n - i):
        print((i, j))
    for j in range(i, n - i):
        print((j, n - i + 1))
    for j in range (n - i + 1, i + 1, -1):
        print((n - i + 1, j))
    for j in range(n - i + 1, i + 1, -1):
        print((j,i))