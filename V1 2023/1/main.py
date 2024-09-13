import math
def citire_matrice(fisier):
    f = open(f"{fisier}","r")
    matrix = []
    s = f.readline()
    n = s[:-1]
    n = int(n)
    for i in range(int(math.sqrt(n))):
        l = []
        for j in range(int(math.sqrt(n))):
            s = f.readline()
            x = s[:-1]
            x = int(x)
            l.append(x)
        matrix.append(l)
    f.close()
    return matrix

def prelucrare_matrice(m):
    n = len(m)
    for i in range(n):
        val = m[i][i]
        for j in range(n):
            m[i][j] -= val
        del(m[i][i])
    return(m)

for line in prelucrare_matrice(citire_matrice("matrice.in")):
    print(*line, sep = " ")

m = citire_matrice("matrice.in")
k = int(input("k = "))
g = open("numere.out", "w")
l = []
ok = 0
for linie in m:
    for nr in linie:
        s = 0
        for cifra in str(nr):
            s += int(cifra)
        if s == k:
            l.append(nr)
            ok = 1
if ok == 1:
    for nr in l:
        x = str(nr)
        g.write(x+' ')
else:
    g.write("Imposibil!")
g.close()


