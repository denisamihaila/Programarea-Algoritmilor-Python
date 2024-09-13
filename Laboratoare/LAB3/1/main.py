def prim(n):
    nrdiv = 0
    for d in range (1, n+1):
        if n % d == 0:
            nrdiv += 1
    if nrdiv == 2:
        return 1
    else:
        return 0

n = int(input("n = "))
l = []
for x in range (2, n+1):
    if prim(x) == 1:
        l.append(x)
print(l)