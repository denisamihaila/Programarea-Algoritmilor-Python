def citire_propozitii():
    f = open("propozitii.in")
    p = []
    s = f.readline()
    while s != "":
        if s[len(s)-1] == "\n":
            p.append(s[:-1])
        else:
            p.append(s)
        s = f.readline()
    f.close()
    return p

def sterge_cuvant(lista_propozitii, x):
    new_list = []
    for prop in lista_propozitii:
        prop = prop.replace(x, "")
        prop = prop.replace("  ", " ")
        if prop != " ":
            new_list.append(prop)
    lista_propozitii = new_list
    for prop in lista_propozitii:
        print(prop, sep = "\n")

p = citire_propozitii()
print(p)
#punctul b)
k = int(input("k = "))
g = open("litere.out", "w")
l = []
for prop in p:
    for cuv in prop.split():
        s = set(cuv)
        if(len(s) <= k):
            l.append(cuv)
lista = set(l)
l = list(lista)
l.sort(reverse = True)
for x in l:
    g.write(x + "\n")
g.close()
#punctul c
sterge_cuvant(p, "nu")
