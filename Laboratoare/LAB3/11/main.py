n = int(input("n = "))
matrix = []
matrix.append([1]) #prima linie e 1
matrix.append([1, 1]) #a doua linie e 1 1
for i in range(2, n): #de la a 2-a la ultima linie
    a = []
    a.append(1)   #adaugam primul element din linie
    for j in range(1, i-1): #de la al doilea la penultimul termen din linie
        suma = matrix[i-1][j-1] + matrix[i-1][j]
        a.append(suma)
    a.append(1)
    matrix.append(a)
print(matrix)