a = int(input("a = "))
b = int(input("b = "))
x = 1
y = 1
while y < a:
    y = y + x
    x = y - x
print(y)

