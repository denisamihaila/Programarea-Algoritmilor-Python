f = open("studenti.in", "r")
s = f.readline().split(", ")
d = {} #grupa: studenti
dict = {} #student: note
while s[0] != "":
    student = s[0] + ' ' + s[1]
    grupa = s[2]
    note = s[3:]
    if grupa in d:
        d[grupa].append(student)
    else:
        d[grupa] = [student]
    if student in dict:
        dict[student].append(note)
    else:
        dict[student] = note
    s = f.readline().split(", ")
print("a) Studentii din fiecare grupa:\n")
print(d)

grupa = input("\nb) Grupa:")
for student in d[grupa]:
    s = 0
    ok = 1 #presupunem ca e integralist
    if len(dict[student]) == 5:
        for nota in dict[student]:
            if int(nota) < 5:
                ok = 0
            s += int(nota)
        media = s // 5
    if ok == 1:
        print(f"{student} {media}")
    else:
        print(f"{student} restantier")
f.close()