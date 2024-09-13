s = input("text: ")
s1 = s
k = int(input("k = "))
ls = []
nr_litere = ord('z')-ord('a') + 1
for x in s:
    if x.isalpha():
        if x.islower(): #sau if 'a'<=x<='z'
            c = (ord(x)-ord('a')+k) % nr_litere #a cata litera este dupa mutare cu k pozitii la dreapta
            ls.append(chr(c+ord('a'))) #litera a c-a din alfabet
        else:
            c = (ord(x) - ord('A') + k) % nr_litere  # a cata litera este dupa mutare cu k pozitii la dreapta
            ls.append(chr(c + ord('A')))  # litera a c-a din alfabet
    else:
        ls.append(x)
s = "".join(ls)
print(s)