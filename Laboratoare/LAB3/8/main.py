m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    l = [int(x) for x in input().split()]
    matrix.append(l)
nr = [x for x in matrix[i] for i in range(m) if x % 2 == 0]
print(len(nr))