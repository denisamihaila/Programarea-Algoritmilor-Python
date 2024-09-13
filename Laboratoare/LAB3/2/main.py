v = [1, 1, 2, 2, 2, 3, 1, 3]
fr = [0 for i in range(1, 101)]
nr = 0
for x in v:
    fr[x] += 1
for i in range(1, 100):
    nr += fr[i] // 2
print(nr)