import copy
def citire_cuvinte():
    f = open("cuvinte.in", "r")
    matrix = []
    text = f.read()
    for prop in text.split("\n"):
        l = prop.split()
        matrix.append(l)
    f.close()
    return matrix

def insereaza_inainte(matrice_cuvinte, x, y):
    new_matrix = []
    for linie in matrice_cuvinte:
        list = []
        for cuv in linie:
            if cuv == x:
                list.append(y)
            list.append(cuv)
        linie = list
        new_matrix.append(linie)
    k = max(len(linie) for linie in new_matrix)
    for linie in new_matrix:
        if len(linie) < k:
            for i in range(k - len(linie)):
                linie.append(".")
    matrice_cuvinte = copy.deepcopy(new_matrix)
    print(matrice_cuvinte) #AICI FUNCTIONEAZA

c = citire_cuvinte()
k = int(input("k = "))
voc = "aeiou"
rezultat = []
for prop in c:
    for cuv in prop:
        nr = 0
        for litera in cuv:
            if litera in voc:
                nr += 1
        if nr >= k:
            rezultat.append(cuv)
g = open("vocale.out", "w")
rezultat = list(set(rezultat))
rezultat = sorted(rezultat, reverse=True)
for cuv in rezultat:
    g.write(cuv + "\n")
g.close()

#matrice_cuvinte = copy.deepcopy(citire_cuvinte())
#insereaza_inainte(matrice_cuvinte, "este", "nu")
#for row in matrice_cuvinte: #AICI NU A MODIFICAT-O
#    print(*row)
insereaza_inainte(c, "este", "nu")
for row in c:
    print(*row)