n = int(input("n = "))
copie = n
inv = 0
while n > 0:
    inv = inv * 10 + n % 10
    n //= 10
if copie == inv:
    print("palindrom")
else:
    print("nu e palindrom")
