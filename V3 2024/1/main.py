def playlist(d, *genuri, durata_minima = "02:00", durata_maxima = "03:30"):
    rez = []
    for gen in genuri:
        for artist in d[gen]:
            for list in d[gen][artist]:
                durata = list[1]
                if durata_minima <= durata <= durata_maxima:
                    token = (gen, artist, list[0], durata)
                    rez.append(token)
    rez.sort(key=lambda tuplu: (tuplu[1], tuplu[2]))
    rez.sort(key=lambda tuplu: (tuplu[3]), reverse=True)
    return rez

def adauga_melodie(d, gen, titlu, artist, durata):
    if gen in d:
        if artist not in d[gen]:
            d[gen][artist] = []
        d[gen][artist].append([titlu, durata])
        nr = 0
        for artist in d[gen]:
            nr += len(d[gen][artist])
        sir = f"Genul {gen} contine acum {nr} melodii"
        return sir
    else:
        return "Nu exista acest gen muzical."

f = open("melodii.in")
d = {}
for line in f.readlines():
    if line[:6] == "Gen >>":
        gen = line[7:-1]
        d[gen] = {}
    else:
        elements = line.split(" / ")
        if elements[2][-1] == "\n":
            elements[2] = elements[2][:-1]
        titlu = elements[0]
        artist = elements[1]
        durata = elements[2]
        if artist not in d[gen]:
            d[gen][artist] = []
        d[gen][artist].append([titlu, durata])

print(d)
print(playlist(d, "Rock", "Hip-Hop"))
adauga_melodie(d, "Rock", "a", "b", "c")
print(d)
f.close()