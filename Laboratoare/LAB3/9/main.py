m = int(input("m = "))
n = int(input("n = "))
matrix = []
for i in range(m):
    l = [int(x) for x in input().split()]
    matrix.append(l)
sume = [sum(i)-max(i) for i in matrix]
print(sume)
