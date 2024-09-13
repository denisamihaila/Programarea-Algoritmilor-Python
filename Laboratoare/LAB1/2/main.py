n = int(input("n = "))
dif = 0
for i in range(n):
    z = float(input(f"ziua {i+1}: "))
    if i > 0:
        if z - ant > dif:
            dif = round(z - ant, 2)
            z1 = i
            z2 = i + 1
    ant = z
print(f"{dif} RON, între zilele {z1} si {z2}")