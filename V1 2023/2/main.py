def premianti(d, *nr, k):
    rezultat = []
    for echipa in d:
        for membru in d[echipa]:
            scoruri = sorted([int(x) for x in d[echipa][membru]])
            tokenMembru = [echipa, membru]
            premiat = []
            medie = 0
            for scor in scoruri:
                if scor in nr:
                    premiat.append(scor)
                    medie += scor
            if len(premiat) > k:
                tokenMembru.append(premiat)
                tokenMembru.append(round(float(medie/len(premiat)), 2))
                rezultat.append(tokenMembru)
    rezultat = sorted(rezultat, key = lambda x: x[-1], reverse=True)
    return rezultat

def stergere(d, nume_echipa, nume_membru):
    del d[nume_echipa][nume_membru]
    if(len(d[nume_echipa]) > 1):
        return d[nume_echipa]
    else:
        for nume in d[nume_echipa].keys():
            mesaj = "Am sters si jucatorul " + str(nume) + " si echipa " + str(nume_echipa)
        del d[nume_echipa]

        return mesaj

f = open("punctaje.in", "r")
d = {}
nume_echipa = ""
for line in f:
    if line[:6] == 'Echipa':
        nume_echipa = line[7:].strip()
        d[nume_echipa] = {}
    else:
        d[nume_echipa][line[:line.find(':')-1]] = line[line.find(':')+1:].split()

f.close()
premianti(d, 50, 25, 40, 60, 30, 45, k=3)
print(stergere(d, "Potiuni magice", "Strumfita"))
print(stergere(d, "Potiuni magice", "Papa Strumf"))