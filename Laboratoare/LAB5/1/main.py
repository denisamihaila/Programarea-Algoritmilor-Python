def citire():
    global nr, lista
    nr = int(input("nr = "))
    lista = [int(x) for x in input("lista = ").split()]

def functie(s, x, i, j): #primul element strict mai mare decat x din s[i:j]
    for n in s[i:j]:
        if n > x:
            return n
    return -1

citire()
print(nr)
print(lista)
ok = 1
for i in range(nr-1):
    if functie(lista, lista[i], i+1, nr) != -1:
        ok = 0
if ok == 1:
    print("descrescator")
else:
    print("nu e descrescator")