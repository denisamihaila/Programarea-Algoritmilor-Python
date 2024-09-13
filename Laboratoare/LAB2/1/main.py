s = input("Sirul s: ")
x = s[0]
s = s.replace(x, "")
#metoda 1 de afisare:
print(f"După ștergerea literei {x}, sirul obtinut este {s} de lungime {len(s)}")
#metoda 2 de afisare:
y = "După ștergerea literei {}, sirul obtinut este {} de lungime {}"
y = y.format(x, s, len(s))
print(y)