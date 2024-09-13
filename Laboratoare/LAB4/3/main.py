f1 = open("cuvinte1.in")
f2 = open("cuvinte2.in")
d = {}
s = f1.readline()
while s != "":
    cuvinte = s.split()
    for cuv in cuvinte:
        if cuv in d:
            d[cuv] += 1
        else:
            d[cuv] = 1
    s = f1.readline()
s = f2.readline()
while s != "":
    cuvinte = s.split()
    for cuv in cuvinte:
        if cuv in d:
            d[cuv] += 1
        else:
            d[cuv] = 1
    s = f2.readline()
print("a)")
print(d)
print("b)")
print(*sorted(d), sep=" ")
f1.close()
f2.close()