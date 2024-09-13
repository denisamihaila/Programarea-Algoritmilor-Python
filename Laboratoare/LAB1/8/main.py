n = int(input("n = "))
x = 0
for i in range (1,n):
    v = int(input(f"v[{i}] = "))
    x = x ^ i ^ v
x = x ^ n
print(x)