import random
#print(random.randrange(1,100))
n = int(input("n = "))
m = int(input("m = "))
matrix = []
for i in range(n):
    linie = []
    for j in range(m):
        linie.append(random.randrange(1,100))
    matrix.append(linie)
for linie in matrix:
    print(*linie, sep = " ")