m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    l = [int(x) for x in input().split()]
    matrix.append(l)
matrix.append(l) #adugam linia m
k = int(input("k = "))
l = [0 for i in range(n)]
matrix.insert(k+1, l)
for i in range(m+1):
    print(*matrix[i], sep = " ")
