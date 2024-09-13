n = int(input("n = "))
arr = [i for i in range(1, n+1)]
for i in range(1 << n):
        # Loop through all elements of the input array
    for j in range(n):
            #Check if the jth bit is set in the current subset
        if (i & (1 << j)) != 0:
                #If the jth bit is set, add the jth element to the subset
            print(arr[j], end=" ")
    print()
