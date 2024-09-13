import math
n = int(input("n = "))
k = int(input("k = "))
b = int(input("b = "))
k -= 1
if b == 1:
    n = n | (1 << k)
else:
    x = math.log(n, 2)
    x = int(ceil(x))
    a = (1 << x) - 1
    a = a ^ (1 << k)
    n = n & a
print(n)
