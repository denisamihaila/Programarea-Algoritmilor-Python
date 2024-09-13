m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    a = [int(x) for x in input().split()]
    matrix.append(a)
maxime = []
for i in range(m):
    max = matrix[i][0]
    for j in range(1,n):
        if matrix[i][j] > max:
            max = matrix[i][j]
    maxime.append(max)
print(maxime)

'''''
Altfel: 
maxime = [max(b) for b in matrix]