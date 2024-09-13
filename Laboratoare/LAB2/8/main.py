s = input("s = ")
cs = s
l = []
i = 0
suma = 0
while i < len(s):
    if s[i].isnumeric():
        nr = int(s[i])
        i += 1
        while (i < len(s)) and s[i].isnumeric():
            nr = nr * 10 + int(s[i])
            i += 1
        i = i + 1
        print("nr=", nr)
        suma = suma + nr
    else:
        i = i + 1

print(suma)