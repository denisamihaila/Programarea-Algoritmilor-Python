def func(cnp, dict):
    try:
        nota = int(dict[cnp][1][0])
        nota += 1
        return nota
    except KeyError:
        return None
def adauga(cnp, note, dict):
    try:
        dict[cnp][1].extend(note)
        return dict[cnp][1]
    except KeyError:
        return None
def fd(cnp, dict):
    del dict[cnp]
f = open("elevi.in")
g = open("elevi.out")
s = f.readline()
d = {}
while s != "":
    date = s.split()
    nume = date[1] + ' ' + date[2]
    d[date[0]] = [nume, date[3:]]
    s = f.readline()
print(d)
'''''
PUNCTUL B
cnp = input("cnp: ")
print(func(cnp, d))
'''''

'''''
PUNCTUL C
note = [10,8]
cnp = input("cnp: ")
print(adauga(cnp, note, d))
'''''

'''''
#PUNCTUL D
cnp = input("cnp: ")
fd(cnp, d)
print(d)
'''''
lista = []
for x in d:
    l = []
    l.extend(d[x])
    lista.append(l)
def lala(x):
    s = 0
    for y in x[1]:
        s += int(y)
    return s
lista.sort(key = lala, reverse = True)
print(lista)
f.close()
g.close()