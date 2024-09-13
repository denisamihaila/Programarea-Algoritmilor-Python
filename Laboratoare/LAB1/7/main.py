n = int(input("n = "))
s = 0
for i in range(n):
    x = int(input())
    s = s ^ x
print(s)