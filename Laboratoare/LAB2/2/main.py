s = input("s = ")
print(" " + s)
for i in range (1, len(s) // 2):
    print(s[i:-i].center(10," "))