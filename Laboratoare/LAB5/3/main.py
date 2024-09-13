def functie(cuv, out, *fisiere):
    g = open(f"{out}", "w")
    for fisier in fisiere:
        f = open(f"{fisier}", "r")
        l = []
        s = f.readline()
        i = 1
        ok = 0
        while s != "":
            if cuv in s.lower():
                l.append(i)
                ok = 1
            s = f.readline()
            i += 1
        g.write(fisier + ' ')
        if ok == 1:
            for x in l:
                g.write(str(x) + " ")
        else:
            g.write("nu apare aici")
        f.close()
        g.write("\n")
    g.close()

functie("floare","rez.txt", "eminescu.txt", "paunescu.txt")