n = int(input("n = "))
for i in range(n):
    x = int(input())
    if i == 0:
        mini = x
        maxi = x
    else:
        if x < mini:
            mini = x
        else:
            if x > maxi:
                maxi = x

print(f"Minimul:{mini} Maximul:{maxi}")
