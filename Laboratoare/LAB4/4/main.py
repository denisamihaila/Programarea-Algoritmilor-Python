f = open("test.in")
g = open("test.out", "w")
s = f.readline()
copie = s
delimiters = ["*","="]
ok = 1
while s != "":
    for delimiter in delimiters:
        s = s.replace(delimiter, ' ')
    numere = s.split()
    if int(numere[0]) * int(numere[1]) == int(numere[2]):
        g.write(f"{copie} Corect\n")
        ok += 1
    else:
        g.write(copie + " Gresit " + str(int(numere[0]) * int(numere[1])) + "\n")
    s = f.readline()
    copie = s
g.write(f"Nota {ok}")
f.close()
g.close()