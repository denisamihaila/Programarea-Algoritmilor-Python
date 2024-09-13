def functie(*nr):
    x = 0
    for n in nr:
        x = x * 10
        x += int(max(str(n)))
    return x
def f2(a, b, c):
    x = functie(a, b, c)
    if int(max(str(x))) <= 1:
        return True
    else:
        return False
print(f2(1001, 11, 100))
print(f2(1001, 17, 100))