p = input("p = ")
s = input("s = ")
t = input("t = ")
#v1
l = [x if x != s else t for x in p.split(" ")]
p = " ".join(l)
print(p)
#v2- inlocuire manuala - caut cuvantul si testez daca este incadrat de spatii
rezultat = p
poz = rezultat.find(s)
lung_s=len(s)
while poz != -1:
    if (poz == 0 or rezultat[poz-1].isalpha() == False) and (poz+lung_s == len(rezultat) or rezultat[poz+lung_s].isalpha() == False):
        rezultat = rezultat[:poz] + t+rezultat[poz+lung_s:]
    poz = rezultat.find(s, poz+len(t))

print("\nSirul dupa inlocuiri:")
print(rezultat)