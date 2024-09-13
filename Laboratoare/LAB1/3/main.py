L1 = int(input("L1 = "))
L2 = int(input("L2 = "))
arie_dreptunghi = L1 * L2
#calculam cmmdc(L1,L2)
while L1 != L2:
    if L1 > L2:
        L1 -= L2
    else:
        L2 -= L1
#in L1 si L2 se afla cmmdc
arie_patrat = L1 * L1
numar_placi = arie_dreptunghi // arie_patrat
print(f"{numar_placi} placi de gresie cu latura de {L1} cm")