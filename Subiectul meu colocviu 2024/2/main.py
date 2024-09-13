def candidati_respinsi(d, *sir, punctaj_admis = 50):
    rezultat = []
    for nume_post in sir:
        for nume in d[nume_post]:
            nota1 = int(d[nume_post][nume][0])
            nota2 = int(d[nume_post][nume][1])
            media = 0.4*nota1 + 0.6*nota2
            if nota1 == 0 or nota2 == 0 or media < punctaj_admis:
                tuplu = (nume_post, nume, [nota1, nota2])
                rezultat.append(tuplu)
    rez = sorted(rezultat, key = lambda tuplu: (tuplu[0], -(0.4*tuplu[2][0]+0.6*tuplu[2][1]), -tuplu[2][0]))
    return rez

def elimina_candidati(d, candidati_eliminati, k):
    nr = 0
    for i in range(len(candidati_eliminati)):
        del d[candidati_eliminati[i][1]][candidati_eliminati[i][0]]
    for nume_post in d:
        if len(nume_post) >= k:
            nr += 1
    return nr

f = open("concurs.in", "r")
d = {}
for line in f:
    if line[:5] == "Post:":
        nume_post = line[6:-10]
        nr_proba = int(line[-2])
        if nume_post not in d:
            d[nume_post] = {}
    else:
        elements = line.split(" ")
        nume = elements[0] + " " + elements[1] #numele candidatului
        nota = elements[2][:-1] #nota obtinuta pentru nume_post la nr_proba
        if nr_proba == 1:
            d[nume_post][nume] = []
        d[nume_post][nume].append(nota)

print(d)
print(candidati_respinsi(d, "Programator 1", punctaj_admis = 50))
nume_candidat = input()
nume_post = input()
print(elimina_candidati(d,[(nume_candidat,nume_post)], 4))
f.close()