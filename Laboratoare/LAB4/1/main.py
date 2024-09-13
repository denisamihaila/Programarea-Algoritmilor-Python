def rimeaza(a,b):
    global p
    x = len(a)
    y = len(b)
    if a[x-p:x] == b[y-p:y]:
        return 1
    else:
        return 0

f = open("rime.in", "r")
g = open("rime.out", "w")
p = int(input("p = "))
cuvinte = [] #lista cu toate cuvintele
d = {}  #dictionar
s = f.readline()
while s != "":
    cuvinte.extend([x for x in s.split()])
    s = f.readline()
for cuv in cuvinte: #pt fiecare cuvant din rime.in
    ok = 0
    for x in d:
        if rimeaza(cuv,x) == 1:
            ok = 1
            d[x].append(cuv)
    if ok == 0:
        d[cuv] = []
#res = ''.join(sorted(d, key = lambda x : len(d[x]), reverse = True))
sorted_d = dict(sorted(d.items(), key = lambda x : len(x[1]), reverse = True))
for cuv in sorted_d:
    g.write(f"{cuv} ")
    for x in d[cuv]:
        g.write(f"{x} ")
    g.write(f"\n")
f.close()
g.close()